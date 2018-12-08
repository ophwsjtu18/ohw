import numpy as np
import cv2

cap=cv2.VideoCapture(0)
ret,frame = cap.read()

L=len(frame)
W=len(frame[0])

print(L,W)

SIZE=100

X0=int(W/2-1.5*SIZE)
Y0=int(L/2-1.5*SIZE)

while(True):
    ret,frame = cap.read()
    for i in range(3):
        for j in range(3):
            cv2.rectangle(frame,(i*SIZE+X0,j*SIZE+Y0),(i*SIZE+SIZE+X0,j*SIZE+SIZE+Y0),(255,128,255),5)  
    cv2.imshow('frame',frame)
    if cv2.waitKey(1000)&0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()