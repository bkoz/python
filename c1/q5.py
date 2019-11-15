# Question 5 - Formatting
#
# Print out each item in the list with the same formatting, using the .format 
# method (not string concatenation). For example, the first print statment 
# should read: The store has 12 shoes, each for 29.99 USD.
inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

for item in inventory:
    i = item.split(',')
    print('The store has{} {}, each for{} USD.'.format(i[1], i[0], i[2]))
