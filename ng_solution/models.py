import requests
from django.db import models
from django.conf import settings
import ast

class Movie(models.Model):
    title = models.TextField()
    year = models.IntegerField(null=True, blank=True)
    rated = models.CharField(max_length=100, null=True, blank=True)
    released = models.DateField(null=True)
    runtime = models.CharField(max_length=100,null=True, blank=True)
    genre = models.TextField(null=True, blank=True)
    director = models.TextField(null=True, blank=True)
    writer = models.TextField(null=True, blank=True)
    actors = models.TextField(null=True, blank=True)
    plot = models.TextField(null=True, blank=True)

    @classmethod
    def checkIfExists(cls, title):
        match = cls.objects.filter(title = title).exists()
        return(match)

    @classmethod
    def getMovieDetails(cls, title):
        payload = {'apikey': settings.API_KEY,
                    't': title}
        response = requests.get('http://www.omdbapi.com/', params=payload)
        return(ast.literal_eval(response.text))

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
