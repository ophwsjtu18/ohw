import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

# 显示所有事件
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

havedoubleclick = 0


def draw_circle(event, x, y, flags, param):
    global havedoubleclick
    if event == cv2.EVENT_LBUTTONDBLCLK:
        havedoubleclick += 1


# print("get double click")

ret, frame = cap.read()
# 创建图像与窗口并将窗口与回调函数绑定
cv2.namedWindow('frame')
cv2.setMouseCallback('frame', draw_circle)

while True:
    _, frame = cap.read()
    lenth = int(len(frame[0]))
    width = int(len(frame))
    cv2.rectangle(frame, (int(lenth / 2 - 50), int(width / 2 - 50)), (int(lenth / 2 + 50), int(width / 2 + 50)),
                  (25, 128, 25), 5)
    if havedoubleclick % 2 == 0:
        cv2.circle(frame, (int(lenth / 2), int(width / 2)), 100, (255, 0, 0), -1)
    cv2.imshow('frame', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()