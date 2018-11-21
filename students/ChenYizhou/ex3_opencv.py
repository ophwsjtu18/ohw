import numpy as np
import cv2
from copy import deepcopy
img=cv2.imread("beginner_tutorial67%.png")
ori_img = deepcopy(img)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

cropImg1=img[300:400,0:100]
cropImg2=img[200:300,0:100]

img[300:400,500:600]=cv2.add(cropImg1,cropImg2)

cv2.imshow("image",img)
cv2.imshow("original image", ori_img)
cv2.waitKey(0)
cv2.destroyAllWindows()