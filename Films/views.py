from django.shortcuts import render, redirect
from Films.models import Movie, Actor, Realisator, Comment, User
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

def detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_Comment = form.save()
            movie.comments.add(new_Comment)
            movie.save
            messages.success(request, 'Nouveau comment')
            form = CommentForm()
    context = {'form':form}
    return render(request, 'detail.html', {'movie':movie, 'form':form, 'id':movie_id})

def DeleteFilm(request, film_id):
    objet = Movie.objects.get(pk=film_id)
    objet.delete()
    objets = Movie.objects.all().order_by('title')
    return render(request, 'ListFilms.html',{'objets':objets})

@login_required
def UpdateFilm(request, film_id):
    objet = Movie.objects.get(pk=film_id)
    if request.method == "POST":
        form = FilmForm(request.POST, instance=objet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modification du film: ' +objet.title+' effectuée')
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
            return redirect(reverse('ListFilms'))
    context = {'form':form}
    return render(request, 'CreateFilm.html',context)

def DetailFilm(request, film_id):
    objet = Movie.objects.get(pk=film_id)
    return render(request,'DetailFilm.html',{'objet':objet})

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
        fields = ('title', 'score','realease_date','realisator','actors','genre')

#Acteur

class ActorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ActorForm, self).__init__(*args, **kwargs)
        self.fields['firstname'].label = "Prénom"
        self.fields['name'].label = "Nom"
    class Meta:
        model = Actor
        fields = ('firstname', 'name')

def AddActor(request):
    form = ActorForm()
    if request.method == 'POST':
        form = ActorForm(request.POST)
        if form.is_valid():
            new_Actor = form.save()
            messages.success(request, 'Nouveau acteur')
            context = {'objet': new_Actor}
            return redirect(reverse('ListFilms'))
    context = {'form':form}
    return render(request, 'CreateActor.html',context)

def DeleteActor(request, actor_id):
    objet = Actor.objects.get(pk=actor_id)
    objet.delete()
    return redirect(reverse('ListFilms'))

def UpdateActor(request, actor_id):
    objet = Actor.objects.get(pk=actor_id)
    if request.method == "POST":
        form = FilmForm(request.POST, instance=objet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modification de acteur éffectuée')
            context = {'objet':objet}
            return redirect(reverse('ListFilms'))
    form = ActorForm(instance=objet)
    context = {'form':form, 'objet':objet}
    return redirect(reverse('ListFilms'))

#Realisateur

class RealisatorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RealisatorForm, self).__init__(*args, **kwargs)
        self.fields['firstname'].label = "Prénom"
        self.fields['name'].label = "Nom"
    class Meta:
        model = Realisator
        fields = ('firstname', 'name')

def AddRealisator(request):
    form = RealisatorForm()
    if request.method == 'POST':
        form = RealisatorForm(request.POST)
        if form.is_valid():
            new_Realisator = form.save()
            messages.success(request, 'Nouveau realisateur')
            context = {'objet': new_Realisator}
            return redirect(reverse('ListFilms'))
    context = {'form':form}
    return render(request, 'CreateRealisator.html',context)

def DeleteRealisator(request, realisator_id):
    objet = Realisator.objects.get(pk=realisator_id)
    objet.delete()
    return redirect(reverse('ListFilms'))

def UpdateRealisator(request, realisator_id):
    objet = Realisator.objects.get(pk=realisator_id)
    if request.method == "POST":
        form = RealisatorForm(request.POST, instance=objet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modification de realisateur éffectuée')
            context = {'objet':objet}
            return redirect(reverse('ListFilms'))
    form = RealisatorForm(instance=objet)
    context = {'form':form, 'objet':objet}
    return redirect(reverse('ListFilms'))

#Comment

class CommentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].label = "Commentaire"
        self.fields['score'].label = "Note"
        self.fields['user'].label = "Utilisateur"
    class Meta:
        model = Comment
        fields = ('text', 'score', 'user')

def DeleteComment(request, comment_id, movie_id):
    objet = Comment.objects.get(pk=comment_id)
    objet.delete()
    return redirect('/films/detail/'+str(movie_id))

def UpdateComment(request, comment_id):
    objet = Comment.objects.get(pk=comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=objet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modification du commentaire réalisé')
            context = {'objet':objet}
            return redirect(reverse('ListFilms'))
    form = CommentForm(instance=objet)
    context = {'form':form, 'objet':objet}
    return redirect(reverse('ListFilms'))
