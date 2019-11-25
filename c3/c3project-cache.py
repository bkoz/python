#
# Questions 1 through 3.
#
import requests
import requests_cache
import json

# Install requests_cache with no expiration.
requests_cache.install_cache('requests_cache', expire_after=None)

#
# Question 3
#

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
# print(get_related_titles(["Black Panther"]))
# print(get_related_titles(["Black Panther", "Captain Marvel"]))
# get_related_titles([])

# 
# Question 4
#
def get_movie_data(title):
#http://www.omdbapi.com/?apikey=68415c82&type=movie&t=John+Wick
    baseurl = "http://www.omdbapi.com"
    params_diction = {} # Set up an empty dictionary for query parameters
    params_diction['t'] = title
    params_diction['r'] = 'json'
    params_diction['apikey'] = '68415c82'
    resp = requests.get(baseurl, params=params_diction)    
    return resp.json()  

    
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# print('\nQuestion 4 -----------------------------------------------\n')
# print(get_movie_data("Black Panther"))
# get_movie_data("Baby Mama")

#
# Question 5
#
# Write a function called get_movie_rating. It takes an OMDB dictionary result for 
# one movie and extracts the Rotten Tomatoes rating as an integer. For example, 
# if given the OMDB dictionary for “Black Panther”, it would return 97. If there 
# is no Rotten Tomatoes rating, return 0.
def get_movie_rating(dict):
    # print(json.dumps(dict, indent = 2))
    rating = 0
    for source in dict['Ratings']:
        if source['Source'] == 'Rotten Tomatoes':
            rating = int(source['Value'][:-1])       
    return rating

print('\nQuestion 5 -----------------------------------------------\n')
print(get_movie_rating(get_movie_data("Black Panther")))
print(get_movie_rating(get_movie_data("Sherlock Holmes")))
print(get_movie_rating(get_movie_data("Finding Nemo")))


#
# Question 6
#
# Define a function get_sorted_recommendations. It takes a list of movie titles 
# as an input. It returns a sorted list of related movie titles as output, up 
# to five related movies for each input movie title. The movies should be sorted 
# in descending order by their Rotten Tomatoes rating, as returned by the 
# get_movie_rating function. Break ties in reverse alphabetic order, so that 
# ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.

def get_sorted_recommendations(titleList):
    sortedTitleList = []
    ratedDict = {}
    #print('titleList = ', titleList)
    for title in titleList:
        #print('title =', title)
        relatedTitlesList = get_related_titles(title)
        for relatedTitle in relatedTitlesList:
            movieData = get_movie_data(relatedTitle)
            #print('relatedTitle =', relatedTitle, 'movieData = ', movieData)
            if movieData['Response'] == 'True':
                movieRating = get_movie_rating(movieData)
                sortedTitleList.append(relatedTitle)
                ratedDict[relatedTitle] = movieRating
    kys = ratedDict.keys()
    sorted_values = sorted(kys, reverse = True, key = lambda x: ratedDict[x])
    #print('sortedValues =', sorted_values)
    
    return sorted_values

print('\nQuestion 6 -----------------------------------------------\n')
#print(get_movies_from_tastedive('Black Panther'))
# print(get_movie_data("Death Race"))

print(get_sorted_recommendations(["Black Panther", "Bridesmaids"]))
#print(get_sorted_recommendations(["Black Panther"]))
#print(get_sorted_recommendations(["Sherlock Holmes"]))
# #print(get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"]))