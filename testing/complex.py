#
# Experiment with the numpy complex data type.
#
import cmath
import random

a = complex('(2+j)')
b = complex(3, 1)
z = complex()

print('z = {}, z^2 + 5 = {}'.format(z, (z**2) + 5))
print('{} + {} = {}'.format(a, b, a + b))
print('{} * {} = {}'.format(a, b, a * b))

print('Random number between 0 and 15 = ', random.randrange(0, 15))
