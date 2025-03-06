import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread(r'c:\Users\SAHYADRI\Pictures\Saved Pictures\taxture-scenery-poster.jpg')

# Resize the image
width = 300
height = 200
resized_image = cv2.resize(img, (width, height))

# Save the resized image
cv2.imwrite('resized_image.jpg', resized_image)

# Display resized image
plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for proper display
plt.show()

# Get dimensions of the resized image
h, w, _ = resized_image.shape
halfheight, halfwidth = h // 2, w // 2

# Split the image into four quadrants
TopLeft = resized_image[:halfheight, :halfwidth]
TopRight = resized_image[:halfheight, halfwidth:]
BottomLeft = resized_image[halfheight:, :halfwidth]
BottomRight = resized_image[halfheight:, halfwidth:]

# Save and display the top-left quadrant
cv2.imwrite('Top_Left.jpg', TopLeft)
plt.imshow(cv2.cvtColor(TopLeft, cv2.COLOR_BGR2RGB))
plt.show()

# Save and display the top-right quadrant
cv2.imwrite('Top_Right.jpg', TopRight)
plt.imshow(cv2.cvtColor(TopRight, cv2.COLOR_BGR2RGB))
plt.show()

# Save and display the bottom-left quadrant
cv2.imwrite('Bottom_Left.jpg', BottomLeft)
plt.imshow(cv2.cvtColor(BottomLeft, cv2.COLOR_BGR2RGB))
plt.show()

# Save and display the bottom-right quadrant
cv2.imwrite('Bottom_Right.jpg', BottomRight)
plt.imshow(cv2.cvtColor(BottomRight, cv2.COLOR_BGR2RGB))
plt.show()
