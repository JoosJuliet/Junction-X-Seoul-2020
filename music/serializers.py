from rest_framework.serializers import ModelSerializer

from music.models import MusicLocation


class MusicLocationSerializer(ModelSerializer):
    class Meta:
        model = MusicLocation
        fields = '__all__'
        depth = 1
