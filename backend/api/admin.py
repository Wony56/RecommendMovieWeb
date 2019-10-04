from django.contrib import admin
from .models import Profile, Movie, Rating,UserCluster,movieCluster
from .models import KnnAgeView
# Register your models here.

class profile(admin.ModelAdmin):
    list_display = ('user', 'gender', 'age', 'occupation', 'is_subscribe', 'subscribe_expire')

class movie_cluster(admin.ModelAdmin):
    list_display = ('movie', 'group', )

admin.site.register(Movie)
admin.site.register(Profile, profile)
admin.site.register(Rating)
admin.site.register(UserCluster)
admin.site.register(movieCluster, movie_cluster)
admin.site.register(KnnAgeView)