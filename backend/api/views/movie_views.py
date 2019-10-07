from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Movie,Rating
from django.contrib.auth.models import User
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
        for key in movies:
            

            id = movies[key].get('id', None)
            title = movies[key].get('title', None)
            genres = movies[key].get('genres', None)
            rusercount = movies[key].get('rusercount',None)
            rrating = movies[key].get('rrating',None)
            rgender = movies[key].get('rgender',None)
            academiceducatorcount = movies[key].get('academiceducatorcount',None)
            artistcount = movies[key].get('artistcount',None)
            clericaladmincount = movies[key].get('clericaladmincount',None)
            collegegradstudentcount = movies[key].get('collegegradstudentcount',None)
            customerservicecount = movies[key].get('customerservicecount',None)
            doctorhealthcarecount = movies[key].get('doctorhealthcarecount',None)
            executivemanagerialcount = movies[key].get('executivemanagerialcount',None)
            farmercount = movies[key].get('farmercount',None)
            homemakercount = movies[key].get('homemakercount',None)
            K12studentcount = movies[key].get('K12studentcount',None)
            lawyercount = movies[key].get('lawyercount',None)
            programmercount = movies[key].get('programmercount',None)
            retiredcount = movies[key].get('retiredcount',None)
            salesmarketingcount = movies[key].get('salesmarketingcount',None)
            scientistcount = movies[key].get('scientistcount',None)
            selfemployedcount = movies[key].get('selfemployedcount',None)
            technicianengineercount = movies[key].get('technicianengineercount',None)
            tradesmancraftsmancount = movies[key].get('tradesmancraftsmancount',None)
            unemployedcount = movies[key].get('unemployedcount',None)
            writercount = movies[key].get('writercount',None)
            age1count = movies[key].get('age1count',None)
            age18count = movies[key].get('age18count',None)
            age25count = movies[key].get('age25count',None)
            age35count = movies[key].get('age35count',None)
            age45count = movies[key].get('age45count',None)
            age50count = movies[key].get('age50count',None)
            age56count = movies[key].get('age56count',None)
            othercount = movies[key].get('othercount',None)
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
            movie=Movie(id=id, title=title, genres='|'.join(genres), rusercount = rusercount, rrating=rrating,
            rgender=rgender,othercount=othercount,academiceducatorcount=academiceducatorcount,artistcount=artistcount,
            clericaladmincount=clericaladmincount,collegegradstudentcount=collegegradstudentcount,
            customerservicecount=customerservicecount,doctorhealthcarecount=doctorhealthcarecount,
            executivemanagerialcount=executivemanagerialcount,farmercount=farmercount,homemakercount=homemakercount,
            K12studentcount=K12studentcount,lawyercount=lawyercount,programmercount=programmercount,
            retiredcount=retiredcount,salesmarketingcount=salesmarketingcount,scientistcount=scientistcount,
            selfemployedcount=selfemployedcount,technicianengineercount=technicianengineercount,tradesmancraftsmancount=tradesmancraftsmancount,
            unemployedcount=unemployedcount,writercount=writercount,age1count=age1count,
            age18count=age18count,age25count=age25count,age35count=age35count,age45count=age45count,
            age50count=age50count,age56count=age56count, tmdb_id=tmdb_id, overview=overview,year=year, poster_path=poster_path).save()
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

@api_view(['GET'])
def movie_by_user(request):
    if request.method == 'GET':
        username = request.GET.get('username', None)
            
        try:
            user = User.objects.get(username=username)
            watchList = Rating.objects.get(user=user)

            query = Q()
            for element in watchList:
                query = query | Q(id=element.movie.id)
            movies = movie.filter(query)

            serializer = MovieSerializer(movies, many=True)
            data = serializer.data

        except:
            return Response(status=status.HTTP_200_OK)

        return Response(data=data, status=status.HTTP_200_OK)

@api_view(['POST'])
def register_rating(request):
    if request.method == 'POST':
        movie_data = request.data.get('params', None)

        try:
            user_by_cookie = request.COOKIES.get('user')
            user_by_session = request.session.get('user', None)

            movie_id = movie_data.get('id', None)
            rating = movie_data.get('rating', None)

            if user_by_cookie == user_by_session:
                username = user_by_session
                movie = Movie.objects.get(id=movie_id)
                user = User.objects.get(username=username)
                profile = Profile.objects.get(user=user)
                
                Rating(user=user, movie=movie, rating=rating).save()

                profile.seemovie += "|" + movie.id + "{" + rating

                profile.save()

                movie.rrating = (movie.rrating * movie.rusercount + rating) / (movie.rusercount + 1)
                movie.rusercount += 1
                
                if profile.gender == 'M':
                    movie.rgender += 1
                else:
                    movie.rgender -= 1

                if profile.age == 1:
                    movie.age1count += 1
                elif profile.age == 18:
                    movie.age18count += 1
                elif profile.age == 25:
                    movie.age25count += 1
                elif profile.age == 35:
                    movie.age35count += 1
                elif profile.age == 45:
                    movie.age45count += 1
                elif profile.age == 50:
                    movie.age50count += 1
                elif profile.age == 56:
                    movie.age56count += 1

                if profile.occupation == "academic/educator":
                    movie.academiceducatorcount += 1
                elif profile.occupation == "artist":
                    movie.artistcount += 1
                elif profile.occupation == "clerical/admin":
                    movie.clericaladmincount += 1
                elif profile.occupation == "college/grad student":
                    movie.collegegradstudentcount += 1
                elif profile.occupation == "customer service":
                    movie.customerservicecount += 1
                elif profile.occupation == "doctor/health care":
                    movie.doctorhealthcarecount += 1
                elif profile.occupation == "executive/managerial":
                    movie.executivemanagerialcount += 1
                elif profile.occupation == "farmer":
                    movie.farmercount += 1
                elif profile.occupation == "homemaker":
                    movie.homemakercount += 1
                elif profile.occupation == "K-12 student":
                    movie.K12studentcount += 1
                elif profile.occupation == "lawyer":
                    movie.lawyercount += 1
                elif profile.occupation == "programmer":
                    movie.programmercount += 1
                elif profile.occupation == "retired":
                    movie.retiredcount += 1
                elif profile.occupation == "sales/marketing":
                    movie.salesmarketingcount += 1
                elif profile.occupation == "scientist":
                    movie.scientistcount += 1
                elif profile.occupation == "self-employed":
                    movie.selfemployedcount += 1
                elif profile.occupation == "technician/engineer":
                    movie.technicianengineercount += 1
                elif profile.occupation == "tradesman/craftsman":
                    movie.tradesmancraftsmancount += 1
                elif profile.occupation == "unemployed":
                    movie.unemployedcount += 1
                elif profile.occupation == "writer":
                    movie.writercount += 1
                else:
                    movie.othercount += 1
                
                movie.save()
                
        except:
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(stats = status.HTTP_201_CREATED)

                

