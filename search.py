from imdb import IMDb
import os
import sys
import getopt
import json


#with open('storage/userdata.json', 'r') as f:
#    data_storage = json.load(f)

#tmdb.api_key = data_storage['api_key']

ia=IMDb()

def search_movie(name):
    search = ia.search_movie(name)
    movie = ia.get_movie(search[0].movieID)
    actor = movie['cast']

    print("MOVIE NAME -----------")
    print(movie['title'])
    print("\n")

    print("PLOT -----------")
    print(movie['plot'])
    print("\n")

    print("ACTORS ---------\n")
    for i in actor:    
        print(i, end=", ")
    print("\n\n")

    #print(actor)

search_movie("Inception")