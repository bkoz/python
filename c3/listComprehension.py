#
# Extract all the names.
#
tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
for n in tester['info']:
    print(n['name'])
compri = [n['name'] for n in tester['info']]

#
# Extract numbers > 10
#
L = [12, 34, 21, 4, 6, 9, 42]
lst = []
for x in L:
    if x > 10:
        lst.append(x)
print(lst)

lst2 = [num for num in L if num > 10]

#
# Below we have provided two lists of numbers, L1 and L2. Using zip and list comprehension, 
# create a new list, L3, that sums the two numbers if the number from L1 is greater than 10 and 
# the number from L2 is less than 5. This can be accomplished in one line of code.
#
print('-------------')
L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

print('L1=', L1)
print('L2=', L2)
L3 = []
for (x1, x2) in list(zip(L1, L2)):
    if x1 > 10 and x2 < 5:
        L3.append(x1 + x2)
print('L3 =', L3)

#
# List comprehension
# [<transformer_expression> for <loop_var> in <sequence> if <filtration_expression>]
#
L3 = [ x1 + x2 for (x1, x2) in list(zip(L1, L2)) if x1 > 10 and x2 < 5 ]
print('L3 =', L3)
