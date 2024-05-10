from django.contrib import admin
from testapp.models import Movies

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'release_date', 'movie_name', 'hero_name', 'heroien_name', 'movie_rating']

admin.site.register(Movies, MovieAdmin)