import requests
import json
from collections import ChainMap

API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}

def create_users():
    movie_data = open('./movies.dat', 'r', encoding='ISO-8859-1')
    user_data = open('./users.dat', 'r', encoding='ISO-8859-1')
    rating_data = open('./ratings.dat', 'r', encoding='ISO-8859-1')
    request_data = {'profiles': {}}
    mrequest_data = {'movies' : {}}
    occupation_map = {
        0: "other", 1: "academic/educator", 2: "artist", 3: "clerical/admin", 4: "college/grad student",
        5: "customer service", 6: "doctor/health care", 7: "executive/managerial", 8: "farmer", 9: "homemaker",
        10: "K-12 student", 11: "lawyer", 12: "programmer", 13: "retired", 14: "sales/marketing",
        15: "scientist", 16:  "self-employed", 17: "technician/engineer", 18: "tradesman/craftsman",
        19: "unemployed", 20: "writer"
    }
    i = 0

    for line in movie_data.readlines():
        [id, title, genres] = line.split('::')
        genres = genres[:-1].split('|')
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
      
        mrequest_data['movies'][id] ={
                'id': id,
                'title': title,
                'genres': genres,  
        }
        #print(request_data['movies'][id])
        print("##############################")
    rr_data = {}

    for line in rating_data.readlines() :
        i = i + 1
        [user, movie, rating, timeStamp] = line.split('::')
        timeStamp = int(timeStamp[:-1])
        rating = int(rating)
        # print(timeStamp)
        # cm = ChainMap(*profilesrequest_data['profiles'])
        # print(cm)
        # value = cm['username']
        # print(value)
        #print(profilesrequest_data[user]['age'])
        
        if user in rr_data:
            
            #print(rr_data[user]['seenmovie'])
            seenmovie = str(rr_data[user]['seenmovie'])+ "|" + str(mrequest_data['movies'][movie]['id'] + "{" + str(rating))
           
            #print(mrequest_data['movies'][movie]['title'])
            #print(seenmovie)
            #print("###########")
            #input()
            rr_data[user] = {
                'seenmovie' : seenmovie
                 

            }
        else :
            seenmovie = str(mrequest_data['movies'][movie]['id']+ "{" + str(rating))
           
            #print(mrequest_data['movies'][movie]['title'])
            #print(seenmovie)
            #print("###########")
            rr_data[user] = {
                'seenmovie' :seenmovie 
            }


    for line in user_data.readlines():
        [userid, gender, age, occupation, zipcode] = line.split('::')
        username = 'user' + userid
        age = int(age)
        occupation = occupation_map[int(occupation)]
        #print(rr_data[userid]['seenmovie'])
        seenm = "empty"
        if( 'seenmovie'  in rr_data[userid]):
            seenm = rr_data[userid]['seenmovie']

        request_data['profiles'][userid]={
            'username': username,
            'password': username,
            'age': age,
            'gender': gender,
            'is_subscribe': False,
            'occupation': occupation,
            'seenmovie' :seenm
        }
        
    response = requests.post(API_URL + 'auth/signup-many/', data=json.dumps(request_data), headers=headers)
    #print(response.text)


