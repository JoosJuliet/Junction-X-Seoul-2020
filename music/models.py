from django.db import models

# Create your models here.
from django_extensions.db.models import TimeStampedModel


class User(TimeStampedModel):
    zeppeto_hash_code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return f' name : {self.name}/ zeppeto_hash_code:  {self.zeppeto_hash_code}/ password: {self.password} '


class Music(TimeStampedModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'name: {self.name} '


class MusicLocation(TimeStampedModel):
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    music = models.ForeignKey('Music', on_delete=models.DO_NOTHING)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return f'{self.id} / {self.user} {self.music}/ 위치 {self.longitude} - {self.latitude}'