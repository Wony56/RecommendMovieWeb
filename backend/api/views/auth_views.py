from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import create_profile, Profile
from api.serializers import ProfileSerializer, RatingSerializer
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib import auth
from datetime import datetime, timedelta

@api_view(['POST'])
def signup(request):

    if request.method == 'POST':
        profile = request.data.get('params', None)

        print(profile)
        
        username = profile.get('username', None)
        password = profile.get('password', None)
        age = profile.get('age', None)
        occupation = profile.get('occupation', None)
        gender = profile.get('gender', None)
        is_subscribe = profile.get('is_subscribe', None)
        subscribe_expire = datetime.now()
        seenmovie=profile.get('seenmovie',None)
        if(seenmovie == None):
            seenmovie = "None"
        print(seenmovie)
        print("$$$$$$$$$$$$$$$$$$$$$$$")
        if is_subscribe:
            if is_subscribe == True:
                subscribe_expire += timedelta(days=3)
        else:
            is_subscribe = False
                
        if age < 18:
            age ="1"
        elif age <=24:
            age = "18"
        elif age <=34:
            age="25"
        elif age <=44:
            age="35"
        elif age <= 49:
            age="45"
        elif age <= 55:
            age="50"
        else:
            age="56"

        create_profile(username=username, password=password, age=age,
                        occupation=occupation, gender=gender, is_subscribe=is_subscribe, subscribe_expire=subscribe_expire,seenmovie=seenmovie)
            
        return Response(status=status.HTTP_201_CREATED)

@api_view(['POST'])
def signup_many(request):

    if request.method == 'POST':
        
        profiles = request.data.get('profiles', None)
        
        for key in profiles:
            print(key)
            username = profiles[key].get('username', None)
            print(username)
            print(profiles[key].get('seenmovie',None))
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^")
            password = profiles[key].get('password', None)
            age = profiles[key].get('age', None)
            occupation = profiles[key].get('occupation', None)
            gender = profiles[key].get('gender', None)
            is_subscribe = profiles[key].get('is_subscribe', None)
            subscribe_expire = datetime.now()
            seenmovie = profiles[key].get('seenmovie',None)
            print(seenmovie)
            print("GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG")
            if is_subscribe:
                if is_subscribe == True:
                    subscribe_expire += timedelta(days=3)
                    
            if age < 18:
                age ="1"
            elif age <=24:
                age = "18"
            elif age <=34:
                age="25"
            elif age <=44:
                age="35"
            elif age <= 49:
                age="45"
            elif age <= 55:
                age="50"
            else:
                age="56"

            create_profile(username=username, password=password, age=age,
                            occupation=occupation, gender=gender, is_subscribe=is_subscribe, subscribe_expire=subscribe_expire,seenmovie=seenmovie)
                
        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_profile(request) :

    if request.method == 'GET' :
        id = request.GET.get('id',None)
        user = User.objects.get(username='user'+id)
        profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(profile)
        data = serializer.data
        ratings = user.rating_set.all()
        serializer = RatingSerializer(ratings,many=True)
        data['ratings'] = serializer.data
        
        return Response(data=data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login(request):

    if request.method == 'POST':
        request_data = request.data.get('params', None)

        if request_data:
            try:
                username = request_data.get('username', None)
                password = request_data.get('password', None)

                user = User.objects.get(username=username)
            except User.DoesNotExist:
                err = "아이디 또는 비밀번호가 틀렸습니다."
                return Response(data=err, status=status.HTTP_401_UNAUTHORIZED)
            
            if not check_password(password, user.password):
                err = "아이디 또는 비밀번호가 틀렸습니다."
                return Response(data=err, status=status.HTTP_401_UNAUTHORIZED)
            else:
                request.session['user'] = user.username
                profile = Profile.objects.get(user=user)
                serializer = ProfileSerializer(profile)

                return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def on_auth_state(request):
    if request.method == 'GET':
        user_by_cookie = request.COOKIES.get('user')
        user_by_session = request.session.get('user', None)

        if user_by_cookie and user_by_session:
            if user_by_cookie == user_by_session:
                user = User.objects.get(username=user_by_session)
                profile = Profile.objects.get(user=user)
                serializer = ProfileSerializer(profile)

                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def logout(request):
    if request.method == 'GET':
        user_by_cookie = request.COOKIES.get('user')
        user_by_session = request.session.get('user', None)

        if user_by_cookie and user_by_session:
            if user_by_cookie == user_by_session:
                del request.session['user']
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def user_duplicate(request):
    if request.method == 'POST':
        request_data = request.data.get('params', None)
        print(request_data)

        try:
            username = request_data.get('username', None)

            if username:
                user = User.objects.get(username=username)

                if user:
                    err = "이미 존재하는 USERNAME입니다."
                    return Response(data=err, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_500_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def update_subscribe(request):
    if request.method == 'GET':
        try:
            user_by_cookie = request.COOKIES.get('user')
            user_by_session = request.session.get('user', None)

            if user_by_session and user_by_cookie:
                if user_by_session == user_by_cookie:
                    user = User.objects.get(username=user_by_session)
                    profile = Profile.objects.get(user=user)
                    profile.is_subscribe = True;
                    profile.subscribe_expire = datetime.now() + timedelta(days=3)
                    profile.save()
        except:
            return Response(status=status.HTTP_500_BAD_REQUEST)
        
        return Response(status=status.HTTP_200_OK)