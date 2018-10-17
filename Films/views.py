from django.shortcuts import render, redirect
from Films.models import Movie
from django.forms import ModelForm, Textarea
from django import forms
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from django.template import RequestContext
from django.db import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def ListFilms(request):
    objets = Movie.objects.all().order_by('title')
    return render(request,'ListFilms.html',{'objets':objets})

@login_required
def DeleteFilm(request, film_id):
    objet = Movie.objects.get(pk=film_id)
    objet.delete()
    return render(request, 'ListFilms.html')

@login_required
def UpdateFilm(request, film_id):
    objet = Movie.objects.get(pk=film_id)
    if request.method == "POST":
        form = FilmForm(request.POST, instance=objet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modification du film: ' +objet.title+' éffectuée')
            context = {'objet':objet}
            return render(request,'ListFilms.html', context)
    form = FilmForm(instance=objet)
    context = {'form':form, 'objet':objet}
    return render(request,'UpdateFilm.html', context)

@login_required
def AddFilm(request):
    form = FilmForm()
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            new_Film = form.save()
            messages.success(request, 'Nouveau Film' + new_Film.title)
            context = {'objet': new_Film}
            return render(request, 'ListFilms.html', context)
    context = {'form':form}
    return render(request, 'CreateFilm.html',context)

class FilmForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FilmForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Titre"
        self.fields['score'].label = "Note"
        self.fields['realease_date'].label = "Date de Sortie"
        self.fields['realisator'].label = "Realisateur"
        self.fields['actors'].label = "Acteur"
        self.fields['genre'].label = "Genre"
    class Meta:
        model = Movie
        fields = ('title', 'score','realease_date','realisator','actors','genre','comments')
        widgets = {
            'comments': Textarea(attrs={'cols':60,'rows':10}),
            #'realease_date': models.DateField(),
        }


