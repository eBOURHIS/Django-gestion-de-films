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
from django.contrib.auth.decorators import user_passes_test
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

def List(request):
    objets = Movie.objects.all().order_by('release_date')
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

class FilmForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FilmForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Titre"
        self.fields['score'].label = "Note"
        self.fields['release_date'].label = "Date de Sortie"
        self.fields['director'].label = "Realisateur"
        self.fields['actors'].label = "Acteur"
        self.fields['genre'].label = "Genre"
        self.fields['synopsis'].label = "Synopsis"
        self.fields['image'].label = "Image"

    class Meta:
        model = Movie
        fields = ('title', 'score','release_date','director','actors','genre', 'synopsis', 'image')


@user_passes_test(lambda u: u.is_superuser)
def listFilms(request):
    movies = Movie.objects.all()
    form = FilmForm()
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            new_movie = form.save()
            return redirect(reverse('listFilms'))
    context = {"movies": movies, "form": form}
    return render(request, 'CreateFilm.html', context)

@user_passes_test(lambda u: u.is_superuser)
def DeleteFilm(request, film_id):
    objet = Movie.objects.get(pk=film_id)
    objet.delete()
    objets = Movie.objects.all().order_by('title')
    return render(request, 'listFilms.html',{'objets':objets})

@user_passes_test(lambda u: u.is_superuser)
def UpdateFilm(request, film_id):
    films = Movie.objects.all()
    film = Movie.objects.get(pk=film_id)
    form = FilmForm(instance=film)
    if request.method == 'POST':
        form = ActorForm(request.POST, instance=film)
        if form.is_valid():
            form.save()
            return redirect(reverse('listFilms'))
    contexte = {'form': form, 'path' : str(film_id), 'films' : films}
    return render(request, 'CreateFilm.html', contexte)

@user_passes_test(lambda u: u.is_superuser)
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

#Acteur

class ActorForm(ModelForm):
    class Meta:
        model = Actor
        fields = ('firstname', 'name')
        labels = {
            'name' : 'Nom',
            'firstname' : 'Prénom',
        }

@user_passes_test(lambda u: u.is_superuser)
def listActor(request):
    actors = Actor.objects.all()
    form = ActorForm()
    if request.method == 'POST':
        form = ActorForm(request.POST)
        if form.is_valid():
            new_actor = form.save()
            return redirect(reverse('listActor'))
    context = {"actors": actors, "form": form}
    return render(request, 'CreateActor.html', context)

@user_passes_test(lambda u: u.is_superuser)
def AddActor(request):
    form = ActorForm()
    if request.method == 'POST':
        form = ActorForm(request.POST)
        if form.is_valid():
            new_Actor = form.save()
            messages.success(request, 'Nouveau acteur')
            context = {'objet': new_Actor}
            return redirect(reverse('listActor'))
    context = {'form':form}
    return render(request, 'CreateActor.html',context)

@user_passes_test(lambda u: u.is_superuser)
def DeleteActor(request, actor_id):
    objet = Actor.objects.get(pk=actor_id)
    objet.delete()
    return redirect(reverse('listActor'))

@user_passes_test(lambda u: u.is_superuser)
def UpdateActor(request, actor_id):
    actors = Actor.objects.all()
    actor = Actor.objects.get(pk=actor_id)
    form = ActorForm(instance=actor)
    if request.method == 'POST':
        form = ActorForm(request.POST, instance=actor)
        if form.is_valid():
            form.save()
            return redirect(reverse('listActor'))
    contexte = {'form': form, 'path' : str(actor_id), 'actors' : actors}
    return render(request, 'CreateActor.html', contexte)

#Realisateur

class DirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = ('firstname', 'name')
        labels = {
            'name' : 'Nom',
            'firstname' : 'Prénom',
        }

@user_passes_test(lambda u: u.is_superuser)
def listRealisator(request):
    realisators = Director.objects.all()
    form = DirectorForm()
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            new_director = form.save()
            return redirect(reverse('listRealisator'))
    context = {"realisators":realisators, "form": form}
    return render(request, 'CreateDirector.html',context)

@user_passes_test(lambda u: u.is_superuser)
def DeleteDirector(request, director_id):
    movies = Movie.objects.filter(director=Director.objects.get(pk=director_id))
    for movie in movies:
        movie.director = None
        movie.save()
    Director.objects.get(pk=director_id).delete()
    return redirect(reverse('listRealisator'))

@user_passes_test(lambda u: u.is_superuser)
def UpdateDirector(request, director_id):
    realisators = Director.objects.all()
    realisator = Director.objects.get(pk=director_id)
    form = DirectorForm(instance=realisator)
    if request.method == 'POST':
        form = DirectorForm(request.POST, instance=realisator)
        if form.is_valid():
            form.save()
            return redirect(reverse('listRealisator'))
    contexte = {'form': form, 'path' : str(director_id), 'realisators' : realisators}
    return render(request, 'CreateDirector.html', contexte)

#Comment

class CommentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].label = "Commentaire"
        self.fields['score'].label = "Note"

    class Meta:
        model = Comment
        fields = ('text', 'score')

@login_required
def DeleteComment(request, comment_id, movie_id):
    objet = Comment.objects.get(pk=comment_id)
    objet.delete()
    return redirect('/films/detail/'+str(movie_id))

@login_required
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
