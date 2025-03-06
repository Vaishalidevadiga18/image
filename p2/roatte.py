
import cv2
import numpy as np


img = cv2.imread('scene.jpg')

if img is None:
    print("Error: Image not found")
    exit()


height, width = img.shape[:2]


center = ( height // 2,width // 2)
angle = 90 
scale = 1.0 
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
rotated= cv2.warpAffine(img, rotation_matrix, (width, height))


scale_factor = 0.5
scaled= cv2.resize(img, None, fx=scale_factor, fy=scale_factor)


tx, ty = 50, 50 
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
translated = cv2.warpAffine(img, translation_matrix, (width, height))


cv2.imshow('Original Image', img)
cv2.imshow('Rotated Image', rotated)
cv2.imshow('Scaled Image', scaled)
cv2.imshow('Translated Image', translated)


cv2.waitKey(0)

    