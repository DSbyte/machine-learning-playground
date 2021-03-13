import cv2
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt


image = misc.ascent()

# plt.grid(False)
# plt.gray()
# plt.axis('off')
# plt.imshow(image)
# plt.show()

transformed_image = np.copy(image)
size_x = transformed_image.shape[0]
size_y = transformed_image.shape[1]

filter = [ [-1, -2, -1], [0, 0, 0], [1, 2, 1] ]
weight = 1

for x in range(1, size_x-1):
    for y in range(1, size_y-1):
        op_pixel = 0.0
        op_pixel += (image[x - 1, y - 1] * filter[0][0])
        op_pixel += (image[x, y - 1] * filter[0][1])
        op_pixel += (image[x + 1, y - 1] * filter[0][2])
        op_pixel += (image[x - 1, y] * filter[1][0])
        op_pixel += (image[x, y] * filter[1][1])
        op_pixel += (image[x + 1, y] * filter[1][2])
        op_pixel += (image[x - 1, y + 1] * filter[2][0])
        op_pixel += (image[x, y + 1] * filter[2][1])
        op_pixel += (image[x + 1, y + 1] * filter[2][2])

        op_pixel *= weight

        if (op_pixel < 0):
            op_pixel = 0
        elif (op_pixel > 255):
            op_pixel = 255
        
        transformed_image[x, y] = op_pixel

new_x = int(size_x/2)
new_y = int(size_y/2)

newImage = np.zeros((new_x, new_y))
for x in range(0, size_x, 2):
    for y in range(0, size_y, 2):
        pixels = []
        pixels.append(transformed_image[x, y])
        pixels.append(transformed_image[x+1, y])
        pixels.append(transformed_image[x, y+1])
        pixels.append(transformed_image[x+1, y+1])
        pixels.sort(reverse=True)
        newImage[int(x/2), int(y/2)] = pixels[0]

plt.grid(False)
plt.gray()
plt.imshow(newImage)
plt.show()