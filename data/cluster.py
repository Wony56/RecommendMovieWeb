from sklearn.cluster import KMeans
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import requests
import json

API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}


# #클러스터의 개수 지정(n개)
# num_clusters = n
# #알맞은 매트릭스 Z 삽입
# km = KMeans(n_clusters=num_clusters)
# km.fit(Z)
def get_movies():
    movie_data = open('./movies.dat','r',encoding='ISO-8859-1')
    data_set = []

    for line in movie_data.readlines():
        [movieid,title,genres]=line.split('::')
        movieid = int(movieid)
        year = int(title[-5:-1])
        genres = genres[:-1].split('|')
        genre_map = {
        "Action":0,"Adventure":1,"Animation":2,"Children's":3,"Comedy":4,
        "Crime":5,"Documentary":6,"Drama":7,"Fantasy":8,"Film-Noir":9,"Horror":10,
        "Musical":11,"Mystery":12,"Romance":13,"Sci-Fi":14,"Thriller":15,"War":16,
        "Western":17
        }

        genreid = 0
        for genre in genres:
            genreid += genre_map[genre]*genre_map[genre]
        data_set.append([year,genreid*31,movieid])

    return np.array(data_set)

def get_users():
    user_data = open('./users.dat', 'r', encoding='ISO-8859-1')
    data_set = []
    # rating_data = get_ratings()
    # print(rating_data)
    for line in user_data.readlines():
        [userid, gender, age, occupation, zipcode] = line.split('::')
        username = int(userid)
        age = int(age)
        occupation = int(occupation)
        if gender == 'M':
            gender=1
        else :
            gender=2
        data_set.append([
            age,
            gender,
            occupation*occupation
        ])

    return np.array(data_set)

# cluster_num 구하기
def elbow(X):

    print(X)
    sse = []

    for i in range(1,20):
        km = KMeans(n_clusters=i).fit(X)
        sse.append(km.inertia_)

    plt.plot(range(1,20), sse, marker='o')
    plt.xlabel('K')
    plt.ylabel('SSE')
    plt.show()

def KMeans_movie(X):
    kmeans = KMeans(n_clusters=17)
    # print(X[:,0:2])
    kmeans.fit(X[:,0:2])
    # y_pred = kmeans.predict(X)
    labels = kmeans.labels_

    fig = plt.figure(figsize=(10,10))
    # print("AAA",X[:,1])
    # print("bbbb",X[:,0])
    # print("cccc",labels.astype(np.float))
    plt.scatter(X[:,1],X[:,0],c=labels.astype(np.float),s=10)
    plt.ylabel('year')
    plt.xlabel('genre')
    print(labels)
    plt.show()
    return labels

def KMeans_user(X):

    kmeans = KMeans(n_clusters=4).fit(X)
    fig= plt.figure(figsize=(10,10))
    ax = Axes3D(fig,rect=[0,0,.95,1],elev=48,azim=134)
    # kmeans.fit(X)
    labels=kmeans.labels_
    # print(labels)
    ax.scatter(X[:, 0], X[:, 1], X[:, 2],c=labels.astype(np.float))
    ax.w_xaxis.set_ticklabels([])
    ax.w_yaxis.set_ticklabels([])
    ax.w_zaxis.set_ticklabels([])
    ax.set_xlabel('AGE')
    ax.set_ylabel('GENDER')
    ax.set_zlabel('OCCUPATION')
    ax.set_title('KMEANS')
    ax.dist = 12
    
    plt.show()
    
    return labels

def create_usercluster(cdatas):
    request_data={'cluster_data':[]}
    # cdatas = cdatas.tolist()
    # print(cdatas.tolist()) 
    for cdata in cdatas:
        request_data['cluster_data'].append({
            'group': str(cdata)
        })
    
    # print(request_data)
    response = requests.post(API_URL + 'cluster/clusterUser/', data=json.dumps(request_data), headers=headers)

def create_moviecluster(cdatas,moviedatas):
    request_data={'cluster_data':[]}
    # cdatas = cdatas.tolist()
    # print(cdatas.tolist()) 
    # print(len(cdatas))
    # print(moviedatas)
    for idx,cdata in enumerate(cdatas):
        # print(moviedatas[idx][2],cdata)
        request_data['cluster_data'].append({
            'movieId': str(moviedatas[idx][2]),
            'group': str(cdata)
        })
    
    # print(request_data)
    response = requests.post(API_URL + 'cluster/clusterMovie/', data=json.dumps(request_data), headers=headers)

if __name__ == '__main__':
    users_set  = get_users()
    # elbow(users_set)
    user_cdata=KMeans_user(users_set)
    create_usercluster(user_cdata)

    movies_set = get_movies()
    # elbow(movies_set)
    movie_cdata=KMeans_movie(movies_set)
    create_moviecluster(movie_cdata,movies_set)