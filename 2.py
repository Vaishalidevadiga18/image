import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread(r'c:\Users\SAHYADRI\Pictures\Saved Pictures\taxture-scenery-poster.jpg')

width = 300
height = 200


resized_image = cv2.resize(img, (width, height))



cv2.imwrite('resized_image.jpg', resized_image)
plt.imshow(resized_image)
plt.show()
h, w, _ = resized_image.shape

halfheight, halfwidth = h // 2, w // 2

TopLeft = resized_image[:halfheight, :halfwidth]
TopRight = resized_image[:halfheight, halfwidth:]
BottomLeft = resized_image[halfheight:, :halfwidth]
BottomRight = resized_image[halfheight:, halfwidth:]

cv2.imwrite('Top Left.jpg ', TopLeft)
plt.imshow(TopLeft)
plt.show()

cv2.imwrite('Top Right.jpg', TopRight)
plt.imshow(TopRight)
plt.show()

cv2.imwrite('Bottom Left.jpg', BottomLeft)
plt.imshow(BottomLeft)
plt.show()

cv2.imwrite('Bottom Right.jpg', BottomRight)

plt.imshow(BottomRight)
plt.show()





