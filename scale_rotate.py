import numpy as np
import cv2

image = cv2.imread("/home/sanjay/Downloads/output.jpg", 1)

# scale
img_half = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
img_stretch = cv2.resize(image, (800, 800))
img_stretch_near = cv2.resize(image, (800, 800), interpolation=cv2.INTER_NEAREST)

cv2.imshow("Half", img_half)
cv2.imshow("Stretch", img_stretch)
cv2.imshow("Stretch near", img_stretch_near)

# Rotation
M = cv2.getRotationMatrix2D((image.shape[1]/2, image.shape[0]/2), 45, 1)
rotated = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("rotated", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()