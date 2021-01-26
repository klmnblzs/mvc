#!/usr/bin/env python3
from imdb import IMDb

ia=IMDb()


def search_movie(name):
    """
    Search for a movie on imdb using title
    Returns: Movie title, plot, actors
    """

    search = ia.search_movie(name)
    movie = ia.get_movie(search[0].movieID)


    movie_data = []

    movie_data.append(movie["title"])
    movie_data.append(movie["plot"])
    movie_data.append(movie["genres"])

    return movie_data


def get_top():
    top = ia.get_top250_movies()

    return top
