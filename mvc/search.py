#!/usr/bin/env python3
from imdb import IMDb
import requests

ia=IMDb()


def get_top():
    """
    Get top 250 movies from imdb
    Returns: list of movies
    """
    top = ia.get_top250_movies()

    return top


def search_movie(query):
    """
    Search for a movie in Open Movie Database
    Returns: details about movie
    """

    api_key = "&apikey=f30ed61b"
    url = 'http://www.omdbapi.com/?t={0}{1}'.format(
        query, api_key)
    response = requests.get(url)

    movie_details = {
        'title': response.json()['Title'],
        'genre': response.json()['Genre'],
        'release': response.json()['Released'],
        'plot': response.json()['Plot'],
        'rating': response.json()['imdbRating'],
        'poster_url': response.json()['Poster'],
        'runtime': response.json()['Runtime'],
    }

    return movie_details
