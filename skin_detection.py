import numpy as np
import cv2

faces = cv2.imread("/home/sanjay/Downloads/faces_copy.jpeg", 1)
faces = cv2.resize(faces, (0, 0), fx=0.3, fy=0.3)
hsv = cv2.cvtColor(faces, cv2.COLOR_BGR2HSV)
h = hsv[:, :, 0]
s = hsv[:, :, 1]
v = hsv[:, :, 2]

hsv_split = np.concatenate((h, s, v), axis=1)

cv2.imshow("HSV Faces", hsv_split)

# everything above 40 will be white
ret, min_sat = cv2.threshold(s, 40, 255, cv2.THRESH_BINARY)
cv2.imshow("Min saturation", min_sat)

# everything above 15 will be black
ret, max_hue = cv2.threshold(h, 15, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Max Hue", max_hue)

final = cv2.bitwise_and(min_sat, max_hue)
cv2.imshow("Final", final)

cv2.waitKey(0)
cv2.destroyAllWindows()