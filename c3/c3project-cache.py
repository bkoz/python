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
