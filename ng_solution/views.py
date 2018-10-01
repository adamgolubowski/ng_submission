from ng_solution.models import Movie
from ng_solution.serializers import MovieSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class MoviesList(APIView):
    def get(self, request):
        return Response({'message': 'test GET'})

    def post(self, request):
        serializer = MovieSerializer(data = request.data)
        if serializer.is_valid():
            data = serializer.data
            title = data['title']
            if Movie.checkIfExists(title) == False:
                movie_details = Movie.getMovieDetails(title)
                serializer.save(data=movie_details)
                return Response(movie_details)
            #else
            #result = serializer.save(movie_details)
            #return Response({'message': ' {0}'.format(result)})
        return Response({'message': serializer.errors}, status=400)
