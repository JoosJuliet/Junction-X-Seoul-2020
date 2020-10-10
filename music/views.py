from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def ping(request):
    return HttpResponse('pong')

# GET /musics
def get_musics(request):
    return HttpResponse('get_musics')


#  POST /users/{zeppeto_hash_code}/music -> 계

def post_user_memory(request, zeppeto_hash_code):

    return HttpResponse(zeppeto_hash_code)




def get_user_musics(request, zeppeto_hash_code):
    return HttpResponse(zeppeto_hash_code)
#GET /users/{zeppeto_hash_code}/musics
