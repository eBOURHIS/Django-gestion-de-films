from django.urls import path
from . import views
from .views import ListFilms

urlpatterns = [
    path(r'list', views.ListFilms, name='ListFilms'),
    path(r'update/<int:film_id>', views.UpdateFilm, name='UpdateFilm'),
    path(r'delete/<int:film_id>', views.DeleteFilm, name='DeleteFilm'),
    path(r'add', views.AddFilm, name='AddFilm'),
    #routes d'authentification
]