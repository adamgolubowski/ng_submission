from rest_framework import serializers
from ng_solution.models import Movie

class MovieSerializer(serializers.Serializer):
    title = serializers.CharField()

    def save(self, data):
        return(Movie.objects.create(data))
