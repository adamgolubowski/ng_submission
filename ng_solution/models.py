from django.db import models

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
    def checkIfExists(cls, validated_data):
        match = cls.objects.filter(title = validated_data.get('title')).exists()
        return(match)
