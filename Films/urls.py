from django.urls import path
from .views import ListFilms

urlpatterns = [
    path(r'List', ListFilms, name='ListFilms'),
    
]