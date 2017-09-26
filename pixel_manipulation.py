import numpy as np
import cv2

color = cv2.imread("/home/sanjay/Downloads/output.jpg", 1)

gray = cv2.cvtColor(color, cv2.COLOR_RGB2GRAY)

b = color[:, :, 0]
g = color[:, :, 1]
r = color[:, :, 2]

rgba = cv2.merge((b, g, r, g))

cv2.imshow("rgba", rgba)

cv2.imwrite("/home/sanjay/Downloads/rgba.png", rgba)

cv2.waitKey(0)
cv2.destroyAllWindows()
