#!/usr/bin/env python3
import search
import sys
import getopt
import inquirer
from pprint import pprint
from colored import attr, fg


def help():
    print(f"""

{fg(1)}mvc - movie recommender

{fg(2)}Usage:

    {fg(3)}-h               {fg(1)}show help
    {fg(3)}-s|--search      {fg(1)}search for a movie
    {fg(3)}-t|--top         {fg(1)}choose from top movies

{fg(2)}Examples:

    {fg(3)}mvc -h
    {fg(3)}mvc -s {fg(4)}"The Matrix"
    {fg(3)}mvc -t

{fg(7)}""")


def print_search(query):
    movie = search.search_movie(query)
    title = movie["title"]
    genre = movie["genre"]
    release = movie["release"]
    plot = movie["plot"]
    rating = movie["rating"]
    poster_url = movie["poster_url"]
    runtime = movie["runtime"]

    print(f"""
 {title} ({release}) {runtime} - {genre}

 {rating}
""")
    per_line = 79
    for i in range(0, len(plot), per_line):
        print(f" {plot[i:i+per_line]}")
    print("")


def choose_from_top():
    top = search.get_top()

    movies = [
        inquirer.List(
            "result",
            message=f"{fg(1)}Choose a movie",
            choices=top,
        ),
    ]

    title = inquirer.prompt(movies)
    query = str(title["result"])
    print_search(query)


def notify(text, error=False):
    """
    Colored status wrapper
    """
    icon = f"{fg(9)}{attr(0)}" if error else f"{fg(10)}{attr(0)}"
    print(f"\n {icon} {attr(2)}{text}{attr(0)}\n")


if __name__ == "__main__":
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

        # Work around to if no arguments given simply run the main function
        # try:
        #     if sys.argv[1] is None:
        #         main()
        # except IndexError:
        #     main()

    except getopt.error:
        help()

    except KeyboardInterrupt:
        sys.exit()

    # except:
    #     help()
