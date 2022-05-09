import cv2
import cvzone

img = cv2.imread('Mix/step-0.png')
img3 = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
img3[:,:,3] = 150 #Lower the value, lesser the clarity

cv2.imshow('img.png',img3)
cv2.waitKey(0)
cv2.imwrite('Mix/step-1.png',img3)