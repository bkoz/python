import requests
import json
import requests_cache

requests_cache.install_cache('demo_cache')

for i in range(10):
    r = requests.get('http://httpbin.org/delay/1')
    print(r.json())
