import cv2
import numpy as np


cap = cv2.VideoCapture(r'C:\\Users\\Kantipur\\Desktop\\New folder\\computer_vision\\basic\\sources\\videos\\video2.mp4')

while cap.isOpened:
    r,frame = cap.read()
    if r is None:
        break
    else:
        if r == True:
            cv2.imshow('video', frame)
            if cv2.waitKey(25) & 0xff == ord('p'):
                break
        else:
            break
cap.release()
cv2.destroyAllWindows()