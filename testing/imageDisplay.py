import PIL
from PIL import Image
import numpy as np

#img = Image.open('felix-kozdemba.jpg')

size = (64, 64)
i = np.ones(size)
i *= 255
for y in range(size[1]):
    for x in range(size[0]):
        if y % 2:
            i[x][y] = 0

img = Image.fromarray(i)

img.show()
