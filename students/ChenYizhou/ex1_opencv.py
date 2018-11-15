import cv2
import numpy as np

'''
pre_img = cv2.imread('./beginner_tutorial67%.png')
img = np.array(pre_img)
print(img.shape)
print(type(img))
cv2.imshow('IMAGE', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow('my_frame', frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
