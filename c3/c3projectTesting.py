import requests
import requests_cache
import json

def get_movies_from_tastedive(movie):
    baseurl = "https://tastedive.com/api/similar"
    params_diction = {} # Set up an empty dictionary for query parameters
    params_diction["q"] = movie
    # The type=movies is not consistent with the api docs.
    # It specifies singular, (i.e. type=movie)
    params_diction["type"] = "movies"
    params_diction["limit"] = 5 # get at most 5 results
    params_diction["k"] = '350179-umichpyt-IXUEPCY9'
    resp = requests.get(baseurl, params=params_diction)    
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
def get_movie_data(title):
    baseurl = "https://www.omdbapi.com"
    params_diction = {} # Set up an empty dictionary for query parameters
    params_diction["t"] = title
    params_diction["r"] = "json"
    params_diction["apikey"] = "68415c82"
    #print(params_diction)
    resp = requests.get(baseurl, params=params_diction)    
    #print('url:',resp.url)
    #print('text:',resp.text)
    #return resp.json()
    d = resp.json()
    return d

def get_movie_rating(diction):
    #print(json.dumps(dict, indent = 2))
    rating = 0
    for source in diction['Ratings']:
        if source['Source'] == 'Rotten Tomatoes':
            rating = int(source['Value'][:-1])       
    return rating


def get_sorted_recommendations(titleList):
    ratedDict = {}
    #print('titleList =', titleList)
    relatedTitlesList = get_related_titles(titleList)
    for relatedTitle in relatedTitlesList:
        movieData = get_movie_data(relatedTitle)
        if movieData['Response'] == 'True':
            movieRating = get_movie_rating(movieData)
            ratedDict[relatedTitle] = movieRating
    
    kys = ratedDict.keys()
    sortedTitles = sorted(kys, reverse = True, key = lambda x: ratedDict[x])
    
    return sortedTitles

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
print(get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"]))


