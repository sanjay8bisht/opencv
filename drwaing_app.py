import numpy as np
import cv2

canvas = np.ones([500, 500, 3], 'uint8')*255

radius = 30
color = (0, 255, 0)
pressed = False


def click(event, x, y, flags, param):
    global canvas, pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(canvas, (x, y), radius, color, -1)
        pressed = True
    elif event == cv2.EVENT_MOUSEMOVE and pressed:
        cv2.circle(canvas, (x, y), radius, color, -1)
    elif event == cv2.EVENT_LBUTTONUP:
        pressed = False

cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas", click)

while True:

    cv2.imshow("canvas", canvas)

    k = cv2.waitKey(1)

    if k & 0xFF == 27:
        break
    elif k & 0xFF == ord('b'):
        color = (255, 0, 0)
    elif k & 0xFF == ord('r'):
        color = (0, 0, 255)


cv2.destroyAllWindows()