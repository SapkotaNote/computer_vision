import cv2

img = cv2.imread(r'C:\\Users\\Kantipur\\Desktop\\New folder\\computer_vision\\basic\\sources\\images\\img2.jpg')
img_ = cv2.resize(img, (600,600))

rectangle = cv2.rectangle(
    img = img_,
    color = (250,250,0),
    thickness = 5,
    pt1=(200,200),
    pt2 = (400,450),
    lineType = cv2.LINE_AA
)
cv2.imshow("LOOK THIS", rectangle)
cv2.waitKey(0)
cv2.destroyAllWindows()