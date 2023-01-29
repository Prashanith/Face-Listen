from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SongsDatabase(models.Model):
    title = models.CharField(max_length=255)
    emotion = models.ForeignKey('Emotion',on_delete=models.CASCADE)
    link = models.TextField()
class UserPlayList(models.Model):
    userId = models.ForeignKey(User,on_delete = models.CASCADE)
    songFk = models.ForeignKey('SongsDatabase', on_delete=models.CASCADE)

class Emotion(models.Model):
    emotion = models.CharField(max_length=255)
    

