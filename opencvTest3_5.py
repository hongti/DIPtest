import cv2
import numpy as np

img = cv2.imread('photo\\mogu.png')
rows, cols, ch = img.shape

# 当鼠标按下时变为True
# 如果mode 为true 绘制矩形。按下'm' 变成绘制曲线。
# 创建回调函数
def select_point(event, x, y, flags, param):
    # 当按下左键是返回起始位置坐标
    if event == cv2.EVENT_LBUTTONDOWN:



        cv2.imshow('Output', dst)
    # 当鼠标左键按下并移动是绘制图形。event 可以查看移动，flag 查看是否按下

cv2.namedWindow('image')
cv2.setMouseCallback('input', select_point)
cv2.imshow("image", img)

while(1):
    pts1 = np.float32([[y1, x1], [y2, x2], [y3, x3], [y4, x4]])
    pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(img, M, (cols, rows))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
