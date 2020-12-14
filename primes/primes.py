#
# Calculate prime numbers (not working just yet). :)
#
def isPrime(x):
    for i in range(x-1):
        if (i > 1):
            r = x % i
            print(x, '%', i, ':', r)
            if (r == 0):
                break
    if (r > 1):
        return True
    else:
        return False

n = 11
isPrime(3)
#for i in range(2, n):
#  if isPrime(i) == True:
#    print(i)
