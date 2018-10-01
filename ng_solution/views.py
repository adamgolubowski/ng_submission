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
            return Response({'message': 'test get {0}'.format(data)})
        return Response({'message': serializer.errors}, status=400)
