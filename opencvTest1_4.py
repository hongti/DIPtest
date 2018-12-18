import cv2

flag = True
font = cv2.FONT_HERSHEY_SIMPLEX
cap = cv2.VideoCapture('C:\\Users\\machenike\\Desktop\\数字图像处理\\实验资料（20181210）\\vtest.avi')
string = ['message1', 'message2', 'message3', '']
num = 0

def showMessage(event,x,y,flags,param):
    global flag
    if event == cv2.EVENT_LBUTTONDOWN:
        flag = (not flag)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        num += 25
        if flag:
            num %= 3
        else:
            num = 3
        messageFrame = cv2.putText(frame, string[num], (100, 50), font, 1, (0, 0, 255), 2)
        color = cv2.cvtColor(messageFrame, 1)
        cv2.setMouseCallback('frame', showMessage)
        cv2.imshow('frame', color)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
