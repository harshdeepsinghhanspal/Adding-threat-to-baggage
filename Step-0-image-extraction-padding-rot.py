import cv2
import numpy as np
import cvzone

img = cv2.imread('threat_images/BAGGAGE_20170522_113049_80428_A.jpg')
imgBg = cv2.imread('background_images/BAGGAGE_20180811_175323_83216_B_1.jpg')

# Convert to gray, and threshold
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
th, threshed = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

# Morph-op to remove noise
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
morphed = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, kernel)

# Find the max-area contour
cnts = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
cnt = sorted(cnts, key=cv2.contourArea)[-1]

# Crop
x,y,w,h = cv2.boundingRect(cnt)
dst = img[y:y+h, x:x+w]

# length, breadth extraction
old_image_height, old_image_width, channels = dst.shape
bg_height, bg_width, bg_channel = imgBg.shape

# paddings addition
new_image_width = bg_width
new_image_height = bg_height
color = (255,255,255)
result = np.full((new_image_height,new_image_width, channels), color, dtype=np.uint8)

# compute center offset
x_center = (new_image_width - old_image_width) // 2
y_center = (new_image_height - old_image_height) // 2

# copy img image into center of result image
result[y_center:y_center+old_image_height,
       x_center:x_center+old_image_width] = dst
dst = result
dst = cvzone.rotateImage(dst,45)#45deg rotation

#remove black collar after rotation
x,y,z = np.shape(dst)
for py in range(0,x):
    for px in range(0,y):
        if(dst[py][px][0] < 10):
            dst[py][px][0]=255
            dst[py][px][1]=255
            dst[py][px][2]=255

# view result
cv2.imshow("result", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save result
cv2.imwrite("Mix/step-0.png", dst)