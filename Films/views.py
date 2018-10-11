from django.shortcuts import render
from Films.models import Movie

# Create your views here.

def ListFilms(request):
    objets = Movie.object.all().order_By('title')
    return render(request,' ListFilms.html',{'objets':objets})