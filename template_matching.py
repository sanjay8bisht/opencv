import numpy as np
import cv2

template = cv2.imread("/home/sanjay/Downloads/template.jpg", 0)
frame = cv2.imread("/home/sanjay/Downloads/players.jpg", 0)

cv2.imshow("template", template)
cv2.imshow("frame", frame)

result = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print(min_val, max_val, min_loc, max_loc)

cv2.circle(result, max_loc, 15, 255, 2)

cv2.imshow("result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
