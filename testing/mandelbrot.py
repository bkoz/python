import PIL
from PIL import Image
import numpy as np
import random

#img = Image.open('felix-kozdemba.jpg')

# size = (64, 64)
# i = np.ones(size)
# i *= 255
# for y in range(size[1]):
#     for x in range(size[0]):
#         if y % 2:
#             i[x][y] = 0

# img = Image.fromarray(i)

# img.show()

def buildColorMapGradient():
    cmap = {}
    for i in range(256):
        #cmap[i] = (int(r/7*255), int(g/7*255), int(b/3*255))
        cmap[i] = (i, i, 255 - i)

    return cmap

def buildColorMap():
    i = 0
    cmap = {}
    for r in range(8):
        for g in range(8):
            for b in range(4):
                cmap[i] = (int(r/7*255), int(g/7*255), int(b/3*255))
                i += 1
    return cmap

# Mandelbrot - Calculates and returns an image of the Mandelbrot fractal.
def createImage(width, height):
	size = (width, height, 3)
	xmin = -2 
	ymin = -2 
	xmax = 2
	ymax = 2
	
	c = random.randrange(0, 15)
	print("createImage: contrast = ", c)
	img = np.zeros(size, dtype=np.int8)
	colorMap = buildColorMapGradient()

	for py in range(height):
		y = float(py)/float(height)*(ymax-ymin) + ymin
		for px in range(width):
			x = float(px)/float(width)*(xmax-xmin) + xmin
			z = complex(x, y)
			# Image point (px, py) represents complex value z.
			pixel = mandelbrot(z, c)
			if pixel < 0:
				pixel = 0
			img[py][px] = colorMap[pixel]
			
	return img

#
# mandelbrot - Compute and return the pixel.
#             
def mandelbrot(z, contrast):
	"""
	:param z: A complex number
	:param contrast: One of 16 contrast levels (int)
	"""
	iterations = 200
	v = complex()
	inTheSet = 0

	for n in range(iterations):
		v = v*v + z
		# cmplx.Abs returns the absolute value (also called the modulus) of x.
        # func Abs(x complex128) float64 { return math.Hypot(real(x), imag(x)) }
		if complex.__abs__(v) > 2:
			return 255 - (contrast * n)

	return inTheSet

image = Image.fromarray(createImage(1024, 1024), mode='RGB')
image.show()