#!/usr/bin/env python3
import search
import sys
import getopt
import inquirer
from pprint import pprint
from colorama import init, Fore

# Initialize colorama
init()


def help():
    print(f"""

{Fore.RED}mvc - movie recommender

{Fore.BLUE}Usage:

    {Fore.RED}-h{Fore.RESET}                    {Fore.BLUE}show help
    {Fore.RED}-s|--search {Fore.GREEN}<title>   {Fore.BLUE}search for a movie
    {Fore.RED}-t|--top{Fore.RESET}              {Fore.BLUE}choose from top movies

{Fore.BLUE}Examples:

    {Fore.RED}mvc -h{Fore.RESET}
    {Fore.RED}mvc -s {Fore.GREEN}"The Matrix"
    {Fore.RED}mvc -t{Fore.RESET}

{Fore.RESET}""")


def print_search(query):
    movie = search.search_movie(query)
    movie_title = movie[0]
    movie_plot = movie[1]
    movie_genre = movie[2]

    try:
        print(f"\n\n{Fore.RED}{movie_title}{Fore.RESET} - {movie_genre[0]}, {movie_genre[1]}")
    except:
        print(f"\n\n{Fore.RED}{movie_title}{Fore.RESET} - {movie_genre[0]}")

    print(f"\n\n{movie_plot[0]}\n\n")

    try:
        print(f"{movie_plot[1]}\n\n")
    except:
        return 0


def choose_from_top():
    top = search.get_top()

    movies = [
        inquirer.List(
            "result",
            message=f"{Fore.RED}Choose a movie",
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
