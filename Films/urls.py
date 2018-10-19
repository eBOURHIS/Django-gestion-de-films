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
    path(r'updateActor/<int:actor_id>', views.UpdateActor, name='UpdateActor'),
    path(r'deleteActor/<int:actor_id>', views.DeleteActor, name='DeleteActor'),

    #Realisateur
    path(r'addRealisator', views.AddRealisator, name='AddRealisator'),
    path(r'updateRealisator/<int:realisator_id>', views.UpdateRealisator, name='UpdateRealisator'),
    path(r'deleteRealisator/<int:realisator_id>', views.DeleteRealisator, name='DeleteRealisator'),

    #Comment
    path(r'addComment', views.AddComment, name='AddComment'),
    path(r'updateComment/<int:comment_id>', views.UpdateComment, name='UpdateComment'),
    path(r'deleteComment/<int:comment_id>', views.DeleteComment, name='DeleteComment'),

    path(r'detail/<int:movie_id>', views.detail, name='detail'),  
    
]