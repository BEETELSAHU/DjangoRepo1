from django.db import models

# Create your models here.
class Movies(models.Model):
    release_date = models.DateField()
    movie_name = models.CharField(max_length=30)
    hero_name = models.CharField(max_length=30)
    heroien_name = models.CharField(max_length=30)
    movie_rating = models.FloatField()

