from django.db import models
from django import forms

# Create your models here.
class Realisator(models.Model):
    firstname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname + " " + self.name

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

    def __str__(self):
        return self.firstname + " " + self.name

class User(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    admin = models.BooleanField(default=False)

class Comment(models.Model):
    user = models.OneToOneField('User', on_delete=False)
    text = models.TextField(max_length=1000)
    score = models.FloatField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users", default="")
    #comment = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="comments", default="")




