from django.urls import path
from .views import ListFilms

urlpatterns = [
    path(r'list', ListFilms, name='ListFilms'),
    
]