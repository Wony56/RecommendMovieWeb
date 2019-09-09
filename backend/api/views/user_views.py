from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Profile
from api.serializers import ProfileSerializer
from django.contrib.auth.models import User
from django.db.models import Q

@api_view(['POST'])
def edit_profile(request):
    
    if request.method == "POST":
        try:
                edited_user = request.data.get('params', None)
                if edited_user:
                        username = edited_user.get('username', None)
                        user = User.objects.get(username=username)
                        occupation = edited_user.get('occupation', None)
                        gender = edited_user.get('gender', None)
                        age = edited_user.get('age', None)

                        profile = Profile.objects.get(user=user)

                        profile.occupation = occupation
                        profile.gender = gender
                        profile.age = age
                        profile.save()

                        return Response(status=status.HTTP_200_OK)
                else:
                        raise ValueError
        except:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def all_profiles(request):
    
    if request.method == 'GET' :
        try:
                user = User.objects.get(username="admin")
                profiles = Profile.objects.exclude(user=user)

                serializer = ProfileSerializer(profiles, many=True)
                data = serializer.data
                return Response(data=data, status=status.HTTP_200_OK)
        except:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def delete_user(request):

        if request.method == 'DELETE':
                try:
                        username = request.GET.get('username', None)
                        selected_users = request.GET.getlist('selected[]', None)

                        user = User.objects.all()

                        if username:
                                user = user.get(username=username)
                        if selected_users:
                                query = Q();
                                for selected_user in selected_users:
                                        query = query | Q(username=selected_user)
                                user = User.objects.filter(query)

                        
                        user.delete()
                        return Response(status=status.HTTP_200_OK)
                except:
                        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

