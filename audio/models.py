from django.contrib.auth.models import User
from django.db import models
from django.db.models import URLField


class AudioKniga(models.Model):
    name = models.CharField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='book', null=True)
    author = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    genre = models.CharField(max_length=255, blank=True)
    desc = models.CharField(max_length=1000)
    audio_url = URLField(max_length=1000, blank=True)


class Wish(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=255, unique=True)
    book_author = models.CharField(max_length=255)
    book_photo = models.CharField(max_length=255)