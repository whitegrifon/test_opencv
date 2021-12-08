import cv2
def s_img(name, img):
    cv2.imshow(name, img)

img = cv2.imread('test.png')
s_img('original', img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
s_img('hsv', hsv)

hsv_min = (60, 50, 44)
hsv_max = (120, 255, 255)

hsv_min_r = (0, 100, 0)
hsv_max_r = (10, 255, 255)

hsv_min_r1 = (170, 100, 0)
hsv_max_r1 = (179, 255, 255)

thresh_1 = cv2.inRange(hsv, hsv_min_r, hsv_max_r)
thresh_2 = cv2.inRange(hsv, hsv_min_r1, hsv_max_r1)
thresh = cv2.inRange(hsv, hsv_min, hsv_max)
thresh_3 = thresh_1 + thresh_2
s_img('red1', thresh_1)
s_img('red2', thresh_2)
#s_img('red21')
s_img('red3', thresh_3)
s_img('green', thresh)



moments = cv2.moments(thresh_3, 1)
dM01 = moments['m01']
dM10 = moments['m10']
dArea = moments['m00']

x = int(dM10 / dArea)
y = int(dM01 / dArea)
cv2.circle(img, (x, y), 10, (0, 255, 255), -1)

cv2.imshow('result', img)

cv2.waitKey(0)
cv2.destroyAllWindows()