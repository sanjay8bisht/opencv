import cv2
import numpy as np

color = cv2.imread("/home/sanjay/Downloads/output.jpg")
cv2.imshow("Image", color)
cv2.moveWindow("Image", 0, 0)
print(color.shape)
height, width, channel = color.shape
b, g, r = cv2.split(color)

rgb_split = np.empty([height, width*3, 3], 'uint8')

rgb_split[:, 0:width] = cv2.merge([b, b, b])
rgb_split[:, width:width*2] = cv2.merge([g, g, g])
rgb_split[:, width*2:width*3] = cv2.merge([r, r, r])

cv2.imshow("Channel", rgb_split)
cv2.moveWindow("Channel", 0, height)

hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
hsv_split = np.concatenate((h, s, v), axis=1)

cv2.imshow("HSV Split", hsv_split)
cv2.moveWindow("HSV Split", 0, 0)

cv2.waitKey(0)
cv2.destroyAllWindows()
