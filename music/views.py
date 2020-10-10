from django.http import HttpResponse

import math
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


#  POST /users/{zeppeto_hash_code}/music -> 계

def post_user_memory(request, zeppeto_hash_code):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(zeppeto_hash_code)




def get_user_musics(request, zeppeto_hash_code):
    return HttpResponse(zeppeto_hash_code)
#GET /users/{zeppeto_hash_code}/musics
