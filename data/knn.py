import pandas as pd
import numpy as np
import requests
import json

API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}

def get_users(): 
    unames = ['userid','gender','age','occupation','zipcode']
    df = pd.read_csv('./users.dat',sep='::',engine= 'python',names=unames)
    return df

def get_ratings():
    unames = ['userid','movieid','rating','timestamp']
    df = pd.read_csv('./ratings.dat',sep='::',engine= 'python',names=unames)
    # print(df)
    return df

def get_movies():
    unames = ['movieid','title','genres']
    df = pd.read_csv('./movies.dat',sep='::',engine= 'python',names=unames)

    genre = pd.DataFrame(df.genres.str.split('|').tolist()).stack().unique()
    genre = pd.DataFrame(genre,columns=['genre'])
    genre = genre.sort_values(["genre"], ascending=[True])
    genre = genre.reset_index(drop=True)

    df = df.join(df.genres.str.get_dummies().astype(int))
    df.drop('genres',inplace=True,axis=1)
    # print(df)

    return df, genre

if __name__ == '__main__':
    # idx =1
    user_df = get_users()
    ratings_df = get_ratings()
    movie_df , genre= get_movies()
    ages = [1,18,25,35,45,50,56]

    age_genre_df = pd.DataFrame(genre,columns=['genre',1,18,25,35,45,50,56])
    # age_genre_df
    # pd.get_dummies(demo_df, columns=['숫자 특성', '범주형 특성'])

    ages = [1,18,25,35,45,50,56]
    for idx in ages:
        user_df[user_df['age']==idx]

        usersid = user_df[user_df['age']==idx]['userid']

        age_genre_df[idx]=0

        for i in usersid:
            moviesid = ratings_df[ratings_df['userid']==i]['movieid']

            movie = movie_df.loc[movie_df['movieid'].isin(moviesid)]

            aaa=pd.DataFrame(movie.sum(axis=0))

            svalue = movie.sum(axis=0)['Action':]

            age_genre_df[idx] += svalue.values

    # print(age_genre_df.idxmax())
    max=pd.Series(age_genre_df[[1,18,25,35,45,50,56]].astype(float).idxmax())
    print(max)
    print(age_genre_df.iloc[max,0])
    print(age_genre_df)

    request_data={'knn_data':[]}
   
    for idx,i in enumerate([1,18,25,35,45,50,56]):
        request_data['knn_data'].append({
            'age':i,
            'Action':age_genre_df.iloc[0,idx+1],
            'Adventure':age_genre_df.iloc[1,idx+1],
            'Animation':age_genre_df.iloc[2,idx+1],
            "Children's":age_genre_df.iloc[3,idx+1],
            'Comedy':age_genre_df.iloc[4,idx+1],
            'Crime':age_genre_df.iloc[5,idx+1],
            'Documentary':age_genre_df.iloc[6,idx+1],
            'Drama':age_genre_df.iloc[7,idx+1],
            'Fantasy':age_genre_df.iloc[8,idx+1],
            'Film-Noir':age_genre_df.iloc[9,idx+1],
            'Horror':age_genre_df.iloc[10,idx+1],
            'Musical':age_genre_df.iloc[11,idx+1],
            'Mystery':age_genre_df.iloc[12,idx+1],
            'Romance':age_genre_df.iloc[13,idx+1],
            'Sci-Fi':age_genre_df.iloc[14,idx+1],
            'Thriller':age_genre_df.iloc[15,idx+1],
            'War':age_genre_df.iloc[16,idx+1],
            'Western':age_genre_df.iloc[17,idx+1],
            'max_genre':age_genre_df.iloc[max[i],0]
            })
    print(request_data)
    # print(request_data)
    response = requests.post(API_URL + 'recommend/knn_age_view/', data=json.dumps(request_data), headers=headers)
