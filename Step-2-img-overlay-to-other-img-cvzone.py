import cv2

imgBack = cv2.imread('background_images/BAGGAGE_20180811_175323_83216_B_1.jpg')
imgBack = cv2.cvtColor(imgBack, cv2.COLOR_BGR2BGRA)
imgBack[:,:,3] = 0

imgFront = cv2.imread('Mix/step-1.png', cv2.IMREAD_UNCHANGED)

result = cv2.addWeighted(imgFront, 0.50, imgBack, 0.50, 0)

cv2.imshow('result',result)
cv2.waitKey(0)
cv2.imwrite('Mix/step-2.png',result)