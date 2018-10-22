from django.urls import path
from . import views
from .views import ListFilms
from . import views as core_views
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
    path(r'addDirector', views.AddDirector, name='AddDirector'),
    path(r'updateDirector/<int:director_id>', views.UpdateDirector, name='Updatedirector'),
    path(r'deleteDirector/<int:director_id>', views.DeleteDirector, name='Deletedirector'),

    #Comment
    path(r'updateComment/<int:comment_id>', views.UpdateComment, name='UpdateComment'),
    path(r'deleteComment/<int:comment_id>/<int:movie_id>', views.DeleteComment, name='DeleteComment'),

    path(r'detail/<int:movie_id>', views.detail, name='detail'),
    path(r'signup/', core_views.signup, name='signup'),
    
]