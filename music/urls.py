from django.contrib import admin
from django.urls import path, include

from music import views

urlpatterns = [
    path(f'users/<slug:zeppeto_hash_code>/musics', views.get_user_musics),
    path(f'musics', views.get_user_musics),
    path(f'users/<slug:zeppeto_hash_code>/music', views.post_user_memory)

]


