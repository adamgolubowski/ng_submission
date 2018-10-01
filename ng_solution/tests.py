import ast
from rest_framework.test import APITestCase
from django.test import TestCase
from ng_solution.serializers import MovieSerializer
from ng_solution.models import Movie

STATUS_SUCCESS = 200
STATUS_ERROR = 400

class PostMovieTestCase(APITestCase):
    def setUp(self):
        self.url = '/movies/'

    def test_title_missing(self):
        data = {}
        response = self.client.post(self.url,data,format='json')
        self.assertEqual(response.status_code,STATUS_ERROR)

    def test_post_new_movie(self):
        data = {'title': 'Lady Bird'}
        response = self.client.post(self.url,data,format='json')
        self.assertEqual(response.status_code, STATUS_SUCCESS)
        self.assertEqual(response.data['Title'],'Lady Bird')
        self.assertEqual(response.data['Year'],'2017')
        self.assertEqual(response.data['Director'],'Greta Gerwig')

class LookupMovieTestCase(TestCase):
    def setUp(self):
        self.test_title = 'Call Me By Your Name'
        Movie.objects.create(
            title=self.test_title,
            year=2017)

    def test_missing_movie_lookup(self):
        lookup_result = Movie.checkIfExists('Lady Bird')
        self.assertEqual(lookup_result, False)

    def test_existing_movie_lookup(self):
        lookup_result = Movie.checkIfExists(self.test_title)
        self.assertEqual(lookup_result, True)

class GetMovieDetailsTestCase(TestCase):
    def setUp(self):
        self.data = {"Title":"Lady Bird",
                     "Year":"2017",
                     "Rated":"R",
                     "Released":"01 Dec 2017",
                     "Runtime":"94 min",
                     "Genre":"Comedy, Drama",
                     "Director":"Greta Gerwig",
                     "Writer":"Greta Gerwig"}

    def test_get_movie_details(self):
        movie = Movie.getMovieDetails(self.data['Title'])
        self.assertEqual(movie['Title'],self.data['Title'])
        self.assertEqual(movie['Year'],self.data['Year'])

    def test_get_details_no_movie(self):
        movie_details = Movie.getMovieDetails('aaaa')
        self.assertIn('Error',movie_details)
