from api.models import UserCluster,Movie,movieCluster
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import MovieSerializer
from django.db.models import Q

# 미완
@api_view(['GET'])
def get_usergroup(request):
    if request.method=='GET':
        request_data = request.data.get('params',None)
        username = request_data.get('username', None)
        user = User.objects.get(username = username)
        usergroup = UserCluster.objects.get(user=user)
        groupnum = usergroup['group']

        usergroups = UserCluster.objects.all()
        usergroups = usergroups.filter(group = groupnum)
        if usergroups.count()>8:
            usergroups[:8]
        serializer = ProfileSerializer(usersgroups, many=True)
        data = serializer.data
        
        return Response(data=data, status=status.HTTP_200_OK)

# 미완
@api_view(['GET'])
def get_moviegroup(request):
    if request.method=='GET':
        movie_id = request.GET.get('movieId', None)
        movie = Movie.objects.get(id=movie_id)
        moviegroup = movieCluster.objects.get(movie=movie)
        groupnum = moviegroup.group

        moviegroups = movieCluster.objects.all()
        moviegroups = moviegroups.filter(group = groupnum)
        if moviegroups.count()>8:
            moviegroups=moviegroups[:8]
        
        movies = Movie.objects.all()

        query = Q()
        for moviegroup in moviegroups:
            query = query | Q(id=moviegroup.id)
        movies = movies.filter(query)

        serializer = MovieSerializer(movies, many=True)
        data = serializer.data
        
        return Response(data=data, status=status.HTTP_200_OK)

@api_view(['POST'])
def usercluster_many(request):
    if request.method == 'POST':
        userclusters = request.data.get('cluster_data',None)
        print(userclusters)
        idx = 1
        for usercluster in userclusters:
            group = usercluster.get('group', None)
            # print(group)
            user = User.objects.get(username='user'+str(idx))
            # print(user)
            UserCluster(user=user, group=group).save()
            idx+=1

        return Response(status=status.HTTP_201_CREATED)

        
@api_view(['POST'])
def moviecluster_many(request):
    if request.method == 'POST':
        movieclusters = request.data.get('cluster_data',None)
        # print(movieclusters)
        # movies = Movie.objects.all()
        # print(movies[0])
        # print(movies)
        for moviecluster in movieclusters:
            # print(moviecluster)
            movieId = moviecluster.get('movieId',None)
            # print(movieId)
            movie=Movie.objects.get(id=movieId)
            # print(movie)
            group = moviecluster.get('group', None)
            # print(group)
            movieCluster(movie=movie, group=group).save()
            # idx+=1

        return Response(status=status.HTTP_201_CREATED)
        