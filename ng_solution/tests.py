import ast
from rest_framework.test import APITestCase
from django.test import TestCase
from ng_solution.serializers import MovieSerializer
from ng_solution.models import Movie, Comment

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
        self.assertEqual(Movie.objects.filter(title = 'Lady Bird').exists(),True)


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
        self.assertTrue(lookup_result)

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

class ListMoviesTestCase(APITestCase):
    def setUp(self):
        self.url = '/movies/'
        Movie.objects.create(title='Call Me By Your Name',year=2017)
        Movie.objects.create(title='Lady Bird',year=2017)

    def test_list_movies(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,STATUS_SUCCESS)
        self.assertEqual(len(response.data),2)
        self.assertEqual(response.data[0]['title'],'Call Me By Your Name')
        self.assertEqual(response.data[1]['title'],'Lady Bird')

class PostCommentTestCase(APITestCase):
    def setUp(self):
        self.url = '/comments/'
        self.m1 = Movie.objects.create(title='Call Me By Your Name',year=2017)

    def test_post_comment(self):
        data = {'movie': self.m1.id,
                'body': 'test comment'}
        response = self.client.post(self.url,data,format='json')
        self.assertEqual(response.status_code,STATUS_SUCCESS)
        self.assertEqual(response.data['movie'],self.m1.id)
        self.assertEqual(response.data['body'],data['body'])

    def test_post_comment_missing_movie(self):
        data = {'movie': 9999,
                'body': 'test comment 2'}
        response = self.client.post(self.url,data,format='json')
        self.assertEqual(response.status_code,STATUS_ERROR)


class ListCommentTestCase(APITestCase):
    def setUp(self):
        self.url = '/comments/'
        self.m1 = Movie.objects.create(title='Call Me By Your Name',year=2017)
        self.m2 = Movie.objects.create(title='Lady Bird',year=2017)
        self.c1 = Comment.objects.create(movie=self.m1,body='Great movie')
        self.c2 = Comment.objects.create(movie=self.m1,body='Awesome movie')
        self.c3 = Comment.objects.create(movie=self.m2,body='Love this movie')

  
    def test_list_comments(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,STATUS_SUCCESS)
        self.assertEqual(len(response.data),3)
        self.assertEqual(response.data[0]['movie'],self.m1.id)
        self.assertEqual(response.data[0]['body'],'Great movie')
        self.assertEqual(response.data[1]['movie'],self.m1.id)
        self.assertEqual(response.data[1]['body'],'Awesome movie')

    def test_select_comment(self):
        payload = {'movieid': self.m2.id}
        response = self.client.get(self.url,data=payload)
        #import pdb; pdb.set_trace()
        self.assertEqual(response.status_code,STATUS_SUCCESS)