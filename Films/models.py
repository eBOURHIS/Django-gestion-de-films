from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class Realisator(models.Model):
    firstname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=50)
    score = models.FloatField(max_length=20)
    realease_date = models.DateField()
    realisator = models.ForeignKey(Realisator, on_delete=False, related_name="realisators", default="")
    genre = models.CharField(max_length=50)
    actors = models.ManyToManyField('Actor')
    comments = models.ManyToManyField('Comment')

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Actor(models.Model):
    firstname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

class Comment(models.Model):
    text = models.TextField(max_length=1000)
    score = models.FloatField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="utilisateur", default="")
    #comment = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="comments", default="")
