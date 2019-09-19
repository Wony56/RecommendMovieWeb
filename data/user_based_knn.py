from scipy.sparse import csr_matrix
import numpy as np
from numpy.linalg import norm

################현재 로그인된 useridx를 기반으로 실행################
###################해당 유저에게 추천해줄 movieid 5개 리스트 받아옴 ######################
def create_ratings():
    # user 마지막 idx
    user_data = open('./users.dat', 'r', encoding='ISO-8859-1')
    user_last = user_data.readlines()[-1]
    user_len= int(user_last.split('::')[0])

    #movie 마지막 idx
    movie_data = open('./movies.dat', 'r', encoding='ISO-8859-1')
    movie_last = movie_data.readlines()[-1]
    movie_len = int(movie_last.split('::')[0])
    # print(movie_len)
    
    # useridx x movieidx matrix 생성
    matrix = np.zeros((user_len,movie_len))
    # print(matrix)
    
    # rating_data
    rating_data = open('./ratings.dat', 'r', encoding='ISO-8859-1')
 
    for line in rating_data.readlines() :
        [user, movie, rating, timeStamp] = line.split('::')
        matrix[int(user)-1][int(movie)-1]=float(rating)
 
    # #####chocie = 현재 user
    choice = 1 -1
    # cos_sim(matrix[choice],user_len,matrix)
    sim_scores=[]
    for i in range(user_len):
        sim_scores.append([i+1,cos_sim(matrix[choice],matrix[i])])
    # print(sim_scores)
    
    sim_scores = sorted(sim_scores,key=lambda x: x[1],reverse=True)
    sim_scores = sim_scores[1:6]
    # print(sim_scores)
    # print(np.array(sim_scores))
    
    recommend = getRecommendation(sim_scores,matrix,choice)
    print(recommend)

def getRecommendation(sim_scores,matrix,choice):
    score = 0
    sim_total=0
    for i in sim_scores:
        sim_total +=i[1]

    score_list=dict()
    for movieid in range(len(matrix[choice])):
        if matrix[choice][movieid-1] ==0:
            for i in sim_scores:
                score+= matrix[i[0]-1][movieid-1]* i[1]
            score_list[movieid]=score/sim_total
            score = 0
    score_list = sorted(score_list.items(),key=lambda x:x[1],reverse=True)

    recommend=[]
    for i in range(5):
        recommend.append(score_list[i][0])
    
    return recommend

def cos_sim(A,B):
    return np.dot(A,B)/(norm(A)*norm(B))   
if __name__ == '__main__':
    create_ratings()