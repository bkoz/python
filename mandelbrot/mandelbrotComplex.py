import matplotlib.pyplot as plt


def linspace(start, stop, num):
    return [start + (stop - start) / (num - 1) * k for k in range(num)]


def zeros(rows, cols):
    return [[0 for j in range(cols)] for i in range(rows)]


d = 100 # Pixel density 
n = 50 # Maximum number of iterations
maxN = -1

x = linspace(-2.5, 1.5, 4 * d + 1)
y = linspace(-1.5, 1.5, 3 * d + 1)

T = zeros(len(y), len(x))

for i, b in enumerate(y):
    for j, a in enumerate(x):
        z = complex()
        c = complex(a, b)
        for k in range(n):
            z = z * z + c
            if complex.__abs__(z) >= 2:
                T[i][j] = k + 1
                if k > maxN:
                    maxN = k
                break

plt.imshow(T, cmap=plt.cm.jet)
plt.show()
#plt.savefig('mandelbrot.png', dpi=200)
print('maxN = {}'.format(maxN))