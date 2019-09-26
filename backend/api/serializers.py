from .models import Profile, Movie, Rating
from rest_framework import serializers

class RatingSerializer(serializers.ModelSerializer):
    # movie_name = serializers.SerializerMethodField('get_moivename')
    # user_name = serializers.SerializerMethodField('get_username')
    class Meta :
        model = Rating
        fields = ('user','movie','rating','timeStamp')

    # def get_moivename(self,obj) :
    #     return obj.movie.title
    # def get_username(self,obj) :
    #     return obj.user.username

class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    username = serializers.SerializerMethodField('get_username')
    is_staff = serializers.SerializerMethodField('get_is_staff')

    class Meta:
        model = Profile
        fields = ('id', 'username', 'is_staff', 'gender', 'age', 'occupation','seenmovie')

    def get_username(self, obj):
        return obj.user.username

    def get_is_staff(self, obj):
        return obj.user.is_staff
        
class MovieSerializer(serializers.ModelSerializer):
    genres_array = serializers.ReadOnlyField()
    # view_cnt = serializers.SerializerMethodField('get_viewCnt')
    #average_rating = serializers.SerializerMethodField('get_rating')
    #mcount = serializers.SerializerMethodField('get_mcount')
    #count = serializers.SerializerMethodField('get_count')
    #agecount = serializers.SerializerMethodField('get_agecount')
    agevalue = serializers.SerializerMethodField('get_agevalue')
    occupationvalue = serializers.SerializerMethodField('get_occupationvalue')
    rrating = serializers.SerializerMethodField('get_ratingvalue')
    #rating_set = RatingSerializer(many=True)
    class Meta:
        model = Movie
        fields = ('id', 'title', 'genres_array','view_cnt','rrating','agevalue','occupationvalue','rgender','year','overview','poster_path',
            )
        # ,'view_cnt','rating'
    def get_viewCnt(self, obj):
        ratings = obj.rating_set.all()
        return len(ratings)
    def get_ratingvalue(self,obj):
        rrating = obj.rrating
        return rrating
    def get_occupationvalue(self,obj):
        max = 0;
        value = ""
        if(obj.academiceducatorcount > max ):
            max = obj.academiceducatorcount
            value = "academic/educator"
        if(obj.artistcount > max):
            max = obj.artistcount
            value = "artist"
        if(obj.clericaladmincount > max):
            max = obj.clericaladmincount
            value = "clerical/admin"
        if(obj.collegegradstudentcount > max):
            max =obj.collegegradstudentcount
            value = "college/grad student"
        if(obj.customerservicecount > max):
            max = obj.customerservicecount
            value = "customer service"
        if(obj.doctorhealthcarecount > max):
            max=  obj.doctorhealthcarecount
            value = "doctor/health care"
        if(obj.executivemanagerialcount > max):
            max = obj.executivemanagerialcount
            value = "executive/managerial"
        if(obj.farmercount > max):
            max = obj.farmercount
            value ="farmer"
        if(obj.homemakercount > max):
            max=  obj.homemakercount
            value ="homemaker"
        if(obj.K12studentcount > max):
            max = obj.K12studentcount
            value = "K-12 student"
        if(obj.lawyercount > max):
            max = obj.lawyercount
            value = "lawyer"
        if(obj.programmercount > max):
            max = obj.programmercount
            value=  "programmer"
        if(obj.retiredcount > max):
            max = obj.retiredcount
            value = "retired"
        if(obj.salesmarketingcount > max):
            max= obj.salesmarketingcount
            value = "sales/marketing"
        if(obj.scientistcount > max):
            max = obj.scientistcount
            value = "scientist"
        if(obj.selfemployedcount > max):
            max = obj.selfemployedcount
            value= "self-employed"
        if(obj.technicianengineercount > max):
            max =obj.technicianengineercount
            value = "technician/engineer"
        if(obj.tradesmancraftsmancount > max):
            max = obj.tradesmancraftsmancount
            value = "tradesman/craftsman"
        if(obj.unemployedcount > max):
            max = obj.unemployedcount
            value= "unemployed"
        if(obj.writercount > max):
            max = obj.writercount
            value = "writer"
        if(obj.othercount>max):
            max =obj.othercount
            value = "other"

        return value
    def get_agevalue(self,obj):
        max = 0;
        value = ""
        if(obj.age1count> max):
            max = obj.age1count
            value = "1"
        if(obj.age18count > max):
            max = obj.age18count
            value = "18"
        if(obj.age25count > max):
            max = obj.age25count
            value = "25"
        if(obj.age35count > max):
            max=  obj.age35count
            value = "35"
        if(obj.age45count > max):
            max = obj.age45count
            value = "45"
        if(obj.age50count > max):
            max = obj.age50count
            value= "50"
        if(obj.age56count >max):
            max = obj.age56count
            value = "56"

        return value
    