def create_movies():
    movie_data = open('./movies.dat', 'r', encoding='ISO-8859-1')
    rating_data = open('./ratings.dat', 'r', encoding='ISO-8859-1')
    request_data = {'movies' : {}}

   

    user_data = open('./users.dat', 'r', encoding='ISO-8859-1')
    profilesrequest_data = {}
    occupation_map = {
        0: "other", 1: "academic/educator", 2: "artist", 3: "clerical/admin", 4: "college/grad student",
        5: "customer service", 6: "doctor/health care", 7: "executive/managerial", 8: "farmer", 9: "homemaker",
        10: "K-12 student", 11: "lawyer", 12: "programmer", 13: "retired", 14: "sales/marketing",
        15: "scientist", 16:  "self-employed", 17: "technician/engineer", 18: "tradesman/craftsman",
        19: "unemployed", 20: "writer"
    }
    i = 0

    for line in user_data.readlines():
        [userid, gender, age, occupation, zipcode] = line.split('::')
        username = 'user' + userid
        age = int(age)
       # occupation = occupation_map[int(occupation)]
        profilesrequest_data[userid] = {
            'username': username,
            'userid' : userid,
            'password': username,
            'age': age,
            'gender': gender,
            'occupation': occupation
        }
    #print(profilesrequest_data[userid]['occupation'])

    rr_data = {}

    for line in rating_data.readlines() :
        i = i + 1
        [user, movie, rating, timeStamp] = line.split('::')
        timeStamp = int(timeStamp[:-1])
        rating = int(rating)
        # print(timeStamp)
        # cm = ChainMap(*profilesrequest_data['profiles'])
        # print(cm)
        # value = cm['username']
        # print(value)
        #print(profilesrequest_data[user]['age'])
        if movie in rr_data:
            rusercount = rr_data[movie]['rusercount']
            rrating = rr_data[movie]['rrating']
            rgender = rr_data[movie]['rgender']
            othercount = rr_data[movie]['othercount']
            academiceducatorcount = rr_data[movie]['academiceducatorcount']
            artistcount = rr_data[movie]['artistcount']
            clericaladmincount = rr_data[movie]['clericaladmincount']
            collegegradstudentcount = rr_data[movie]['collegegradstudentcount']
            customerservicecount = rr_data[movie]['customerservicecount']
            doctorhealthcarecount = rr_data[movie]['doctorhealthcarecount']
            executivemanagerialcount = rr_data[movie]['executivemanagerialcount']
            farmercount = rr_data[movie]['farmercount']
            homemakercount = rr_data[movie]['homemakercount']
            K12studentcount = rr_data[movie]['K12studentcount']
            lawyercount = rr_data[movie]['lawyercount']
            programmercount = rr_data[movie]['programmercount']
            retiredcount = rr_data[movie]['retiredcount']
            salesmarketingcount = rr_data[movie]['salesmarketingcount']
            scientistcount = rr_data[movie]['scientistcount']
            selfemployedcount = rr_data[movie]['selfemployedcount']
            technicianengineercount = rr_data[movie]['technicianengineercount']
            tradesmancraftsmancount = rr_data[movie]['tradesmancraftsmancount']
            unemployedcount = rr_data[movie]['unemployedcount']
            writercount = rr_data[movie]['writercount']
            age1count = rr_data[movie]['age1count']
            age18count = rr_data[movie]['age18count']
            age25count = rr_data[movie]['age25count']
            age35count = rr_data[movie]['age35count']
            age45count = rr_data[movie]['age45count']
            age50count = rr_data[movie]['age50count']
            age56count = rr_data[movie]['age56count']
            
            if(profilesrequest_data[user]['gender'] == 'F') :
                rgender -=1
            else :
                rgender +=1

            if(profilesrequest_data[user]['occupation'] == '0'):
                othercount +=1
            elif(profilesrequest_data[user]['occupation'] == '1'):
                academiceducatorcount +=1
            elif(profilesrequest_data[user]['occupation'] == '2'):
                artistcount +=1
            elif(profilesrequest_data[user]['occupation'] == '3'):
                clericaladmincount +=1
            elif(profilesrequest_data[user]['occupation'] == '4'):
                collegegradstudentcount +=1
            elif(profilesrequest_data[user]['occupation'] == '5'):
                customerservicecount +=1
            elif(profilesrequest_data[user]['occupation'] == '6'):
                doctorhealthcarecount +=1
            elif(profilesrequest_data[user]['occupation'] == '7'):
                executivemanagerialcount +=1
            elif(profilesrequest_data[user]['occupation'] == '8'):
                farmercount +=1
            elif(profilesrequest_data[user]['occupation'] == '9'):
                homemakercount +=1
            elif(profilesrequest_data[user]['occupation'] == '10'):
                K12studentcount +=1
            elif(profilesrequest_data[user]['occupation'] == '11'):
                lawyercount +=1
            elif(profilesrequest_data[user]['occupation'] == '12'):
                programmercount +=1
            elif(profilesrequest_data[user]['occupation'] == '13'):
                retiredcount +=1
            elif(profilesrequest_data[user]['occupation'] == '14'):
                salesmarketingcount +=1
            elif(profilesrequest_data[user]['occupation'] == '15'):
                scientistcount +=1
            elif(profilesrequest_data[user]['occupation'] == '16'):
                selfemployedcount +=1
            elif(profilesrequest_data[user]['occupation'] == '17'):
                technicianengineercount +=1
            elif(profilesrequest_data[user]['occupation'] == '18'):
                tradesmancraftsmancount +=1
            elif(profilesrequest_data[user]['occupation'] == '19'):
                unemployedcount +=1
            elif(profilesrequest_data[user]['occupation'] == '20'):
                writercount +=1


            if(profilesrequest_data[user]['age'] == 1):
                age1count +=1
            elif(profilesrequest_data[user]['age'] == 18):
                age18count +=1
            elif(profilesrequest_data[user]['age'] == 25):
                age25count +=1
            elif(profilesrequest_data[user]['age'] == 35):
                age35count +=1
            elif(profilesrequest_data[user]['age'] == 45):
                age45count +=1
            elif(profilesrequest_data[user]['age'] == 50):
                age50count +=1
            elif(profilesrequest_data[user]['age'] == 56):
                age56count +=1

            rr_data[movie] = {
                'rusercount' : rusercount + 1,
                'rrating' : ((rrating*(rusercount)) + rating)/(rusercount+1),
                'rgender' : rgender,
                'othercount' : othercount,
                'academiceducatorcount' : academiceducatorcount,
                'artistcount' : artistcount,
                'clericaladmincount' : clericaladmincount,
                'collegegradstudentcount' : collegegradstudentcount,
                'customerservicecount' : customerservicecount,
                'doctorhealthcarecount' : doctorhealthcarecount,
                'executivemanagerialcount' : executivemanagerialcount,
                'farmercount' : farmercount,
                'homemakercount' : homemakercount,
                'K12studentcount' : K12studentcount,
                'lawyercount' : lawyercount,
                'programmercount' : programmercount,
                'retiredcount' : retiredcount,
                'salesmarketingcount' : salesmarketingcount,
                'scientistcount' : scientistcount,
                'selfemployedcount' : selfemployedcount,
                'technicianengineercount' : technicianengineercount,
                'tradesmancraftsmancount' : tradesmancraftsmancount,
                'unemployedcount' : unemployedcount,
                'writercount' : writercount,
                'age1count' : age1count,
                'age18count' : age18count,
                'age25count' : age25count,
                'age35count' : age35count,
                'age45count' : age45count,
                'age50count' : age50count,
                'age56count' : age56count,


            }
        else:
            rusercount = 0
            rrating = 0
            rgender = 0
            othercount = 0
            academiceducatorcount = 0
            artistcount = 0
            clericaladmincount = 0
            collegegradstudentcount = 0
            customerservicecount = 0
            doctorhealthcarecount = 0
            executivemanagerialcount = 0
            farmercount = 0
            homemakercount = 0
            K12studentcount = 0
            lawyercount = 0
            programmercount = 0
            retiredcount = 0
            salesmarketingcount =0
            scientistcount = 0
            selfemployedcount = 0
            technicianengineercount = 0
            tradesmancraftsmancount = 0
            unemployedcount = 0
            writercount = 0
            age1count = 0
            age18count = 0
            age25count = 0
            age35count = 0
            age45count = 0
            age50count = 0
            age56count = 0
            
            if(profilesrequest_data[user]['gender'] == 'F') :
                rgender -=1
            else :
                rgender +=1

            if(profilesrequest_data[user]['occupation'] == '0'):
                othercount +=1
            elif(profilesrequest_data[user]['occupation'] == '1'):
                academiceducatorcount +=1
            elif(profilesrequest_data[user]['occupation'] == '2'):
                artistcount +=1
            elif(profilesrequest_data[user]['occupation'] == '3'):
                clericaladmincount +=1
            elif(profilesrequest_data[user]['occupation'] == '4'):
                collegegradstudentcount +=1
            elif(profilesrequest_data[user]['occupation'] == '5'):
                customerservicecount +=1
            elif(profilesrequest_data[user]['occupation'] == '6'):
                doctorhealthcarecount +=1
            elif(profilesrequest_data[user]['occupation'] == '7'):
                executivemanagerialcount +=1
            elif(profilesrequest_data[user]['occupation'] == '8'):
                farmercount +=1
            elif(profilesrequest_data[user]['occupation'] == '9'):
                homemakercount +=1
            elif(profilesrequest_data[user]['occupation'] == '10'):
                K12studentcount +=1
            elif(profilesrequest_data[user]['occupation'] == '11'):
                lawyercount +=1
            elif(profilesrequest_data[user]['occupation'] == '12'):
                programmercount +=1
            elif(profilesrequest_data[user]['occupation'] == '13'):
                retiredcount +=1
            elif(profilesrequest_data[user]['occupation'] == '14'):
                salesmarketingcount +=1
            elif(profilesrequest_data[user]['occupation'] == '15'):
                scientistcount +=1
            elif(profilesrequest_data[user]['occupation'] == '16'):
                selfemployedcount +=1
            elif(profilesrequest_data[user]['occupation'] == '17'):
                technicianengineercount +=1
            elif(profilesrequest_data[user]['occupation'] == '18'):
                tradesmancraftsmancount +=1
            elif(profilesrequest_data[user]['occupation'] == '19'):
                unemployedcount +=1
            elif(profilesrequest_data[user]['occupation'] == '20'):
                writercount +=1


            if(profilesrequest_data[user]['age'] == 1):
                age1count +=1
            elif(profilesrequest_data[user]['age'] == 18):
                age18count +=1
            elif(profilesrequest_data[user]['age'] == 25):
                age25count +=1
            elif(profilesrequest_data[user]['age'] == 35):
                age35count +=1
            elif(profilesrequest_data[user]['age'] == 45):
                age45count +=1
            elif(profilesrequest_data[user]['age'] == 50):
                age50count +=1
            elif(profilesrequest_data[user]['age'] == 56):
                age56count +=1

            rr_data[movie] = {
                'rusercount' : rusercount + 1,
                'rrating' : ((rrating*(rusercount-1)))/(rusercount+1),
                'rgender' : rgender,
                'othercount' : othercount,
                'academiceducatorcount' : academiceducatorcount,
                'artistcount' : artistcount,
                'clericaladmincount' : clericaladmincount,
                'collegegradstudentcount' : collegegradstudentcount,
                'customerservicecount' : customerservicecount,
                'doctorhealthcarecount' : doctorhealthcarecount,
                'executivemanagerialcount' : executivemanagerialcount,
                'farmercount' : farmercount,
                'homemakercount' : homemakercount,
                'K12studentcount' : K12studentcount,
                'lawyercount' : lawyercount,
                'programmercount' : programmercount,
                'retiredcount' : retiredcount,
                'salesmarketingcount' : salesmarketingcount,
                'scientistcount' : scientistcount,
                'selfemployedcount' : selfemployedcount,
                'technicianengineercount' : technicianengineercount,
                'tradesmancraftsmancount' : tradesmancraftsmancount,
                'unemployedcount' : unemployedcount,
                'writercount' : writercount,
                'age1count' : age1count,
                'age18count' : age18count,
                'age25count' : age25count,
                'age35count' : age35count,
                'age45count' : age45count,
                'age50count' : age50count,
                'age56count' : age56count,

            }
        
        
      
        



    for line in movie_data.readlines():
        [id, title, genres] = line.split('::')
        genres = genres[:-1].split('|')
        print(id)
        print(rusercount)
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        if id in rr_data:
             request_data['movies'][id] ={
                'id': id,
                'title': title,
                'genres': genres,
                'rusercount' : rr_data[id]['rusercount'],
                'rrating' : rr_data[id]['rrating'],
                'rgender' : rr_data[id]['rgender'],
                'othercount' : rr_data[id]['othercount'],
                'academiceducatorcount' : rr_data[id]['academiceducatorcount'],
                'artistcount' : rr_data[id]['artistcount'],
                'clericaladmincount' : rr_data[id]['clericaladmincount'],
                'collegegradstudentcount' : rr_data[id]['collegegradstudentcount'],
                'customerservicecount' : rr_data[id]['customerservicecount'],
                'doctorhealthcarecount' : rr_data[id]['doctorhealthcarecount'],
                'executivemanagerialcount' : rr_data[id]['executivemanagerialcount'],
                'farmercount' : rr_data[id]['farmercount'],
                'homemakercount' : rr_data[id]['homemakercount'],
                'K12studentcount' : rr_data[id]['K12studentcount'],
                'lawyercount' : rr_data[id]['lawyercount'],
                'programmercount' : rr_data[id]['programmercount'],
                'retiredcount' : rr_data[id]['retiredcount'],
                'salesmarketingcount' : rr_data[id]['salesmarketingcount'],
                'scientistcount' : rr_data[id]['scientistcount'],
                'selfemployedcount' : rr_data[id]['selfemployedcount'],
                'technicianengineercount' : rr_data[id]['technicianengineercount'],
                'tradesmancraftsmancount' : rr_data[id]['tradesmancraftsmancount'],
                'unemployedcount' : rr_data[id]['unemployedcount'],
                'writercount' : rr_data[id]['writercount'],
                'age1count' : rr_data[id]['age1count'],
                'age18count' : rr_data[id]['age18count'],
                'age25count' : rr_data[id]['age25count'],
                'age35count' : rr_data[id]['age35count'],
                'age45count' : rr_data[id]['age45count'],
                'age50count' : rr_data[id]['age50count'],
                'age56count' : rr_data[id]['age56count'],
             }
        else:
             request_data['movies'][id] ={
                'id': id,
                'title': title,
                'genres': genres,
                'rusercount' : 0,
                'rrating' : 0,
                'rgender' : 0,
                'othercount' : 0,
                'academiceducatorcount' : 0,
                'artistcount' : 0,
                'clericaladmincount' :0,
                'collegegradstudentcount' : 0,
                'customerservicecount' : 0,
                'doctorhealthcarecount' : 0,
                'executivemanagerialcount' : 0,
                'farmercount' : 0,
                'homemakercount' : 0,
                'K12studentcount' : 0,
                'lawyercount' : 0,
                'programmercount' :0,
                'retiredcount' : 0,
                'salesmarketingcount' : 0,
                'scientistcount' : 0,
                'selfemployedcount' : 0,
                'technicianengineercount' : 0,
                'tradesmancraftsmancount' : 0,
                'unemployedcount' : 0,
                'writercount' : 0,
                'age1count' : 0,
                'age18count' : 0,
                'age25count' : 0,
                'age35count' : 0,
                'age45count' : 0,
                'age50count' : 0,
                'age56count' : 0,

             }
        #print(request_data['movies'][id])
        print("##############################")

    response = requests.post(API_URL + 'movies/', data=json.dumps(request_data), headers=headers)
    #print(response.text)


def create_ratings():
    rating_data = open('./ratings.dat', 'r', encoding='ISO-8859-1')
    request_data = {'ratings' : []}

    for line in rating_data.readlines() :
        [user, movie, rating, timeStamp] = line.split('::')
        timeStamp = int(timeStamp[:-1])
        # print(timeStamp)
        # print(datetime.datetime.fromtimestamp(timeStamp))
        # timeStamp = str(datetime.datetime.fromtimestamp(timeStamp))
        #print(timeStamp)
        request_data['ratings'].append({
            'user' : user,
            'movie' : movie,
            'rating' : rating,
            'timeStamp' : timeStamp
        })

    # print(request_data)
    response = requests.post(API_URL + 'ratings/', data=json.dumps(request_data), headers=headers)
    #print(response.text)

if __name__ == '__main__':
    num_users = 15
    #create_movies()
    create_users()
    #create_ratings()