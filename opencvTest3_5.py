import cv2
import numpy as np

img = cv2.imread('photo\\shudu.png')
rows, cols, ch = img.shape
y1, x1 = 0, 0
y2, x2 = 0, 0
y3, x3 = 0, 0
y4, x4 = 0, 0

# 创建回调函数
def select_point(event, x, y, flags, param):
    global y1, x1, y2, x2, y3, x3, y4, x4
    if event == cv2.EVENT_LBUTTONDOWN:
        if y1 == 0:
            y1, x1 = y, x
        elif y2 == 0:
            y2, x2 = y, x
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255))
        elif y3 == 0:
            y3, x3 = y, x
            cv2.line(img, (x1, y1), (x3, y3), (0, 0, 255))
        elif y4 == 0:
            y4, x4 = y, x
            cv2.line(img, (x3, y3), (x4, y4), (0, 0, 255))
            cv2.line(img, (x2, y2), (x4, y4), (0, 0, 255))


cv2.namedWindow('image')
cv2.setMouseCallback('image', select_point)
while True:
    cv2.imshow("image", img)
    if y4 != 0:
        pts1 = np.float32([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
        pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

        M = cv2.getPerspectiveTransform(pts1, pts2)
        dst = cv2.warpPerspective(img, M, (300, 300))
        cv2.imshow('Output', dst)
    if cv2.waitKey(20) & 0xff == 27:
        break
cv2.destroyAllWindows()



