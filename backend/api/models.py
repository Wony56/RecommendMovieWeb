from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, default='M')
    age = models.IntegerField(default=25)
    occupation = models.CharField(max_length=200)
    is_subscribe = models.BooleanField(default=False)
    subscribe_expire = models.DateTimeField(default=datetime.now())

#  wrapper for create user Profile
def create_profile(**kwargs):

    user = User.objects.create_user(
        username=kwargs['username'],
        password=kwargs['password'],
        is_active=True,
    )

    profile = Profile.objects.create(
        user=user,
        gender=kwargs['gender'],
        age=kwargs['age'],
        occupation=kwargs['occupation'],
        is_subscribe=kwargs['is_subscribe'],
        subscribe_expire=kwargs['subscribe_expire']
    )

    return profile


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    genres = models.CharField(max_length=500)
    view_cnt = models.IntegerField(default=0)
    tmdb_id = models.IntegerField(default=0)
    poster_path = models.TextField(default="")
    overview = models.TextField(default="")
    year = models.IntegerField(default=0)
    # 새거 추가시에 왠만하면 default 값 정해주고
    #  newfield = models.TextField(default="")
    @property
    def genres_array(self):
        return self.genres.strip().split('|')

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    rating = models.IntegerField()
    timeStamp = models.DateTimeField()


class movieCluster(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    group = models.IntegerField()
    
class UserCluster(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    group = models.IntegerField()

class KnnAgeView(models.Model):
    Age=models.IntegerField(primary_key=True)
    Action = models.IntegerField(default=0)
    Adventure = models.IntegerField(default=0)
    Animation = models.IntegerField(default=0)
    Childrens = models.IntegerField(default=0)
    Comedy = models.IntegerField(default=0)
    Crime = models.IntegerField(default=0)
    Documentary = models.IntegerField(default=0)
    Drama = models.IntegerField(default=0)
    Fantasy = models.IntegerField(default=0)
    FilmNoir = models.IntegerField(default=0)
    Horror = models.IntegerField(default=0)
    Musical=models.IntegerField(default=0)
    Mystery=models.IntegerField(default=0)
    Romance=models.IntegerField(default=0)
    SciFi =models.IntegerField(default=0)
    Thriller = models.IntegerField(default=0)
    War =models.IntegerField(default=0)
    Western =models.IntegerField(default=0)
    Max_genre=models.CharField(max_length=200)