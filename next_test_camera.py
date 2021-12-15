import cv2

cap = cv2.VideoCapture('out.avi')
while True:
    ret, frame = cap.read()
    if(ret==True):
        cv2.imshow('v-f', frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    if not(ret):
        break

cap.release()

cv2.destroyAllWindows()