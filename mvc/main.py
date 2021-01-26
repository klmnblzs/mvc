#!/usr/bin/env python3
import search
import sys
import getopt
import inquirer
from pprint import pprint

# pip install inquirer


def help():
    print(f"""

Usage:
    -h          show help
    -s <title>  search for a movie

""")


def print_search(query):
    movie = search.search_movie(query)
    movie_title = movie[0]
    movie_plot = movie[1]
    movie_genre = movie[2]

    if movie[2][1]:
        print(f"\n\n{movie_title} - {movie_genre[0]}, {movie_genre[1]}")
    else:
        print(f"\n\n{movie_title} - {movie_genre[0]}")
    print(f"\n\n{movie_plot[0]}\n\n")
    if movie_plot[1]:
        print(f"{movie_plot[1]}\n\n")


def choose_from_top():
    top = search.get_top()

    movies = [
        inquirer.List(
            "result",
            message="Choose a movie:",
            choices=top,
        ),
    ]

    title = inquirer.prompt(movies)
    query = str(title["result"])
    print_search(query)


def main():
    try:
        options, value = getopt.getopt(sys.argv[1:], 'hs:t', ["help", "search", "top"])

        for opt, arg in options:

            if opt in ("-h" or "--help"):
                help()

            elif opt in ("-s" or "--search"):
                print_search(arg)

            elif opt in ("-t" or "--top"):
                choose_from_top()

            else:
                help()

    except getopt.error:
        help()

    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()
