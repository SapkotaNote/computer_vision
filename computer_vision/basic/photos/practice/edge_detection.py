import cv2
img = cv2.imread(r'C:\\Users\\Kantipur\\Desktop\\New folder\\computer_vision\\basic\\sources\\images\\img2.jpg')
img_ = cv2.resize(img, (600,600))

edge = cv2.Canny(img_,
                 4500,4500,
                 apertureSize=5) # ----> only 3,5

cv2.imshow('EDGE IMAGE', edge)
cv2.imshow('ORGINAL IMAGE', img_)
cv2.waitKey(0)
cv2.destroyAllWindows()