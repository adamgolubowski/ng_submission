from ng_solution.models import Movie, Comment
from ng_solution.serializers import MovieSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class MoviesList(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            title = data['title']
            movie_details = Movie.getMovieDetails(title)
            if 'Error' not in movie_details and Movie.checkIfExists(title) == False:
                serializer.save(movie_details)
            return Response(movie_details)
            #else
            #result = serializer.save(movie_details)
            #return Response({'message': ' {0}'.format(result)})
        else:
            return Response({'message': serializer.errors}, status=400)

class CommentsList(APIView):

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'message': serializer.errors}, status=400)

class CommentsQuery(APIView):
    def get(self,request,movieid):
        return Response(status=200)