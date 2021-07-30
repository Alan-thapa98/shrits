from django.contrib import admin
from django.urls import path, include
from home import views
# from .views import (
#     # my_profile_view,
#     invites_received_view,
#     profiles_list_view,
#     invite_profiles_list_view,
#     ProfileDetailView,
#     ProfileListView,
#     send_invatation,
#     remove_from_friends,
#     accept_invatation,
#     reject_invatation,
# )

# app_name = 'profiles'


urlpatterns = [
    path('', views.Home, name="Home"),
    path('Whenplay/videos<int:Video_id>in-shareits',
         views.Whenplay, name="Whenplay"),
    path('Videos', views.Videos, name="Videos"),
    path('<str:Username>.html', views.channel, name="channel"),
    path('search', views.search, name="search"),
    path('demo', views.demo, name="demo"),



    path('signup', views.signup, name="signup"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    # path('/postComment', views.postComment, name="postComment"),
    # path('/', views.blogHome, name="bloghome"),
    # path('/<str:slug>', views.blogPost, name="blogPost"),


]
