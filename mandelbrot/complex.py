#
# Experiment with the complex number data type.
#
import cmath
import random

a = complex('(2+j)')
b = complex(3, 1)
z = complex()

print('{} + {} = {}'.format(a, b, a + b))
# (2+i)(3+i) = 5+5i.
print('{} * {} = {}'.format(a, b, a * b))
print('z = {}, z^2 + 5 = {}'.format(z, (z**2) + 5))

n = random.randrange(0, 15)
print('Random number between 0 and 15 = ', n)
