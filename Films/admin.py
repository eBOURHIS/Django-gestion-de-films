from django.contrib import admin
from Films.models import Movie, Genre, Actor, Realisator, Comment, User

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'score', 'realease_date', 'realisator', 'actors', 'genre', 'comments')

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name')

class ActorAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'name')

class RealisatorAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'name')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'score')

class UserAdmin(admin.ModelAdmin):
    list_display = ('login', 'password', 'admin')

admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Realisator, RealisatorAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(User)
