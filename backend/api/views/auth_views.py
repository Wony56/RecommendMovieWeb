import jwt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_jwt.utils import jwt_payload_handler
from api.models import create_profile, Profile
from api.serializers import ProfileSerializer, RatingSerializer
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.signals import user_logged_in
from backend.settings import SECRET_KEY

@api_view(['POST'])
def signup(request):
        if request.method == 'POST':
                profile = request.data.get('params',None)
                print(profile)
                name = profile.get('name',None)
                password = profile.get('password',None)
                age = profile.get('age', None)
                temp = int(age)
                if temp < 18:
                        age ="1"
                elif temp <=24:
                        age = "18"
                elif temp <=34:
                        age="25"
                elif temp <=44:
                        age="35"
                elif temp<=49:
                        age="45"
                elif temp<=55:
                        age="50"
                else:
                        age="56"

                occupation = profile.get('occupation', None)

                # if "academic/educator"== occupation :
                #         occupation = "1"
                # elif "artist" in occupation:
                #         occupation = "2"
                # elif "clerical/admin" == occupation:
                #         occupation = "3"
                # elif "college/grad student" in occupation:
                #         occupation = "4"
                # elif "customer service" in occupation:
                #         occupation = "5"
                # elif "doctor/health care" in occupation:
                #         occupation = "6"
                # elif "executive/managerial" == occupation:
                #         occupation = "7"
                # elif "farmer" in occupation:
                #         occupation = "8"
                # elif "homemaker" in occupation:
                #         occupation = "9"
                # elif "K-12 student" in occupation:
                #         occupation = "10"
                # elif "lawyer" in occupation:
                #         occupation = "11"
                # elif "programmer" in occupation:
                #         occupation = "12"
                # elif "retired" in occupation:
                #         occupation = "13"
                # elif "sales/marketing" in occupation:
                #         occupation = "14"
                # elif "scientist" in occupation:
                #         occupation = "15"
                # elif "self-emplyed" in occupation:
                #         occupation = "16"
                # elif "technician/engineer" in occupation:
                #         occupation = "17"
                # elif "tradesman/craftsman" in occupation:
                #         occupation = "18"
                # elif "unemployed" in occupation:
                #         occupation = "19"
                # elif "writer" in occupation:
                #         occupation = "20"
                # else:
                #         occupation="0"

                gender = profile.get('gender', None)

                create_profile(username=name, password=password, age=age,
                        occupation=occupation, gender=gender)

                return Response(status=status.HTTP_201_CREATED)

@api_view(['POST'])
def signup_many(request):

    if request.method == 'POST':
        profiles = request.data.get('profiles', None)
        for profile in profiles:
            username = profile.get('username', None)
            password = profile.get('password', None)
            age = profile.get('age', None)
            occupation = profile.get('occupation', None)
            gender = profile.get('gender', None)

            create_profile(username=username, password=password, age=age,
                           occupation=occupation, gender=gender)

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
        # print(data)
        return Response(data=data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([AllowAny,])
def authenticate_user(request):
        
        if request.method == "POST":
                try:
                        request_data = request.data['params']
                        username = request_data.get('username', None)
                        password = request_data.get('password', None)

                        user = User.objects.get(username=username)
                        if user and check_password(password, user.password):
                                try:
                                        payload = jwt_payload_handler(user)
                                        token = jwt.encode(payload, SECRET_KEY)
                                        user_details = {}
                                        user_details['name'] = "%s" % (user.username)
                                        user_details['token'] = token
                                        user_logged_in.send(sender=user.__class__, request=request, user=user)
                                        return Response(user_details, status=status.HTTP_200_OK)
                                except Exception as e:
                                        raise e
                        else:
                                res = {
                                        'error': 'can not authenticate with the given credentials or the account has be'
                                }
                                return Response(res, status=status.HTTP_403_FORBIDDEN)
                except KeyError:
                        res = {'error': 'please provide a username and a password'}
                        return Response(res)

@api_view(['POST'])
def on_auth_user(request):
        if request.method == 'POST':
                token = request.data['token']
                
                if token:
                        data = jwt.decode(token, SECRET_KEY)
                        
                        username = data.get('username')
                        user = User.objects.get(username=username)
                        profile = Profile.objects.get(user=user)

                        serializer = ProfileSerializer(profile)

                        return Response(data=serializer.data, status=status.HTTP_200_OK)
                else:
                        return Response(status=status.HTTP_200_OK)
