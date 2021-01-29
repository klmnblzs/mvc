#!/usr/bin/env python3
from imdb import IMDb
import requests
from dataclasses import dataclass

ia=IMDb()
api_url = 'http://www.omdbapi.com/'


def get_top():
    """
    Get top 250 movies from imdb
    Returns: list of movies
    """
    top = ia.get_top250_movies()

    return top


@dataclass
class Movie:
    title: str
    api_key: str
    plot: str = None

    def __post_init__(self):
        payload = {'t': self.title, 'plot': self.plot, 'r': 'json', 'apikey': self.api_key}
        self.values = requests.get(api_url, params=payload).json()

    def get_all_data(self):
        values = self.values if self.values['Response'] == 'True' else self.values['Error']
        return values

    def get_data(self, *args):
        items = {item: self.values.get(item, 'key not found!') for item in args}

        return items
