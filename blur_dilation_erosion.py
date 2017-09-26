import numpy as np
import cv2

image = cv2.imread("/home/sanjay/Downloads/output.jpg", 1)
cv2.imshow("Original", image)

blur = cv2.GaussianBlur(image, (3, 33), 0)
cv2.imshow("Blur", blur)

kernel = np.ones((5, 5), 'uint8')

# turns small dark pixels to white or matching pixels like small black pixel on white background is converted to white
dilate = cv2.dilate(image, kernel, iterations=2)

# opposite of dilate
erode = cv2.erode(image, kernel, iterations=2)

cv2.imshow("Dilate", dilate)
cv2.imshow("Erode", erode)

cv2.waitKey(0)
cv2.destroyAllWindows()