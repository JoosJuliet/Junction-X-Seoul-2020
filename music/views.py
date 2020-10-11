from django.db.models import Q
from django.http import HttpResponse

import math

from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from music.models import User, Music, MusicLocation
from music.serializers import MusicLocadtionSerializer

from rest_framework.decorators import action, api_view





def ping(request):
    return HttpResponse('pong')

# GET /musics
def get_musics(request):
    return HttpResponse('get_musics')

from rest_framework.decorators import action, api_view


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()



@api_view(['POST', 'GET'])
def post_user_memory(request, zeppeto_hash_code):

    if request.method == 'POST':

        # POST	/users/{zeppeto_hash_code}/music
        # 	request	longitude
        # 		latitude
        # 		sing_name
        user = User.objects.filter(zeppeto_hash_code=zeppeto_hash_code).first()
        data = request.data
        music = Music.objects.filter(name=data['music_name']).first()
        if not music:
            return HttpResponse('음악이 없습니다, 음악을 등록해주세요')
        music_location = MusicLocation.objects.create(user=user, music=music, longitude=data['longitude'], latitude=data['latitude'])
        music_location.save()

        return HttpResponse('success')

    if request.method == 'GET':
        # GET	/users/{zeppeto_hash_code}/music
        # 	request	longitude
        # 		latitude
        # 		sing_name
        # 이거는내노래list보내주기
        user = MusicLocation.objects.select_related('user').filter(user__zeppeto_hash_code=zeppeto_hash_code).values_list('music__name', 'user__musiclocation__latitude','music__musiclocation__longitude')

        return Response(user)
