#
# Python sandbox
#

mystr = "Hello there python!"

for i, j in enumerate(mystr):
    print(i, j)

print('A string and 2 vars, {0}, {1}, {2}'.format("a", "b", mystr))

print('Plural test...')
words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
print('Original list = ', words)

past_tense = list()
for i, word in enumerate(words):
    if word[-1] == 'e':
        word += 'd'
    else:
        word += 'ed'
    past_tense += [word]

print('Past tense list = ', past_tense)

sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
same_letter_count = 0
for i, j in enumerate(sentence.split()):
    if j[0] == j[-1]:
        same_letter_count += 1

print(same_letter_count)

s = "ball"
r = ""
for item in s:
   r = item.upper() + r
print(r)

