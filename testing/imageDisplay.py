import PIL
from PIL import Image
import numpy as np

#img = Image.open('felix-kozdemba.jpg')

size = (64, 64, 3)
i = np.zeros(size, dtype=np.int8)
for y in range(size[1]):
    for x in range(size[0]):
        if y % 2:
            i[y][x][0] = 255
            i[y][x][1] = 0
            i[y][x][2] = 0

# i[0][31][0] = 255
# i[0][31][1] = 255
# i[0][31][2] = 255

img = Image.fromarray(i, mode='RGB')

img.show()
