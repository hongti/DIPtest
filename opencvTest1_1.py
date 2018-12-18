import cv2
cap = cv2.VideoCapture('C:\\Users\\machenike\\Desktop\\数字图像处理\\实验资料（20181210）\\vtest.avi')
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
    if cv2.waitKey(25) & 0xFF == ord('q')  :
        break
cap.release()
cv2.destroyAllWindows()
