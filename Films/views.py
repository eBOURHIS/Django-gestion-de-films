from django.shortcuts import render, redirect
from Films.models import Movie, Actor, Director, Comment
from django.forms import ModelForm, Textarea
from django import forms
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from django.template import RequestContext
from django.db import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/films/list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def ListFilms(request):
    objets = Movie.objects.all().order_by('title')
    paginator = Paginator(objets, 3)

    page = request.GET.get('page')

    objets = paginator.get_page(page)

    return render(request,'ListFilms.html', {'objets':objets})

def detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_Comment = form.save()
            new_Comment.user = request.user
            new_Comment.save()
            movie.comments.add(new_Comment)
            movie.save
            messages.success(request, 'Nouveau comment')
            form = CommentForm()
    context = {'form':form}
    return render(request, 'detail.html', {'movie':movie, 'form':form, 'id':movie_id})

@login_required
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

class FilmForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FilmForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Titre"
        self.fields['score'].label = "Note"
        self.fields['realease_date'].label = "Date de Sortie"
        self.fields['director'].label = "Realisateur"
        self.fields['actors'].label = "Acteur"
        self.fields['genre'].label = "Genre"
    class Meta:
        model = Movie
        fields = ('title', 'score','realease_date','director','actors','genre')

#Acteur

class ActorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ActorForm, self).__init__(*args, **kwargs)
        self.fields['firstname'].label = "Prénom"
        self.fields['name'].label = "Nom"
    class Meta:
        model = Actor
        fields = ('firstname', 'name')

@login_required
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

@login_required
def DeleteActor(request, actor_id):
    objet = Actor.objects.get(pk=actor_id)
    objet.delete()
    return redirect(reverse('ListFilms'))

@login_required
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

class DirectorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(DirectorForm, self).__init__(*args, **kwargs)
        self.fields['firstname'].label = "Prénom"
        self.fields['name'].label = "Nom"
    class Meta:
        model = Director
        fields = ('firstname', 'name')

@login_required
def AddDirector(request):
    form = DirectorForm()
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            new_Director = form.save()
            messages.success(request, 'Nouveau realisateur')
            context = {'objet': new_Director}
            return redirect(reverse('ListFilms'))
    context = {'form':form}
    return render(request, 'CreateDirector.html',context)

@login_required
def DeleteDirector(request, director_id):
    objet = Director.objects.get(pk=director_id)
    objet.delete()
    return redirect(reverse('ListFilms'))

@login_required
def UpdateDirector(request, director_id):
    objet = Director.objects.get(pk=director_id)
    if request.method == "POST":
        form = DirectorForm(request.POST, instance=objet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modification de realisateur éffectuée')
            context = {'objet':objet}
            return redirect(reverse('ListFilms'))
    form = DirectorForm(instance=objet)
    context = {'form':form, 'objet':objet}
    return redirect(reverse('ListFilms'))

#Comment

class CommentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].label = "Commentaire"
        self.fields['score'].label = "Note"

    class Meta:
        model = Comment
        fields = ('text', 'score')

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
    #form = CommentForm(instance=objet)
    context = {'form':form, 'objet':objet}
    return redirect(reverse('ListFilms'))
