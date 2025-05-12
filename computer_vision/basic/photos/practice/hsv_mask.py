import cv2
import numpy as np

cap =cv2.VideoCapture(r'C:\\Users\\Kantipur\\Desktop\\New folder\\computer_vision\\basic\\sources\\videos\\video.mp4')
def sapkota(x):
    pass
cv2.namedWindow("window")
cv2.createTrackbar('lb', "window", 0, 200, sapkota)
cv2.createTrackbar('lg', "window", 0, 200, sapkota)
cv2.createTrackbar('lr', "window", 0, 200, sapkota)
cv2.createTrackbar('ub', "window", 0, 250, sapkota)
cv2.createTrackbar('ug', "window", 0, 250, sapkota)
cv2.createTrackbar('ur', "window", 0, 250, sapkota)

while True:
    r,frame = cap.read()
    if cap is None:
        break
    else:
        if r == True:
            img = cv2.resize(frame, (400,400))
            hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            lb=cv2.getTrackbarPos('lb', "window")
            lr=cv2.getTrackbarPos('lr', "window")
            lg=cv2.getTrackbarPos('lg', "window")
            ub=cv2.getTrackbarPos('ub', "window")
            ur=cv2.getTrackbarPos('ur', "window")
            ug=cv2.getTrackbarPos('ug', "window")

            lo = np.array(([lb,lr,lg]))
            up= np.array(([ub,ur,ug]))

            maks = cv2.inRange(hsv_img, lo,up)
            res = cv2.bitwise_and(img, img, mask=maks)

            cv2.imshow("this is orginal image",img)
            cv2.imshow("this is HSV image",hsv_img)
            cv2.imshow("this is RES",res)
            cv2.imshow("this is MASK",maks)
            if cv2.waitKey(1) & 0xff == ord('p'):
                break
            
        else:
            break
cap.release()
cv2.destroyAllWindows()