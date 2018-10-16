from django.shortcuts import render
from Films.models import Movie, User
from django.forms import ModelForm

# Create your views here.

def ListFilms(request):
    objets = Movie.objects.all().order_by('title')
    return render(request,'ListFilms.html',{'objets':objets})

class InscriptionForm(ModelForm):
    class Meta:
        model = User
        fields = ('login', 'password')
        labels = {
            'pseudo': 'Pseudo',
            'password': 'Mot de passe',
        }

def inscription(request):
    form = InscriptionForm()
    if request.method == "POST":
        new_user = form.save()
