import numpy as np
import cv2
import urllib.request
response = urllib.request.urlopen(192.168.40.130)
cap=cv2.VideoCapture(0)
ret,frame = cap.read()

Size=100

l=len(frame)
w=len(frame[0])

X0=int(w/2-1.5*Size)
Y0=int(l/2-1.5*Size)

while(True):
    ret,frame=cap.read()
    for i in range(3):
        for j in range(3):
            cv2.rectangle(frame,(i*Size+X0,j*Size+Y0),(i*Size+Size+X0,j*Size+Size+Y0),(255,0,0),2)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1000)&0xFF==ord('q'):
        break
cap.release()
cv2.destoryAllWindows()
