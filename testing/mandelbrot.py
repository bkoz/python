import PIL
from PIL import Image
import numpy as np
import random

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
	colorMap = buildColorMapGradient((0, 0, 255), (255, 255, 255))

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