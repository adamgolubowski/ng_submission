﻿# Netguru Python Developer recruitment solution

## Author
Adam Gołubowski
e-mail: adam.golubowski@gmail.com
mobile: +48 662 052 984
web: http://adamgolubowski.github.io

## Quick start
#### Running locally
The easiest way to run the application is to use Docker.
```
$ git clone https://github.com/adamgolubowski/ng_submission.git
$ cd ng_submission
$ docker-compose build
$ docker-compose up
```
Next, use tool like curl to send a sample request:
```
$ curl --header "Content-Type: application/json" \
	 --request POST \
	 --data '{"title":"Lady Bird"}' \
	 http://localhost:8000/movies/
{"Title":"Lady Bird","Year":"2017","Rated":"R","Released":"01 Dec 2017","Runtime":"94 min","Genre":"Comedy, Drama","Director":"Greta Gerwig",...}
```
#### Using Heroku app
The application has been deployed to Heroku: `https://ngsubmission.herokuapp.com`. endpoints:
```
https://ngsubmission.herokuapp.com/movies
https://ngsubmission.herokuapp.com/comments
```

## Task
We’d like you to build simple REST API for us - a basic movie database interacting with external API.  Here’s full specification of endpoints that we’d like it to have:

-   POST /movies:
    -   Request body should contain only movie title, and its presence should be validated.
    -   Based on passed title, other movie details should be fetched from [http://www.omdbapi.com/](https://workable.com/nr?l=http%3A%2F%2Fwww.omdbapi.com%2F) (or other similar, public movie database) - and saved to application database.
    -   Request response should include full movie object, along with all data fetched from external API.
-   GET /movies:
    -   Should fetch list of all movies already present in application database.
    -   Additional filtering, sorting is fully optional - but some implementation is a bonus.
-   POST /comments:
    -   Request body should contain ID of movie already present in database, and comment text body.
    -   Comment should be saved to application database and returned in request response.
-   GET /comments:
    1.  Should fetch list of all comments present in application database.
    2.  Should allow filtering comments by associated movie, by passing its ID.

## Solution
I created a Django application using Django-REST framework. The application exposes two resources: `movies` and `comments`. 

### Endpoints

#### GET /movies/
returns list of movies in the database.
example: 
```
crul https://ngsubmission.herokuapp.com/movies/
```

#### POST /movies/
add movie to database. The application will use OMBDAPI service to request details for a movie specified in `title` field in the request body.  If the service returns details successfully then the application saves information and returns details of a movie.
example: 
```
curl --header "Content-Type: application/json" \
	 --request POST \
	 --data "{\"title\":\"Lady Bird\"}" \
	 https://ngsubmission.herokuapp.com/movies/
```

#### GET /comments/
returns list of comments in the database
example: 
```
curl https://ngsubmission.herokuapp.com/comments/
```
#### GET /comments/?movieid=`<id>`
returns comments for a movie with id = `<id>`
example: 
```
curl https://ngsubmission.herokuapp.com/comments/?movieid=1
```

#### POST /comments/
add new comment to a movie available in the database. Request body must include fields: `movie` - id of a movie existing in the database, `body` - comment body
example:
```
curl --header "Content-Type: application/json" \
	 --request POST \
	 --data "{\"movie\":1, \"body\":\"test comment\"}" \
	 https://ngsubmission.herokuapp.com/comments/
```

### Running locally
The solution can be run locally using Docker. 
```
$ cd ng_submission
$ docker-compose build
$ docker-compose up
```
this creates a container called `ng_submission_backend_1` and starts application in it. The application is available on localhost, e.g. `localhost:8000/movies`

### Using Heroku App
The application was deployed to Heroku. Use web browser and navigate to:
```
https://ngsubmission.herokuapp.com/movies
https://ngsubmission.herokuapp.com/comments
```

### Tests
The solution includes unit tests. Run tests with  `manage.py test`. The example below shows how to execute tests on a local instance of the application:
```
$ cd ng_submission
$ docker-compose build
$ docker-compose up
$ docker exec -it ng_submission_backend_1 bash
root@b3e7d0415c2c:/ng# ./manage.py test

```
