from django.contrib import admin
from Films.models import Movie, Genre, Actor, Director, Comment, User

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'score', 'realease_date', 'director', 'actors', 'genre', 'image')

class ActorAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'name')

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'name')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'score')


admin.site.register(Movie)#MovieAdmin
admin.site.register(Genre)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Comment, CommentAdmin)


