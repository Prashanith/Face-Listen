from django.contrib import admin
from .models import UserPlayList
from .models import SongsDatabase
from .models import Emotion
# Register your models here.

admin.site.register(UserPlayList)
admin.site.register(SongsDatabase)
admin.site.register(Emotion)

