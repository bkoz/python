import PIL
from PIL import Image
import numpy as np

#img = Image.open('felix-kozdemba.jpg')

def buildColorMap():
    i = 0
    cmap = {}
    for r in range(8):
        for g in range(8):
            for b in range(4):
                cmap[i] = (int(r/7*255), int(g/7*255), int(b/3*255))
                i += 1
    return cmap

size = (256, 256, 3)
cm = buildColorMap()
i = np.zeros(size, dtype=np.int8)
for y in range(size[1]):
    for x in range(size[0]):
            i[y][x] = cm[y]
            
# i[0][31][0] = 255
# i[0][31][1] = 255
# i[0][31][2] = 255

img = Image.fromarray(i, mode='RGB')

img.show()
