import pandas as pd
import numpy as np
from scipy.sparse.linalg import svds

def get_users(): 
    unames = ['userid','gender','age','occupation','zipcode']
    df = pd.read_csv('./users.dat',sep='::',engine= 'python',names=unames)
    return df

def get_ratings():
    unames = ['userid','movieid','rating','timestamp']
    df = pd.read_csv('./ratings.dat',sep='::',engine= 'python',names=unames)
    return df

def get_movies():
    unames = ['movieid','title','genres']
    df = pd.read_csv('./movies.dat',sep='::',engine= 'python',names=unames)

    genre = pd.DataFrame(df.genres.str.split('|').tolist()).stack().unique()
    genre = pd.DataFrame(genre,columns=['genre'])
    df = df.join(df.genres.str.get_dummies().astype(int))
    df.drop('genres',inplace=True,axis=1)

    return df

def recommend_movies(predictions_df,userid,movies_df,original_ratings_df,num_recommendations=8):
    user_row_number = userid-1
    # 예측값으로 추천해줄 영화 정렬
    sorted_user_predictions = predictions_df.iloc[user_row_number].sort_values(ascending=False)
    
    # 원본 movie_df
    user_data = original_ratings_df[original_ratings_df.userid == (userid)]

    # 해당 유저의 평점순으로 movie_df join 정렬(이미본거)
    user_full = (user_data.merge(movies_df,how='left',left_on='movieid',right_on='movieid').sort_values(['rating'],ascending=False))

    # 안본 영화중에 추천
    recommendations = (movies_df[~movies_df['movieid'].isin(user_full['movieid'])].
                      merge(pd.DataFrame(sorted_user_predictions).reset_index(),how='left',
                           left_on='movieid',
                            right_on='movieid').
                       rename(columns={user_row_number:'predictions'}).
                       sort_values('predictions',ascending=False).
                       iloc[:num_recommendations,:-1]
                      )
    print(recommendations)
    return user_full, recommendations

if __name__ == '__main__':
    movies_df = get_movies()
    ratings_df = get_ratings()
    users_df = get_users()

    R_df = ratings_df.pivot(index = 'userid',columns = 'movieid',values = 'rating').fillna(0)

    R = R_df.values

    user_ratings_mean = np.mean(R,axis=1)
    # normalization
    R_demeaned = R - user_ratings_mean.reshape(-1,1)

    # svd
    U,sigma,vt = svds(R_demeaned,k=50)
    sigma = np.diag(sigma)
    # cost function(평점 R과 근사한 평점의 차를 구하는 RMSE  + 일반화된 솔루션을 위한 규제항)
    all_user_predicted_ratings = np.dot(np.dot(U,sigma),vt)+user_ratings_mean.reshape(-1,1)
    # 예측 평점
    preds_df = pd.DataFrame(all_user_predicted_ratings,columns=R_df.columns)

    already_rated, predictions = recommend_movies(preds_df,837,movies_df,ratings_df,10)
    print(predictions)