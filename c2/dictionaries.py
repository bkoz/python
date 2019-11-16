#
# Week 2 - Dictionaries
#

#
# Write code to find out how many lines are in the file emotion_words.txt as shown above. 
# Save this value to the variable num_lines. Do not use the len method.
#
baseDir='/Users/koz/src/github/python/'

print('while loop ...')
filename = baseDir + 'squared_numbers.txt'
fname = "squared_numbers.txt"
with open(fname, 'r') as lines: 
    for lin in lines:                     
        print(lin)

#
# Read CSV files.
#
print('Read CSV files ...\n')
fileconnection = open(baseDir + "olympics.csv", 'r')
lines = fileconnection.readlines()
header = lines[0]
field_names = header.strip().split(',')
print(field_names)
for row in lines[1:]:
    vals = row.strip().split(',')  # First split is to remove \n
    if vals[5] != "NA":
        print("{} {} {}".format(
                vals[0],
                vals[4],
                vals[5]))

places = {"Australia":2000, "Greece":2004, "China":2008, "England":2012}

places['Brazil'] = 2016
print(places)

print('\nCounting occurences of words in a dictionary ...\n')
sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
sentence = "what can I do"
words = sentence.split()
word_counts = {}
for word in words:
    if word not in word_counts:
        # we have not seen this character before, so initialize a counter for it
        word_counts[word] = 0

    #whether we've seen it before or not, increment its counter
    word_counts[word] = word_counts[word] + 1

char_d = {}
for c in word_counts.keys():
    print(c + ": " + str(word_counts[c]) + " occurrences")
    char_d[c] = word_counts[c]
print(char_d)

print('\nLetter counts ...\n')
stri = "what can I do"
letter_counts = {} # start with an empty dictionary
for c in stri:
    if c not in letter_counts:
        # we have not seen this character before, so initialize a counter for it
        letter_counts[c] = 0

    #whether we've seen it before or not, increment its counter
    letter_counts[c] = letter_counts[c] + 1

char_d = {}
for c in letter_counts.keys():
    print(c + ": " + str(letter_counts[c]) + " occurrences")
    char_d[c] = letter_counts[c]
print(char_d)

print('\nmax value ...\n')
#
# Write a program that finds the key in a dictionary that has the maximum value. 
# If two keys have the same maximum value, it’s OK to print out either one. 
#
d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}
ks = d.keys()
best_key_so_far = list(ks)[0]  # Have to turn ks into a real list before using [] to select an item
for k in ks:
    if d[k] > d[best_key_so_far]:
        best_key_so_far = k

print("key " + best_key_so_far + " has the highest value, " + str(d[best_key_so_far]))

print('\n min_value ...\n')
placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
letter_counts = {} # start with an empty dictionary
for c in placement:
    if c not in letter_counts:
        # we have not seen this character before, so initialize a counter for it
        letter_counts[c] = 0

    #whether we've seen it before or not, increment its counter
    letter_counts[c] = letter_counts[c] + 1

ks = letter_counts.keys()
d = {}
min_value = list(ks)[0]

for c in letter_counts.keys():
    d[c] = letter_counts[c]
    if d[c] < d[min_value]:
        min_value = c
print('min_value = ', min_value, "val = ", d[min_value])

print('\nmax_value ...\n')
product = "iphone and android phones"
letter_counts = {} # start with an empty dictionary
for c in product:
    if c not in letter_counts:
        # we have not seen this character before, so initialize a counter for it
        letter_counts[c] = 0

    #whether we've seen it before or not, increment its counter
    letter_counts[c] = letter_counts[c] + 1

ks = letter_counts.keys()
lett_d = {}
max_value = list(ks)[0]

for c in letter_counts.keys():
    lett_d[c] = letter_counts[c]
    if lett_d[c] > lett_d[max_value]:
        max_value = c

print('max_value = ', max_value, "val = ", lett_d[max_value])

print('\nLetter counts ...\n')
string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
lstring = string1.lower()
letter_counts = {} # start with an empty dictionary
for c in lstring:
    if c not in letter_counts:
        # we have not seen this character before, so initialize a counter for it
        letter_counts[c] = 0

    #whether we've seen it before or not, increment its counter
    letter_counts[c] = letter_counts[c] + 1

print(string1.lower())
print(letter_counts)