# Write code using zip and filter so that these lists (l1 and l2) are combined into one 
# big list and assigned to the variable opposites if they are both longer than 3 characters each.
#
# Expected: [('left', 'right'), ('front', 'back)]
#
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
big_list = []
l = list(zip(l1, l2))
for pair in list(zip(l1, l2)):
    print(pair)
    if len(pair[0]) > 3 and len(pair[1]) > 3:
        big_list.append(pair)

opposites = list(filter(lambda word: len(word[0]) > 3 and len(word[1]) > 3, list(zip(l1, l2))))

print('l=', l)
print('big=', big_list)
print('opposites =', opposites)

# Below, we have provided a species list and a population list. Use zip to combine these 
# lists into one list of tuples called pop_info. From this list, create a new list called 
# endangered that contains the names of species whose populations are below 2500.


species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']

population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]

pop_info = list(zip(species, population))
print('\n')
print(pop_info)
print('\n')
# e = list(filter(lambda animal: animal[1] < 2500, pop_info))
# endangered = []
# for a in e:
#     endangered.append(a[0])
#
# The textbook complained about a 'filter' error, however, the grader did not seem to care.
#
endangered = [ a[0] for a in filter(lambda animal: animal[1] < 2500, pop_info) ]

print(endangered)