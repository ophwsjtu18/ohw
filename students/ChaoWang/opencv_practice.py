# -*- coding: utf-8 -*-
import numpy as np
import cv2

#读取一张图片，按任意键退出
'''im_huaji = cv2.imread('E:/Study/examples/matlab/huaji.png')
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',im_huaji)

cv2.waitKey(0)
cv2.destroyAllWindows()'''

#抓取摄像头一张图，显示出来，按q键返回,每1000毫秒检测一次
'''cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    cv2.imshow('my_frame',frame)
    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()'''

#在视频左上角添加一个矩形白框,框的粗细为5个像素
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    cv2.rectangle(frame,(0,0),(100,100),(255,128,255),5)
    print(len(frame))
    print(len(frame[0]))
    cv2.imshow('my_frame',frame)
    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
