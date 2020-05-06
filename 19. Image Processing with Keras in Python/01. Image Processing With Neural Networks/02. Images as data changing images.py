'''
Images as data: changing images
To modify an image, you can modify the existing numbers in the array. In a color image, you can change the values in one of the color channels without affecting the other colors, by indexing on the last dimension of the array.

The image you imported in the previous exercise is available in data.

Instructions
100 XP
Modify the bricks image to replace the top left corner of the image (10 by 10 pixels) into a red square.
Visualize the resulting image.
'''
SOLUTION

# Set the red channel in this part of the image to 1
data[:10,:10, 0] = 1

# Set the green channel in this part of the image to 0
data[:10, :10, 1] = 0

# Set the blue channel in this part of the image to 0
data[:10, :10, 2] = 0

# Visualize the result
plt.imshow(data)
plt.show()