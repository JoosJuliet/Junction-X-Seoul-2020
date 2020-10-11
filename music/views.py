from django.http import HttpResponse

import math

from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from music.models import User, Music, MusicLocation
from music.serializers import MusicLocadtionSerializer


def getLatLngBound(lat, lng):
  # 5km 구간
  lat_change = 5 / 111.2
  lng_change = abs(math.cos(lat * (math.pi / 180)))
  bounds = {
    "lat_min": lat - lat_change,
    "lng_min": lng - lng_change,
    "lat_max": lat + lat_change,
    "lng_max": lng + lng_change
  }
  return bounds


def ping(request):
    return HttpResponse('pong')

# GET /musics
def get_musics(request):
    return HttpResponse('get_musics')

from rest_framework.decorators import action, api_view


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()

    def destroy(self, request, *args, **kwargs):
        return Response(data={'result': 'Success'})

@api_view(['POST'])
def post_user_memory(request, zeppeto_hash_code):
    data = request.data
    user = User.objects.filter(zeppeto_hash_code=zeppeto_hash_code).first()
    music = Music.objects.filter(name=data['music_name']).first()
    music_location = MusicLocation.objects.create(user=user, music=music, longitude=data['longitude'], latitude=data['latitude'])
    music_location.save()
    if request.method == 'POST':
        return HttpResponse(data)
    return HttpResponse()


# >>> r3 = Reporter(first_name='John', last_name='Smith', email='john@example.com')
# >>> Article.objects.create(headline="This is a test", pub_date=date(2005, 7, 27), reporter=r3)

# POST	/users/{zeppeto_hash_code}/music
# 	request	longitude
# 		latitude
# 		sing_name
# 		zeppeto_hash_code


def get_user_musics(request, zeppeto_hash_code):
    return HttpResponse(zeppeto_hash_code)
#GET /users/{zeppeto_hash_code}/musics
