import cv2
import cv2.cv2

cap = cv2.VideoCapture(0)
out = cv2.VideoWriter('out.avi', cv2.VideoWriter_fourcc(*"MJPG"), 25.0, (640, 480))
while True:
    ret, frame = cap.read()
    if(ret==True):
        out.write(frame)
        cv2.cv2.imshow('v-f', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()

cv2.destroyAllWindows()