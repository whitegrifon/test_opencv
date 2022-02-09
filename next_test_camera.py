import cv2
import numpy as np



cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if(ret==True):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsv_min = (45, 50, 50)
        hsv_max = (70, 250, 250)
        hsv_min_r = (0, 100, 100)
        hsv_max_r = (10, 255, 255)

        hsv_min_r1 = (170, 100, 50)
        hsv_max_r1 = (179, 255, 200)
        ir = cv2.inRange(hsv, hsv_min, hsv_max)
        er = cv2.erode(ir, (7, 7), iterations=5)
        dil = cv2.dilate(er, (7,7), iterations=7)
        ir_r = cv2.inRange(hsv, hsv_min_r, hsv_max_r)
        ir_r1 = cv2.inRange(hsv, hsv_min_r1, hsv_max_r1)
        ir_r2 = ir_r + ir_r1
        er_r = cv2.erode(ir_r2, (100, 100), iterations=5)
        dil_r = cv2.dilate(er_r, (100, 100), iterations=7)
        contours, hierarchy = cv2.findContours(dil.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours1, hierarchy1 = cv2.findContours(dil_r.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            rect = cv2.minAreaRect(cnt)
            box=cv2.boxPoints(rect)
            box = np.int0(box)
            area = cv2.contourArea(cnt)
            if area > 1000:
                cv2.drawContours(frame,[box],0,(0, 255, 0),2)
            x, y, w, h = cv2.boundingRect(cnt)
        for cnt in contours1:
            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            area_red = cv2.contourArea(cnt)
            if area_red > 1000:
                cv2.drawContours(frame, [box], 0, (0, 0, 255), 2)
            x1, y1, w1, h1 = cv2.boundingRect(cnt)

            print('x,y,w,h for red', x1,y1,w1,h1, 'area for red', area_red, 'center for red', x1+w1, y1 + h1)
            print('x,y,w,h', x,y,w,h, 'area', area, 'center', x + w, y + h)
        cv2.imshow('red', dil_r)
        cv2.imshow('v-f', dil)
        cv2.imshow('w-f', frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    if not(ret):
        break

cap.release()

cv2.destroyAllWindows()