#
# Question 1
#
import requests_with_caching

def get_movies_from_tastedive(movie):
    baseurl = "https://tastedive.com/api/similar"
    params_diction = {} # Set up an empty dictionary for query parameters
    params_diction["q"] = movie
    # The type=movies is not consistent with the api docs.
    # It specifies singular, (i.e. type=movie)
    params_diction["type"] = "movies"
    params_diction["limit"] = 5 # get at most 5 results
    resp = requests_with_caching.get(baseurl, params=params_diction)    
    return resp.json()  

get_movies_from_tastedive("Bridesmaids")
get_movies_from_tastedive("Black Panther")

#
# Question 2
#
import requests_with_caching

def get_movies_from_tastedive(movie):
    baseurl = "https://tastedive.com/api/similar"
    params_diction = {} # Set up an empty dictionary for query parameters
    params_diction["q"] = movie
    # The type=movies is not consistent with the api docs.
    # It specifies singular, (i.e. type=movie)
    params_diction["type"] = "movies"
    params_diction["limit"] = 5 # get at most 5 results
    resp = requests_with_caching.get(baseurl, params=params_diction)    
    return resp.json()  

def extract_movie_titles(dict):
    movies = []
    for movie in dict['Similar']['Results']:
        movies.append(movie['Name'])
    return movies

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# extract_movie_titles(get_movies_from_tastedive("Tony Bennett")) 
# extract_movie_titles(get_movies_from_tastedive("Black Panther"))

#
# Question 3
#
import requests_with_caching

def get_movies_from_tastedive(movie):
    baseurl = "https://tastedive.com/api/similar"
    params_diction = {} # Set up an empty dictionary for query parameters
    params_diction["q"] = movie
    # The type=movies is not consistent with the api docs.
    # It specifies singular, (i.e. type=movie)
    params_diction["type"] = "movies"
    params_diction["limit"] = 5 # get at most 5 results
    resp = requests_with_caching.get(baseurl, params=params_diction)    
    return resp.json()  

def extract_movie_titles(dict):
    movies = []
    for movie in dict['Similar']['Results']:
        movies.append(movie['Name'])
    return movies

def get_related_titles(movieList):
    relatedTitles = []
    for movie in movieList:
        relatedTitleList = extract_movie_titles(get_movies_from_tastedive(movie))
        for title in relatedTitleList:
            if title not in relatedTitles:
                relatedTitles.append(title) 
    return relatedTitles

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# extract_movie_titles(get_movies_from_tastedive("Tony Bennett")) 
# extract_movie_titles(get_movies_from_tastedive("Black Panther"))


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_related_titles(["Black Panther", "Captain Marvel"])
# get_related_titles([])


