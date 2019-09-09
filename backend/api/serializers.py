from .models import Profile, Movie, Rating
from rest_framework import serializers

class RatingSerializer(serializers.ModelSerializer):
    movie_name = serializers.SerializerMethodField('get_moivename')
    user_name = serializers.SerializerMethodField('get_username')
    class Meta :
        model = Rating
        fields = ('user','movie','rating','timeStamp','movie_name','user_name')

    def get_moivename(self,obj) :
        return obj.movie.title
    def get_username(self,obj) :
        return obj.user.username

class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    username = serializers.SerializerMethodField('get_username')
    is_staff = serializers.SerializerMethodField('get_is_staff')

    class Meta:
        model = Profile
        fields = ('id', 'username', 'is_staff', 'gender', 'age', 'occupation')

    def get_username(self, obj):
        return obj.user.username

    def get_is_staff(self, obj):
        return obj.user.is_staff
        
class MovieSerializer(serializers.ModelSerializer):
    genres_array = serializers.ReadOnlyField()
    # view_cnt = serializers.SerializerMethodField('get_viewCnt')
    average_rating = serializers.SerializerMethodField('get_rating')
    mcount = serializers.SerializerMethodField('get_mcount')
    count = serializers.SerializerMethodField('get_count')
    agecount = serializers.SerializerMethodField('get_agecount')
    
    rating_set = RatingSerializer(many=True)
    class Meta:
        model = Movie
        fields = ('id', 'title', 'genres_array','view_cnt','average_rating','rating_set','mcount','year','overview','poster_path',
            'count','agecount')
        # ,'view_cnt','rating'
    def get_viewCnt(self, obj):
        ratings = obj.rating_set.all()
        return len(ratings)

    def get_rating(self, obj):
        ratings = obj.rating_set.all()
        s = 0
        i = len(ratings)
        if i == 0 :
            return 0
        else :
            for r in ratings :
                s += r.rating
            return round(s/i,1)
            
    def get_mcount(self, obj):
        ratings = obj.rating_set.all()
        m = 0
        for r in ratings :
            if r.user.profile.gender == 'M' :
                m+=1
            elif r.user.profile.gender == 'F' :
                m-=1
        return m
    def get_count(self, obj):
        ratings = obj.rating_set.all()
        m =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        val = ["other", "academic/educator", "artist", "clerical/admin", "college/grad student",
       "customer service", "doctor/health care", "executive/managerial",  "farmer",  "homemaker",
         "K-12 student",  "lawyer",  "programmer",  "retired",  "sales/marketing",
         "scientist",   "self-employed",  "technician/engineer",  "tradesman/craftsman",
         "unemployed",  "writer"]
        for r in ratings :
            if r.user.profile.occupation == 'other' :
                m[0]+=1
            elif r.user.profile.occupation == 'academic/educator':
                m[1]+=1
            elif r.user.profile.occupation == 'artist':
                m[2]+=1
            elif r.user.profile.occupation == 'clerical/admin':
                m[3]+=1
            elif r.user.profile.occupation == 'college/grad student':
                m[4]+=1
            elif r.user.profile.occupation == 'customer service':
                m[5]+=1
            elif r.user.profile.occupation == 'doctor/health care':
                m[6]+=1
            elif r.user.profile.occupation == 'executive/managerial':
                m[7]+=1
            elif r.user.profile.occupation == 'farmer':
                m[8]+=1
            elif r.user.profile.occupation == 'homemaker':
                m[9]+=1
            elif r.user.profile.occupation == 'K-12 student':
                m[10]+=1
            elif r.user.profile.occupation == 'lawyer':
                m[11]+=1
            elif r.user.profile.occupation == 'programmer':
                m[12]+=1
            elif r.user.profile.occupation == 'retired':
                m[13]+=1
            elif r.user.profile.occupation == 'sales/marketing':
                m[14]+=1
            elif r.user.profile.occupation == 'scientist':
                m[15]+=1
            elif r.user.profile.occupation == 'self-employed':
                m[16]+=1
            elif r.user.profile.occupation == 'technician/engineer':
                m[17]+=1
            elif r.user.profile.occupation == 'tradesman/craftsman':
                m[18]+=1
            elif r.user.profile.occupation == 'unemployed':
                m[19]+=1
            elif r.user.profile.occupation == 'writer':
                m[20]+=1
        x = 0
        result = 0
        for i in range(0,21):
            if m[i] > x:
                x = m[i]
                result = i
        return val[result]
    def get_agecount(self, obj):
        ratings = obj.rating_set.all()
        m =[0,0,0,0,0,0,0]
        val = ["1", "18", "25", "35", "45","50", "56"]
       
        for r in ratings :
            
            if r.user.profile.age == 1 :
                m[0]+=1
            elif r.user.profile.age == 18:
                m[1]+=1
            elif r.user.profile.age == 25:
                m[2]+=1
            elif r.user.profile.age == 35:
                m[3]+=1
            elif r.user.profile.age == 45:
                m[4]+=1
            elif r.user.profile.age == 50:
                m[5]+=1
            elif r.user.profile.age == 56:
                m[6]+=1
        x = 0
        result = 0
        for i in range(0,7):
            if m[i] > x:
                x = m[i]
                result = i
        return val[result]
    