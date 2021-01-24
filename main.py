from imdb import IMDb
from search import search_movie
import os
import sys
import getopt
import json

def main():
    try:
        options, value = getopt.getopt(sys.argv[1:], 'hs', ['help', 'search'])

        for opt, arg in options:
            if opt in ("-h" or "--help"):
                print("Help (--HELP OR -H)")

            elif opt in ("-s" or "--search"):
                search.search_movie(arg)

            else:
                print("Help (ELSE)")
                
    except getopt.error:
        print("Help (GETOPT ERROR)")
    
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    try:
        if sys.argv[1] == None:
            print("Help - SYS.ARGV[1]")
        else:
            main()
    except IndexError:
        print("Help - INDEX ERROR")
        
