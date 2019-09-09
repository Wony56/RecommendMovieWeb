from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Rating, Movie 
from django.contrib.auth.models import User

# from api.serializers import MovieSerializer
from rest_framework.response import Response
import datetime

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