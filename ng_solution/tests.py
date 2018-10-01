from rest_framework.test import APITestCase
from ng_solution.serializers import MovieSerializer
from ng_solution.models import Movie

STATUS_SUCCESS = 200
STATUS_ERROR = 400

class PostMovie(APITestCase):
    def setUp(self):
        self.url = '/movies/'
        Movie.objects.create(
            title='Call Me By Your Name',
            year=2017)

    def test_title_missing(self):
        data = {}
        response = self.client.post(self.url,data,format='json')
        self.assertEqual(response.status_code,STATUS_ERROR)

    def test_post_new_movie(self):
        data = {'title': 'Lady Bird'}
        response = self.client.post(self.url,data,format='json')
        self.assertEqual(response.status_code, STATUS_SUCCESS)

    def test_missing_movie_lookup(self):
        data = {'title': 'Lady Bird'}
        lookup_result = Movie.checkIfExists(data)
        self.assertEqual(lookup_result, False)

    def test_existing_movie_lookup(self):
        data = {'title': 'Call Me By Your Name'}
        lookup_result = Movie.checkIfExists(data)
        self.assertEqual(lookup_result, True)
