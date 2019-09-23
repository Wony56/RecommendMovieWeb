import pandas as pd
import numpy as np

# 파일 나중에 dat가 아니라 db에서 받아와야하지 않을까.....?
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
    df = df.join(df.genres.str.get_dummies().astype(int))
    df.drop('genres',inplace=True,axis=1)
    # print(df)

    return df, genre

if __name__ == '__main__':
    idx =1
    user_df = get_users()
    ratings_df = get_ratings()
    # print(user_df[user_df['age']==idx])

    # users_set  = np.transpose(get_users())
    # obj = pd.DataFrame(data={"userid":users_set[0],"age":users_set[1],"gender":users_set[2],"occupation":users_set[3]})
    # print(obj[obj['age']==idx]['userid'])
    
    # ratings_set = get_ratings()
    # df2 = pd.DataFrame(data={"userid":ratings_set[0],"movieid":ratings_set[1]})
    movie_df , genre= get_movies()
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

    print(age_genre_df.iloc[max,0])
    print(age_genre_df)