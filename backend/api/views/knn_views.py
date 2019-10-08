from api.models import KnnAgeView,Movie,Rating,Profile
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import MovieSerializer
from django.contrib.auth.models import User

@api_view(['GET'])
def get_knn_age_view(request):
    if request.method =='GET':
        # age = request.GET.get('age', None)
        userid = request.GET.get('username',None)
        # print(age)
        print(userid)
        # age = params.data.get('age',None)
        user = User.objects.get(username = userid)
        profile = Profile.objects.get(user=user)
        age = profile.age

        obj = KnnAgeView.objects.get(Age=int(age))
        genre = obj.Max_genre

        # 이 장르를 가진 가장 높은 평점을 가진 영화 가져오기
        movies = Movie.objects.all().filter(genres__icontains=genre)

        user = User.objects.get(username = userid)
        isSeen = Rating.objects.filter(user = user).values_list('movie',flat=True)
        print(isSeen)
        movies = movies.exclude(id__in=isSeen)
        
        movies = movies.order_by('-rrating')
        # print(movies.count())
        if movies.count()>=8:
            movies = movies[:8]
        # movies=movies[:8]
        print(movies)
        serializer = MovieSerializer(movies, many=True)
        data = serializer.data
        
        return Response(data=data, status=status.HTTP_200_OK)
        # return Response(status = status.HTTP_200_OK)

@api_view(['GET'])
def update_knn_age_view(request):
    if request.method == 'GET' :
        # params = request.GET.get('params',None)
        age = request.GET.get('age',None)
        movieid = request.GET.get('movieid',None)
        age = int(age)
        movieid = int(movieid)
        print(age)
        print(movieid)
        try :

            obj=KnnAgeView.objects.get(Age=age)
            movie = Movie.objects.get(id=movieid)
            print(movie.genres)
            genres = movie.genres.split('|')
            print(genres)
  
            for genre in genres:
                if genre == 'Action':
                    obj.Action = obj.Action + 1
                elif genre == 'Adventure':
                    obj.Adventure = obj.Adventure + 1
                elif genre == 'Animation':
                    obj.Animation = obj.Animation + 1
                elif genre == "Children's":
                    obj.Childrens = obj.Childrens + 1
                elif genre == 'Comedy':
                    obj.Comedy = obj.Comedy + 1
                elif genre == 'Crime':
                    obj.Crime = obj.Crime + 1
                elif genre == 'Documentary':
                    obj.Documentary = obj.Documentary +1 
                elif genre == 'Drama':
                    obj.Drama = obj.Drama + 1
                elif genre == 'Fantasy':
                    obj.Fantasy = obj.Fantasy + 1
                elif genre == 'Film-Noir':
                    obj.FilmNoir = obj.FilmNoir +1
                elif genre == 'Horror':
                    obj.Horror = obj.Horror + 1
                elif genre == 'Musical':
                    obj.Musical = obj.Musical + 1
                elif genre == 'Mystery':
                    obj.Mystery = obj.Mystery + 1
                elif genre == 'Romance':
                    obj.Romance = obj.Romance + 1
                elif genre == 'Sci-Fi':
                    obj.SciFi = obj.SciFi + 1
                elif genre == 'Thriller':
                    obj.Thriller = obj.Thriller + 1
                elif genre =='War':
                    obj.War = obj.War + 1
                elif genre =='Western':
                    obj.Western = obj.Western + 1
            
            max_key = ''
            max_val = 0
            # print(obj.__dict__.items())
            for key, value in obj.__dict__.items():
                if key is not '_state' and key is not 'Age' and key is not 'Max_genre':
                    if value > max_val:
                        max_key = key
                        max_val = value
            # print(max_key)
            obj.Max_genre = max_key
            print(obj.__dict__)
            # movie.save()
            # obj.save()
            # obj.age의 장르가 max면 maxgenre 변경
           
            obj.save()

            return Response(status=status.HTTP_200_OK)
        except :
            return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def reg_knn_age_view(request):
    if request.method == 'GET':
        knn_age_views = request.data.get('knn_data',None)
        print(knn_age_views)
      
        for knn_age_view in knn_age_views:
            # print(knn_age_view)
            Age = knn_age_view.get('age', None)
            Action = knn_age_view.get('Action',None)
            Adventure = knn_age_view.get('Adventure',None)
            Animation = knn_age_view.get('Animation',None)
            Childrens = knn_age_view.get("Children's",None)
            Comedy = knn_age_view.get("Comedy",None)
            Crime = knn_age_view.get("Crime",None)
            Documentary = knn_age_view.get("Documentary",None)
            Drama = knn_age_view.get("Drama",None)
            Fantasy = knn_age_view.get("Fantasy",None)
            FilmNoir = knn_age_view.get("Film-Noir",None)
            Horror = knn_age_view.get("Horror",None)
            Musical = knn_age_view.get("Musical",None)
            Mystery = knn_age_view.get("Mystery",None)
            Romance = knn_age_view.get("Romance",None)
            SciFi = knn_age_view.get("Sci-Fi",None)
            Thriller = knn_age_view.get("Thriller",None)
            War = knn_age_view.get("War",None)
            Western = knn_age_view.get("Western",None)
            max_genre =knn_age_view.get("max_genre",None)
            print(Age)
            print(max_genre)
            KnnAgeView(
                Age=Age, 
                Action = Action,
                Adventure = Adventure,
                Animation = Animation,
                Childrens = Childrens,
                Comedy = Comedy,  
                Crime = Crime,
                Documentary = Documentary, 
                Drama = Drama,
                Fantasy = Fantasy,
                FilmNoir = FilmNoir,
                Horror = Horror,
                Musical=Musical,
                Mystery=Mystery,
                Romance=Romance,
                SciFi =SciFi,
                Thriller = Thriller,
                War =War,
                Western =Western,
                Max_genre= max_genre
            ).save()
        #     # # idx+=1

        return Response(status=status.HTTP_201_CREATED)