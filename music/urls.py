from django.contrib import admin
from django.urls import path, include

from music import views

urlpatterns = [
    path(f'user/<slug:zeppeto_hash_code>/musics', views.post_user_memory)
]


# urlpatterns += router.urls
#GET /users/{zeppeto_hash_code}/musics
# GET /musics
#  POST /users/{zeppeto_hash_code}/music -> 계