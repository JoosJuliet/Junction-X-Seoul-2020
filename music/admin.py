from django.contrib import admin

# Register your models here.
from .models import User, Music, MusicLocation

admin.site.register(User)
admin.site.register(Music)
admin.site.register(MusicLocation)
