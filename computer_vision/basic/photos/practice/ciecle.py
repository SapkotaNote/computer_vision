import cv2
img = cv2.imread(r'C:\\Users\\Kantipur\\Desktop\\New folder\\computer_vision\\basic\\sources\\images\\img2.jpg')
img_ = cv2.resize(img, (600,600))

circle = cv2.circle(
    img_,
    color=(250,0,255),
    center = (300,330),
    radius = 120,
    thickness=4,
    lineType = cv2.LINE_AA
)
cv2.imshow("THIS IS IMAGE", circle)
cv2.waitKey(0)
cv2.destroyWindow()