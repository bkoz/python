import json

filename = '/Users/bkozdemb/src/github.com/python/c3/sample.json'
fd = open(filename, 'r')
d = json.load(fd)
print('---------')
print(d)
print('---------')

for item in d:
     print(d[item])

print('---------')
d = {'Fred': 44, 'Ella': 31}

filename = '/Users/bkozdemb/src/github.com/python/c3/tmp.json'
fd = open(filename, 'w')
json.dump(d, fd)
fd.close()

print('---------')
a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
print(a_string)
d = json.loads(a_string)
print("------")
print(type(d))
print(d.keys())
print(d['resultCount'])
# print(a_string['resultCount'])
