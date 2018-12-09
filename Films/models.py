from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class Director(models.Model):
    firstname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname + " " + self.name

class Movie(models.Model):
    title = models.CharField(max_length=50)
    score = models.FloatField(max_length=20)
    realease_date = models.DateField()
    director = models.ForeignKey(Director, on_delete=False, related_name="directors", null=True)
    genre = models.CharField(max_length=50)
    actors = models.ManyToManyField('Actor')
    synopsis = models.TextField(max_length=1000, null=True)
    comments = models.ManyToManyField('Comment', blank=True)
    image = models.FileField(upload_to='', blank=True, null=True)

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Actor(models.Model):
    firstname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname + " " + self.name

class Comment(models.Model):
    text = models.TextField(max_length=1000)
    score = models.FloatField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="utilisateur", blank=True, null=True)
    #comment = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="comments", default="")
