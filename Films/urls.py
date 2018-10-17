from django.urls import path
from . import views
from .views import ListFilms

urlpatterns = [

    #Film
    path(r'list', views.ListFilms, name='ListFilms'),
    path(r'updateFilm/<int:film_id>', views.UpdateFilm, name='UpdateFilm'),
    path(r'deleteFilm/<int:film_id>', views.DeleteFilm, name='DeleteFilm'),
    path(r'addFilm', views.AddFilm, name='AddFilm'),

    #Acteur
    path(r'addActor', views.AddActor, name='AddActor'),

    #Realisateur
    path(r'addRealisator', views.AddRealisator, name='AddRealisator'),

    #Comment
    path(r'addComment', views.AddComment, name='AddComment')    
    
]