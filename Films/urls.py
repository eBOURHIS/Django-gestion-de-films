from django.urls import path
from . import views
from .views import List
from . import views as core_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    #Film
    path(r'list', views.List, name='List'),
    path(r'addFilm', views.listFilms, name='listFilms'),
    path(r'film/edit/<int:film_id>', views.UpdateFilm, name='UpdateFilm'),
    path(r'film/delete/<int:film_id>', views.DeleteFilm, name='DeleteFilm'),

    #Acteur
    path(r'addActor', views.listActor, name='listActor'),
    path(r'actor/edit/<int:actor_id>', views.UpdateActor, name='UpdateActor'),
    path(r'actor/delete/<int:actor_id>', views.DeleteActor, name='DeleteActor'),

    #Realisateur
    path(r'addDirector', views.listRealisator, name='listRealisator'),
    path(r'director/edit/<int:director_id>', views.UpdateDirector, name='Updatedirector'),
    path(r'director/delete/<int:director_id>', views.DeleteDirector, name='Deletedirector'),

    #Comment
    path(r'updateComment/<int:comment_id>', views.UpdateComment, name='UpdateComment'),
    path(r'deleteComment/<int:comment_id>/<int:movie_id>', views.DeleteComment, name='DeleteComment'),

    path(r'detail/<int:movie_id>', views.detail, name='detail'),
    path(r'signup/', core_views.signup, name='signup'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)