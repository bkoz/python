#
# Question 1 - No caching version
#
import requests
#import requests_with_caching

def get_movies_from_tastedive(movie):
    baseurl = "https://tastedive.com/api/similar"
    params_diction = {} # Set up an empty dictionary for query parameters
    params_diction["q"] = movie
    params_diction["type"] = "movie"
    params_diction["limit"] = "5" # get at most 5 results
    params_diction["k"] = "350179-umichpyt-IXUEPCY9"
    #resp = requests_with_caching.get(baseurl, params=params_diction)    
    resp = requests.get(baseurl, params=params_diction)    
#    print('resp.url =', resp.url)
#    print('resp.text =', resp.text)
    print(resp.json())
    return resp.json()  
# get_movies_from_tastedive("Bridesmaids")
print('----------\n')
d = get_movies_from_tastedive("Black Panther")
print('----------\n')
#print(d['Similar']['Results'][0]['Name'])
for movie in d['Similar']['Results']:
    print(movie['Name'])

