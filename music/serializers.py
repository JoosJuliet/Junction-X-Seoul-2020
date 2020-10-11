from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers


from .models import User, Music, MusicLocation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'


class MusicLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicLocation
        fields = '__all__'


class MusicLocadtionSerializer(serializers.ModelSerializer):
    pass