import math

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from music.models import MusicLocation, User, Music
from music.serializers import MusicLocationSerializer


class MusicLocationViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = MusicLocationSerializer
    queryset = MusicLocation.objects.select_related('user', 'music')

    music_name_param = openapi.Parameter(
        'musicName',
        openapi.IN_QUERY,
        type=openapi.TYPE_STRING
    )
    zeppeto_param = openapi.Parameter(
        'zeppetoHashCode',
        openapi.IN_QUERY,
        type=openapi.TYPE_STRING
    )
    longitude_param = openapi.Parameter(
        'longitude',
        openapi.IN_QUERY,
        type=openapi.TYPE_NUMBER
    )
    latitude_param = openapi.Parameter(
        'latitude',
        openapi.IN_QUERY,
        type=openapi.TYPE_NUMBER
    )

    @swagger_auto_schema(manual_parameters=[zeppeto_param])
    def list(self, request, *args, **kwargs):
        query_params = self.request.query_params
        zeppeto_hash_code = query_params.get('zeppetoHashCode', None)

        return Response(
            MusicLocationSerializer(
                self.get_queryset().filter(user__zeppeto_hash_code=zeppeto_hash_code),
                many=True
            )
        )

    def _getBoundsFromLatLng(self, lat, lng):
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

    @swagger_auto_schema(manual_parameters=[longitude_param, latitude_param])
    @action(detail=False)
    def musics(self, request):
        query_params = request.query_params
        longitude = query_params.get('longitude')
        latitude = query_params.get('latitude')

        if not longitude or not latitude:
            return Response(data={'message': 'longitude and latitude are required.'})

        longitude, latitude = float(longitude), float(latitude)

        bounds = self._getBoundsFromLatLng(latitude, longitude)
        return Response(
            MusicLocationSerializer(MusicLocation.objects.filter(
                latitude__range=(bounds['lat_min'], bounds['lat_max'])
            ).filter(
                longitude__range=(bounds['lng_min'], bounds['lng_max'])
            ), many=True).data
        )

    @swagger_auto_schema(request_body=MusicLocationSerializer)
    @action(detail=False, methods=['post'])
    def music(self, request):
        data = request.data
        longitude = data.get('longitude')
        latitude = data.get('latitude')
        zeppeto_hash_code = data.get('zeppetoHashCode')
        music_name = data.get('musicName')

        if longitude is None or latitude is None or not zeppeto_hash_code or not music_name:
            return Response(
                data={'message': 'longitude and latitude and zeppetoHashCode and musicName are required.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user, created = User.objects.get_or_create(zeppeto_hash_code=zeppeto_hash_code)
        music, created = Music.objects.get_or_create(name=music_name)

        MusicLocation.objects.create(
            user=user, music=music, longitude=longitude, latitude=latitude
        )
        return Response(status=status.HTTP_201_CREATED)
