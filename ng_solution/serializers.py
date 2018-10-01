from rest_framework import serializers
from ng_solution.models import Movie

class MovieSerializer(serializers.Serializer):
    title = serializers.CharField()

    
