from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Movie,Rating
from api.serializers import MovieSerializer
from rest_framework.response import Response
from django.db.models import Q
from django.db.models import Count, Case, When, F
import requests

@api_view(['GET'])
def update_view_cnt(request) :
    if request.method == 'GET' :
        id = request.GET.get('id',None)
        try :
            movie = Movie.objects.get(id=id)
            movie.view_cnt = movie.view_cnt + 1
            movie.save()
            return Response(status=status.HTTP_200_OK)
        except :
            return Response(status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'DELETE'])
def movies(request):

    if request.method == 'GET':
        id = request.GET.get('id', request.GET.get('movie_id', None))
        title = request.GET.get('title', None)
        genre = request.GET.get('genre', None)
        occupation = request.GET.get('occupation', None)
        gender = request.GET.get('gender' , None)
        age = request.GET.get('age' , None)
        year = request.GET.get('year',None)
        overview =request.GET.get('overview',None)
        poster_path = request.GET.get('poster_path',None)
        movies = Movie.objects.all()
        
        if id:
            movies = movies.filter(pk=id)
        if title:
            movies = movies.filter(title__icontains=title)
        if genre:
            genres = genre.split(',')
            print(genres)
            for i in range(len(genres)-1):
                movies = movies.filter(genres__icontains=genres[i])
       

        if occupation :
            movies = movies.filter(rating__user__profile__occupation=occupation).distinct().annotate(count = Count(
                Case(
                        When(
                            rating__user__profile__occupation=occupation,
                            then=1
                        )
                    ))).order_by('-count')
        # if gender :
        #     movies = movies.annotate(
        #         mcount= Count(
        #             Case(
        #                 When (             
        #                     rating__user__profile__gender = 'M',
        #                     then=1
        #                 )
        #             )
        #         ),
        #         fcount = Count(
        #             Case(
        #                 When (
        #                     rating__user__profile__gender = 'F',
        #                     then=1
        #                 )
        #             )
        #         ),
        #         diff = F('mcount')-F('fcount')
        #     )
            
        #     if gender == 'M' :
        #         movies = movies.filter(diff__gt = 0).order_by('-diff')
        #     if gender == 'F' :
        #         movies = movies.filter(diff__lt = 0).order_by('diff')
        # if age :
        #     movies = movies.annotate(
        #         ageCount = Count(
        #             Case(
        #                 When(
        #                     rating__user__profile__age = age,
        #                     then = 1
        #                 )
        #             )
        #         )
        #     ).filter(ageCount__gt = 0).order_by('-ageCount')
            # movies = movies
        serializer = MovieSerializer(movies, many=True)
        data = serializer.data
            
        return Response(data=data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        id = request.GET.get('id', None)
        selected_movies = request.GET.getlist('selected[]', None)

        movie = Movie.objects.all()

        if id:
            movie = movie.get(id=id)
        if selected_movies:
            query = Q()
            for selected_movie in selected_movies:
                query = query | Q(id=selected_movie)
            movie = movie.filter(query)

        movie.delete()
        return Response(status=status.HTTP_200_OK)

    if request.method == 'POST':
        movies = request.data.get('movies', None)
        for movie in movies:
            id = movie.get('id', None)
            title = movie.get('title', None)
            genres = movie.get('genres', None)
            if not (id and title and genres):
                continue
            if Movie.objects.filter(id=id).count() > 0 or Movie.objects.filter(title=title).count() > 0:
                continue
            n = len(title)
            year = title[n-5:n-1]
            # 괄호 검색
            title = title[:-6]
            if '(' in title :
                title = title.split('(')[0]
            if '.' in title :
                title = title.split('.')[0]
            # , 검색
            if ',' in title :
                title = title.split(',')[0]
            tmurl = "https://api.themoviedb.org/3/search/movie?api_key=8f03cc345840b05e82681223f1ff0d74&language=en-US&query={}&page=1&year={}".format(title,year)
            results = requests.get(tmurl).json()
            # 만약 total_result 가 0이라면 제목으로만 다시검색
            if results['total_results'] == 0 :
                tmurl = "https://api.themoviedb.org/3/search/movie?api_key=8f03cc345840b05e82681223f1ff0d74&language=en-US&query={}&page=1".format(title)
                results = requests.get(tmurl).json()
            # 그래도 없다면 패스
            if results['total_results'] == 0 :
                movie=Movie(id=id, title=title, genres='|'.join(genres), tmdb_id=1, overview='',year=year, poster_path='').save()
                continue
            # results 에 결과 저장
            results = results['results'][0]
            overview = results['overview']
            # https://developers.themoviedb.org/3/search/search-movies
            # https://developers.themoviedb.org/3/movies/get-movie-details
            # api_key=8f03cc345840b05e82681223f1ff0d74
            tmdb_id = results['id']
            if results['poster_path'] == None :
                results['poster_path'] = ""
            poster_path = 'https://image.tmdb.org/t/p/original'+ results['poster_path']
            # example
            # model -> Movie -> item 필드추가하면됨
            # item = results['item']
            # movie=Movie(id=id, item = item)
            movie=Movie(id=id, title=title, genres='|'.join(genres), tmdb_id=tmdb_id, overview=overview,year=year, poster_path=poster_path).save()
        return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def edit_movie(request):
    
    if request.method == 'POST':
        edited_movie = request.data.get('params', None)

        try:
            if edited_movie:
                id = edited_movie.get('id', None)
                title = edited_movie.get('title', None)
                genres = edited_movie.get('genres', None)

                movie = Movie.objects.get(id=id)
                movie.title = title
                movie.genres = genres
                movie.save()

                return Response(status=status.HTTP_200_OK)
            else:
                raise ValueError
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
