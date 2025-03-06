import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r"c:\Users\SAHYADRI\Pictures\Saved Pictures\taxture-scenery-poster.jpg")  
plt.imshow(img)
width = 500
height = 400
resized_image = cv2.resize(img, (width, height))

# Save the resized image
cv2.imwrite('resized_image.jpg', resized_image)

# Display resized image
plt.imshow(resized_image)  # Convert BGR to RGB for proper display
plt.show()
h, w, _ = resized_image.shape
halfheight, halfwidth = h // 2, w // 2

TopLeft = resized_image[:halfheight, :halfwidth]
TopRight = resized_image[:halfheight, halfwidth:]
BottomLeft = resized_image[halfheight:, :halfwidth]
BottomRight = resized_image[halfheight:, halfwidth:]


cv2.imshow('resized Image',resized_image)
cv2.imshow('Top Left ', TopLeft)
cv2.imshow('Top Right ', TopRight)
cv2.imshow('Bottom Left ', BottomLeft)
cv2.imshow('Bottom Right', BottomRight)

cv2.waitKey(0)
cv2.destroyAllWindows()