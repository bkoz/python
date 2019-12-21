import PIL
from PIL import Image
import numpy as np

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

# Mandelbrot - Calculates and returns an image of the Mandelbrot fractal.
def createImage(width, height):
    size = (width, height)
    xmin = -2 
    ymin = -2 
    xmax = 2
    ymax = 2

	c = random.randrange(0, 15)
	print("createImage: contrast = ", c)

    img = np.zeros(size)

	for py in range(height):
		y = float(py)/float64(height)*(ymax-ymin) + ymin
		for px in range(width):
			x = float(px)/float64(width)*(xmax-xmin) + xmin
			z = complex(x, y)
			// Image point (px, py) represents complex value z.
			img[px][py] = mandelbrot(z, c)

	return img
}

#
# mandelbrot - Compute and return the pixel.
#              Implement color LUT using a go map type - key is based on 'n'?

def mandelbrot(z complex128, contrast uint8):
	"""
	:param z: A complex number
	:param contrast: One of 16 contrast levels (int)
	"""
	iterations = 200
	v = complex()
	black = 0
	white = 255

	for n in range(iterations):
		v = v*v + z
		# cmplx.Abs returns the absolute value (also called the modulus) of x.
        # func Abs(x complex128) float64 { return math.Hypot(real(x), imag(x)) }
		if cmplx.Abs(v) > 2 {
			return 255 - (contrast * n)
			#return palette.Plan9[255-contrast*n]
	return black

