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
    seenmovie = models.TextField(default="")

#  wrapper for create user Profile
def create_profile(**kwargs):
    print(kwargs['seenmovie'])
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
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
        subscribe_expire=kwargs['subscribe_expire'],
        seenmovie=kwargs['seenmovie']
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
    rusercount = models.IntegerField(default=0)
    rrating = models.DecimalField(default=0,max_digits=4,decimal_places=2)
    rgender = models.IntegerField(default=0)
    academiceducatorcount = models.IntegerField(default=0)
    artistcount = models.IntegerField(default=0)
    clericaladmincount = models.IntegerField(default=0)
    collegegradstudentcount =models.IntegerField(default=0)
    customerservicecount = models.IntegerField(default=0)
    doctorhealthcarecount = models.IntegerField(default=0)
    executivemanagerialcount = models.IntegerField(default=0)
    farmercount = models.IntegerField(default=0)
    homemakercount =models.IntegerField(default=0)
    K12studentcount = models.IntegerField(default=0)
    lawyercount = models.IntegerField(default=0)
    programmercount = models.IntegerField(default=0)
    retiredcount = models.IntegerField(default=0)
    salesmarketingcount = models.IntegerField(default=0)
    scientistcount = models.IntegerField(default=0)
    selfemployedcount = models.IntegerField(default=0)
    technicianengineercount = models.IntegerField(default=0)
    tradesmancraftsmancount = models.IntegerField(default=0)
    unemployedcount = models.IntegerField(default=0)
    writercount =models.IntegerField(default=0)
    age1count = models.IntegerField(default=0)
    age18count = models.IntegerField(default=0)
    age25count = models.IntegerField(default=0)
    age35count = models.IntegerField(default=0)
    age45count = models.IntegerField(default=0)
    age50count = models.IntegerField(default=0)
    age56count = models.IntegerField(default=0)
    othercount = models.IntegerField(default=0)
    
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
