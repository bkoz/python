import requests
import requests_cache
import json

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

j = get_movie_data('John Wick')
print(json.dumps(j, indent=4))