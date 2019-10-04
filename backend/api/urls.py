from django.conf.urls import url
from api.views import movie_views, rating_views, user_views
from api.views import auth_views,cluster_views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from api.views import knn_views

urlpatterns = [
    url('auth/signup-many/$', auth_views.signup_many, name='sign_up_many'),
    url('movies/$', movie_views.movies, name='movie_list'),
    url('movies/delete/$', movie_views.movies, name='movie_delete'),
    url('movies/edit/$', movie_views.edit_movie, name='edit_movie'),
    url('movies/watch-list/$', movie_views.movie_by_user, name='watch_list'),
    url('ratings/$', rating_views.ratings, name='rating_list'),
    url('update_view_cnt/$', movie_views.update_view_cnt, name='update_view_cnt'),
    url('auth/detail/$', auth_views.get_profile, name='get_profile'),
    url('users/edit/$', user_views.edit_profile, name='edit_profile'),
    url('users/all/$', user_views.all_profiles, name='all_profiles'),
    url('users/delete/$', user_views.delete_user, name='delete_user'),
    url('auth/signup/$',auth_views.signup,name='signup'),
    url('auth/login/$',auth_views.login,name='login'),
    url('auth/logout/$', auth_views.logout, name='logout'),
    url('auth/on/$', auth_views.on_auth_state, name='on_auth'),
    url('auth/duplicate/$', auth_views.user_duplicate, name='user_duplicate'),
    url('auth/subscribe/$', auth_views.update_subscribe, name='update_subscribe'),

    url('auth/api-token-auth/', obtain_jwt_token),
    url('auth/api-token-refresh/', refresh_jwt_token),
    url('auth/api-token-verify/', verify_jwt_token),
    url('cluster/clusterUser/$',cluster_views.usercluster_many,name='usercluster_many'),
    url('cluster/clusterMovie/$',cluster_views.moviecluster_many,name='moviecluster_many'),
    url('cluster/getClusterMovie/$',cluster_views.get_moviegroup,name=' get_moviegroup'),
    url('cluster/getClusterUser/$',cluster_views.get_usergroup,name=' get_usergroup'),

    url('recommend/knn_age_view/$',knn_views.reg_knn_age_view,name='reg_knn_age_view'),
    url('recommend/knn_age_view/update/$',knn_views.update_knn_age_view,name='update_knn_age_view'),
    url('recommend/knn_age_view/get/$',knn_views.get_knn_age_view,name='get_knn_age_view'),

    url('recommend/svd/$',rating_views.svd,name='svd'),
]
