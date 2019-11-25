letters = "alwnfiwaksuezlaeiajsdl"
sorted_letters = sorted(letters, reverse = True)

#

animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']
animals_sorted = sorted(animals)

#

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
alphabetical = sorted(medals)

#

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
def getVal(m):
    return medals[m]

s = sorted(medals, key = getVal, reverse = True)
#print(s)
top_three = []
for i in range(3):
    top_three.append(s[i])
#

groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
def getVal(d):
    return groceries[d]

most_needed = []
sorted_values = sorted(groceries, reverse = True, key = getVal)
for i in sorted_values:
    most_needed.append(i)
#

def last_four(x):
    return x - 17570000

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

sorted_ids = sorted(ids, key=last_four)

#
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_id = sorted(ids, key=lambda x: x - 17570000)

#

dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}
def getVal(d):
    return dictionary[d]

#print(dictionary['Flowers'])
#print(getVal(dictionary['Flowers']))
#sorted_values = sorted(dictionary, reverse = True, key = getVal)
ks = dictionary.keys()
print(ks)
#sorted_values = sorted(dictionary, reverse = True)
sorted_values = sorted(ks, reverse = True, key = lambda x: dictionary[x])


print('sorted_values =', sorted_values)