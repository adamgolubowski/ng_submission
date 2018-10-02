from rest_framework import serializers
from ng_solution.models import Movie, Comment
from datetime import datetime

class MovieSerializer(serializers.Serializer):
    title = serializers.CharField()

    def save(self, data):
        m = Movie(title = data['Title'],
                  year = int(data['Year']),
                  rated = data['Rated'],
                  released = datetime.strptime(data['Released'], '%d %b %Y').date(),
                  runtime = data['Runtime'],
                  genre = data['Genre'],
                  director = data['Director'],
                  writer = data['Writer'],
                  actors = data['Actors'],
                  plot = data['Plot'])
        m.save()

class CommentSerializer(serializers.ModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())

    class Meta:
        model = Comment
        fields = ('id','movie','body')

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
