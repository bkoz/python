import PIL
from PIL import Image
import numpy as np

#img = Image.open('felix-kozdemba.jpg')

def buildColorMap332():
    i = 0
    cmap = {}
    for r in range(8):
        for g in range(8):
            for b in range(4):
                cmap[i] = (int(r/7*255), int(g/7*255), int(b/3*255))
                i += 1
    return cmap

def buildColorMapGradient(fromC, toC):
    """
    Linear Interpolate between 2 colors.
    
    Param: fromC: The from color rgb tuple
    Param: toC: The to color rgb tuple
    Returns: A colormap dictionary
    """
    cmap = {}
    ranges = [0, 1, 2]

    for i in range(3):
        ranges[i] = toC[i] - fromC[i]

    for i in range(256):
        cmap[i] = (int(fromC[0] + ranges[0] * i/255),
        int(fromC[1] + ranges[1]*i/255),
        int(fromC[2]+ranges[2]*i/255))
     
    return cmap

#
# Main
#
size = (256, 256, 3)
fromC=(0, 0, 255)
toC=(255, 255, 255)
cm = buildColorMapGradient(fromC, toC)
i = np.zeros(size, dtype=np.int8)
for y in range(size[1]):
    for x in range(size[0]):
            i[y][x] = cm[y]
            
img = Image.fromarray(i, mode='RGB')
img.show()
