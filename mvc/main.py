#!/usr/bin/env python3
import search
import sys
import getopt


def help():
    print(f"""

Usage:
    -h          show help
    -s <title>  search for a movie

""")


def main():
    try:
        options, value = getopt.getopt(sys.argv[1:], 'hs:', ['help', 'search'])

        for opt, arg in options:

            if opt in ("-h" or "--help"):
                help()

            elif opt in ("-s" or "--search"):
                movie = search.search_movie(arg)
                movie_title = movie[0]
                movie_plot = movie[1]


                print(f"\n\n{movie_title}")
                print(f"\n\n{movie_plot[0]}\n\n")
                if movie_plot[1]:
                    print(f"{movie_plot[1]}\n\n")

                # movie_actors = movie[2]
                # for actor in movie_actors:
                #     print(actor, end=", ")

            else:
                print("Help (ELSE)")

    except getopt.error:
        help()

    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()
