from django.db import models
from django import forms

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=50)
    score = models.FloatField(max_length=20)
    realease_date = models.DateField()
    realisator = models.OneToOneField('Realisator',on_delete=False)
    actors = models.ForeignKey('Actor', on_delete=False)
    genre = models.CharField(max_length=50)
    comments = models.ForeignKey('Comment', on_delete=models.CASCADE)

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Actor(models.Model):
    firstname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

class Realisator(models.Model):
    firstname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

class Comment(models.Model):
    user = models.OneToOneField('User', on_delete=False)
    text = models.TextField(max_length=1000)
    score = models.FloatField(max_length=50)

class User(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    admin = models.BooleanField(default=False)