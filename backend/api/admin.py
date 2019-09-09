from django.contrib import admin
from .models import Profile, Movie, Rating,UserCluster,movieCluster
# Register your models here.

class movie_cluster(admin.ModelAdmin):
    list_display = ('movie', 'group', )

admin.site.register(Movie)
admin.site.register(Profile)
admin.site.register(Rating)
admin.site.register(UserCluster)
admin.site.register(movieCluster, movie_cluster)