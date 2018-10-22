from django.test import TestCase
from django.utils.timezone import now
from Films.models import Movie
from Films.models import Director
from Films.models import Actor
from Films.models import Comment
from Films.models import Genre
from django.contrib.auth.models import User

# Create your tests here.

class CreateTest(TestCase):
    
    def test_createDirector_aucunParam_cree(self):
        #creation realisateur
        Director.objects.create(firstname="Dir", name="Un Directeur")
        Realisateur = Director.objects.get(name="Un Directeur")
        self.assertEqual(Realisateur.name,"Un Directeur")

    def test_createActor_aucunParam_cree(self):
        #creation acteur
        Actor.objects.create(firstname="Act", name="UN acteur")
        Acteur = Actor.objects.get(name="UN acteur")
        self.assertEqual(Acteur.name,"UN acteur")

    def test_createGenre_aucunParam_cree(self):
        #creation genre
        Genre.objects.create(name="UN genre")
        genre = Genre.objects.get(name="UN genre")
        self.assertEqual(genre.name, "UN genre")

    def test_createComment_aucunParam_cree(self):
        #creation utilisateur
        User.objects._create_user(username="User", email="",password="User")
        Utilisateur = User.objects.get(username="User")
        #creation commentaire
        Comment.objects.create(text="Un commentaire TEST", score="1", user=Utilisateur)
        Commentaire = Comment.objects.get(text="Un commentaire TEST")
        self.assertEqual(Commentaire.text, "Un commentaire TEST")


    
    
    def test_createFilm_aucunParam_cree(self):
        #creation realisateur
        Director.objects.create(firstname="Dir", name="Un Directeur")
        Realisateur = Director.objects.get(name="Un Directeur")
        #creation acteur
        Actor.objects.create(firstname="Act", name="UN acteur")
        Acteur = Actor.objects.get(name="UN acteur")
        #creation utilisateur
        User.objects._create_user(username="User", email="",password="User")
        Utilisateur = User.objects.get(username="User")
        #creation commentaire
        Comment.objects.create(text="Un commentaire TEST", score="1", user=Utilisateur)
        Commentaire = Comment.objects.get(text="Un commentaire TEST")
        #creation film
        Movie.objects.create(title="LE test", score="5", realease_date=now(), director=Realisateur, genre="test")
        Film = Movie.objects.get(title="LE test")
        self.assertEqual(Film.title,"LE test")