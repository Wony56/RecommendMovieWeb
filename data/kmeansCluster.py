import numpy as np
from scipy.spatial.distance import cdist
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import sys,math
useridx = 0
movieidx = 0
# K=17
iteration = 10

def cal_distance(p1,p2):
    x1,y1,idx1 = p1
    x2,y2,idx2 = p2
    return Math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
 
def cal_distance3d(p1,p2):
    x1,y1,z1,idx1 = p1
    x2,y2,z2,idx2 = p2
    return ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**(1/3)
    
# 군집
def find_nearest_group_index(point,key_points):
    min_distance= sys.maxsize
    nearest_group = -1
    for idx,key_point in enumerate(key_points):
        
        distance = cal_distance(point,key_point)
        if distance<min_distance:
            min_distance=distance
            nearest_group=idx
    return nearest_group    

def find_nearest_group_index_3d(point,key_points):
    min_distance= sys.maxsize
    nearest_group = -1
    for idx,key_point in enumerate(key_points):
        
        distance = cal_distance3d(point,key_point)
        if distance<min_distance:
            min_distance=distance
            nearest_group=idx
    return nearest_group    

# 평균점이랑 가장가까운점 찾기
def find_nearest_point3d(mean_point,points,exceptional_points=[]):
    min_distance=sys.maxsize
    nearest_point = None
    for idx,point in enumerate(points):

        duplicate = False
        for exception_point in exceptional_points:
            if(np.array_equal(point,exception_point)):
                duplicate = True
        if duplicate:
            continue

        distance = cal_distance3d(point,mean_point)
        # if distance == 0:
        #     continue

        if distance < min_distance:
            min_distance=distance
            nearest_point = point
            if min_distance == 0:
                break
    return nearest_point 

def find_nearest_point(mean_point,points,exceptional_points=[]):
    min_distance=sys.maxsize
    nearest_point = None
    for idx,point in enumerate(points):

        duplicate = False
        for exception_point in exceptional_points:
            if(np.array_equal(point,exception_point)):
                duplicate = True
        if duplicate:
            continue

        distance = cal_distance(point,mean_point)
        # if distance == 0:
        #     continue

        if distance < min_distance:
            min_distance=distance
            nearest_point = point
            if min_distance == 0:
                break
    return nearest_point 

def kmeansUsers(data_set):
    K=5
    print(len(data_set))
    a = range(len(data_set))
    idx = random.sample(a,K)
    
    key_points =[]
    for i in idx:
        key_points.append(data_set[i,:])

    # cluster
    for i in range(iteration):
        groups = []
        for j in range(K):
            groups.append([])

        # 군집
        for data in data_set:
            group_index = find_nearest_group_index_3d(data,key_points)
            groups[group_index].append(data)
    
        # 평균좌표 구하기
        mean_points=[]
        for group in groups:
            if group != []:
                np_group = np.array(group)
                mean_points.append(np_group.mean(axis=0))
    
        # 중심점 새로 찾기
        key_points=[]
        for idx,mean_point in enumerate(mean_points):
            key_points.append(find_nearest_point3d(mean_point,groups[idx],key_points))
    
    global useridx
    labels = [0] * (useridx)
    
    for idx,group in enumerate(groups):
        for item in group:
            labels[item[3]]=idx

    labels = np.array(labels)
    print(labels)
    fig= plt.figure(figsize=(10,10))
    ax = Axes3D(fig,rect=[0,0,.95,1],elev=48,azim=134)
    ax.scatter(data_set[:,0],data_set[:,1],data_set[:,2],c=labels.astype(np.float),s=10)
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

def kmeans(data_set):
    K=17
    a= range(len(data_set))
    idx = random.sample(a,K)
    key_points =[]
    for i in idx:
        key_points.append(data_set[i,:])

    # cluster
    for i in range(iteration):
        groups = []
        for j in range(K):
            groups.append([])

        # 군집
        for data in data_set:
            group_index = find_nearest_group_index(data,key_points)
            groups[group_index].append(data)
        # 평균좌표 구하기
        mean_points=[]
        for group in groups:
            if group != []:
                np_group = np.array(group)
                mean_points.append(np_group.mean(axis=0))
        # print(mean_points)
        # print(groups)
        # 중심점 새로 찾기
        key_points=[]
        for idx,mean_point in enumerate(mean_points):
            key_points.append(find_nearest_point(mean_point,groups[idx],key_points))
    
    print(key_points)
    global movieidx
    labels = [0] * (movieidx)
    for idx,group in enumerate(groups):
        for item in group:
            labels[item[2]]=idx

    labels = np.array(labels)

    print(labels)
    fig = plt.figure(figsize=(10,10))
    plt.scatter(data_set[:,1],data_set[:,0],c=labels.astype(np.float),s=10)
    plt.ylabel('year')
    plt.xlabel('genre')
    plt.show()
    return labels

def get_users():
    user_data = open('./users.dat', 'r', encoding='ISO-8859-1')
    data_set = []
    global useridx
    for line in user_data.readlines():
        [userid, gender, age, occupation, zipcode] = line.split('::')
        userid = int(userid)

        age = int(age)
        occupation = int(occupation)
        if gender == 'M':
            gender=1
        else :
            gender=2
        data_set.append([
            age,
            gender,
            occupation*occupation,
            useridx,
        ])
        useridx+=1
    return np.array(data_set)


def get_movies():
    movie_data = open('./movies.dat','r',encoding='ISO-8859-1')
    data_set = []
    global movieidx
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
        data_set.append([year,genreid*31,movieidx])
        movieidx+=1
    return np.array(data_set)

def create_users(num_users):
    user_data = open('./users.dat', 'r', encoding='ISO-8859-1')
    request_data = {'profiles': []}
    occupation_map = {
        0: "other", 1: "academic/educator", 2: "artist", 3: "clerical/admin", 4: "college/grad student",
        5: "customer service", 6: "doctor/health care", 7: "executive/managerial", 8: "farmer", 9: "homemaker",
        10: "K-12 student", 11: "lawyer", 12: "programmer", 13: "retired", 14: "sales/marketing",
        15: "scientist", 16:  "self-employed", 17: "technician/engineer", 18: "tradesman/craftsman",
        19: "unemployed", 20: "writer"
    }

    for line in user_data.readlines():
        [userid, gender, age, occupation, zipcode] = line.split('::')
        username = 'user' + userid
        age = int(age)
        occupation = occupation_map[int(occupation)]

        request_data['profiles'].append({
            'username': username,
            'password': username,
            'age': age,
            'gender': gender,
            'occupation': occupation
        })

    response = requests.post(API_URL + 'auth/signup-many/', data=json.dumps(request_data), headers=headers)
    print(response.text)


if __name__ == '__main__':
    users_set  = get_users()
    kmeansUsers(users_set)
    # elbow(users_set)
    # movies_set = get_movies()
    # kmeans(movies_set)
    # elbow(movies_set)
