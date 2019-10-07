from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Rating, Movie 
from django.contrib.auth.models import User

# from api.serializers import MovieSerializer
from rest_framework.response import Response
import datetime

import pandas as pd
import numpy as np
from scipy.sparse.linalg import svds
from api.serializers import MovieSerializer

@api_view(['POST'])
def ratings(request):

    # if request.method == 'GET':
    #     id = request.GET.get('id', request.GET.get('movie_id', None))
    #     title = request.GET.get('title', None)

    #     movies = Movie.objects.all()

    #     if id:
    #         movies = movies.filter(pk=id)
    #     if title:
    #         movies = movies.filter(title__icontains=title)

    #     serializer = MovieSerializer(movies, many=True)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)

    # if request.method == 'DELETE':
    #     movie = Movie.objects.all()
    #     movie.delete()
    #     return Response(status=status.HTTP_200_OK)

    if request.method == 'POST':
        # ratings = Rating.objects.all()
        # print(ratings)
        ratings = request.data.get('ratings', None)
        for rating in ratings:
            # print(rating)
            t = rating.get('timeStamp')
            t = datetime.datetime.fromtimestamp(t)
            userid = rating.get('user', None)
            if userid == None:
                userid = '1'
            user = User.objects.get(username='user'+userid)
            movieid = rating.get('movie', None)
            if movieid == None :
                movieid = '1'
            movie = Movie.objects.get(pk=movieid)
            rating = rating.get('rating', None)
            # timeStamp = 0
            # t = rating.get('timeStamp', None)
            
            #앞에user는 Attribute 뒤에껀 가져온값
            if not (user and movie and rating):
                continue

            Rating(user=user, movie=movie, rating=rating, timeStamp = t).save() 
            #Database에 저장하는 부분

        return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def svd(request):
    if request.method =='GET':
        userid = request.GET.get('username',None)
        
        ratings = Rating.objects.all()

        ratings_df =  pd.DataFrame(list(ratings.values('user__username','movie_id','rating')))

        R_df = ratings_df.pivot(index='user__username',columns='movie_id',values='rating').fillna(0)

        # dataframe을 matrix화
        R = R_df.values
        # 해당 영화의 평점의 평균
        user_ratings_mean = np.mean(R,axis=1)

        # normalization
        R_demeaned = R - user_ratings_mean.reshape(-1,1)

        # svd
        U,sigma,vt = svds(R_demeaned,k=50)
        sigma = np.diag(sigma)

        # cost function(평점 R과 근사한 평점의 차를 구하는 RMSE      + 일반화된 솔루션을 위한 규제항)
        all_user_predicted_ratings = np.dot(np.dot(U,sigma),vt)+user_ratings_mean.reshape(-1,1)

        preds_df = pd.DataFrame(all_user_predicted_ratings,index=R_df.index,columns=R_df.columns)

        already_rated, predictions = recommend_movies(preds_df,userid,ratings_df,10)

        r_movies = predictions['movie_id'].tolist()

        movies = Movie.objects.filter(id__in = r_movies)

        serializer = MovieSerializer(movies, many=True)
        data = serializer.data
        return Response(data = data,status=status.HTTP_200_OK)


def recommend_movies(predictions_df,userid,original_ratings_df,num_recommendations=8):

    movies = Movie.objects.all()
    movies_df =  pd.DataFrame(list(movies.values('id','title','genres')))
    movies_df.rename({'id':'movie_id'},axis=1,inplace=True)

#     예측값으로 추천해줄 영화 정렬
    sorted_user_predictions = predictions_df.loc[userid].sort_values(ascending=False)

#     원본 movie_df
    user_data = original_ratings_df[original_ratings_df.user__username == userid]

#   해당 유저의 평점순으로 movie_df join 정렬(이미본거)
    user_full = (user_data.merge(movies_df,how='left',left_on='movie_id',right_on='movie_id').sort_values(['rating'],ascending=False))

# 안본 영화중에 추천
    recommendations = (movies_df[~movies_df['movie_id'].isin(user_full['movie_id'])].
                      merge(pd.DataFrame(sorted_user_predictions).reset_index(),how='left',
                           left_on='movie_id',
                            right_on='movie_id').
                       rename(columns={userid:'predictions'}).
                       sort_values('predictions',ascending=False).
                       iloc[:num_recommendations]
                      )

    return user_full, recommendations
