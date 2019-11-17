#
#
#
d = {'x': []}
print(d)
d['x'].append('d')
d['x'].append('d')
d['x'].append('d')
print(d)
print('keys', d.keys())
print('d[x] =', d['x'])

#
#
#
def beginning(strList):
    i = 0
    retList = []
    while (strList[i] != 'bye'):
        if i < 10:
            retList.append(strList[i])
        i += 1
    return retList


#
#
#
def stop_at_four(numbers):
    newList = []
    i = 0
    while (i < len(numbers)) and (numbers[i] != 4):
        newList.append(numbers[i])
        i += 1
    return newList

print(stop_at_four([1, 6, 2, 3, 9]))
print(stop_at_four([0, 9, 4.5, 1, 7, 4, 8, 9, 3]))

#
#
#
def checkout():
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price < 0:
            pass
        elif price != 0:
            count = count + 1
            total = total + price
            print('Subtotal: $', total)
        else:
            moreItems = False
    if count > 0:
        average = total / count
        print('Total items:', count)
        print('Total $', total)
        print('Average price per item: $', average)
    else:
        print("0 items, can't calculate!")

checkout()

def get_yes_or_no(message):
    valid_input = False
    while not valid_input:
        answer = input(message)
        answer = answer.upper() # convert to upper case
        if answer == 'Y' or answer == 'N':
            valid_input = True
        else:
            print('Please enter Y for yes or N for no.')
    return answer

response = get_yes_or_no('Do you like lima beans? Y)es or N)o: ')
if response == 'Y':
    print('Great! They are very healthy.')
else:
    print('Too bad. If cooked right, they are quite tasty.')

