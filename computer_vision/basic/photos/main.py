import cv2
import numpy as np
img = cv2.imread(r'C:\\Users\\Kantipur\\Desktop\\New folder\\photos\\photos\\img3.jpg')
if img is None:
    print("recheck image link!")
else:
    image = cv2.resize(img, (500, 500))
    #-------------------------------------------------------------------
    # text = cv2.putText(
    #     image,
    #     text="This is text",
    #     org=(250,250),
    #     fontFace= cv2.FONT_HERSHEY_COMPLEX,
    #     fontScale=1.2,
    #     color=(255,0,0),
    #     thickness=4,
    #     lineType=cv2.LINE_8,
    #     bottomLeftOrigin=False
    # )
    #----------------------------------------------------------------------
    # Rectangle
    # rectangle = cv2.rectangle(
    #     img=image,
    #     pt1=(200,200),
    #     pt2=(250,250),
    #     color=(0,0,255),
    #     thickness=4,
    #     lineType= cv2.LINE_4
    # )
    #------------------------------------------------------------------
    # circule = cv2.circle(
    #     img=image,
    #     center=(250,150),
    #     radius=85,
    #     color=(0,255,0),
    #     thickness = 4,
    #     lineType= cv2.LINE_8
    # )
    #------------------------------------------------------------------
    # ellips = cv2.ellipse(
    #     img=image,
    #     center=(250,150),
    #     axes=(45,100),
    #     angle=45,
    #     startAngle= 0,
    #     endAngle=360,
    #     color=(255,0,0),
    #     thickness=5,
    #     lineType= cv2.LINE_8
    # )
    #------------------------------------------------------------------
    # pts = np.array([[100,400],[150,300],[50,75],[75,100],[100,120]])
    # pts = pts.reshape((-1, 1, 2))
    # pentagonon = cv2.polylines(
    #     image,
    #     [pts],
    #     isClosed=True,
    #     color=(255,0,0),
    #     thickness=4,
    #     lineType=cv2.LINE_4
    # )
    #------------------------------------------------------------------
    #EDGE DETECTION
    # new_img = cv2.Canny(image,235,235, apertureSize=5)
    #------------------------------------------------------------------
    # SCALLING, ROTATING
    # h, w = image.shape[:2]
    # rotate = cv2.getRotationMatrix2D((w/2,h/2),90,-1) # -1 for rotate from left, 1 fro ratater from right side
    # new_img = cv2.warpAffine(image,rotate,(w,h))
    #------------------------------------------------------------------
    # 17 IMAGE BLURING
    # G = cv2.GaussianBlur(image, (7,7),0)
    # M = cv2.medianBlur(image,(3))
    #B = cv2.blendLinear(image, 9)# Wrong format
    #------------------------------------------------------------------
    #18 SAVING IMAGE
    # h = np.hstack((image,image))
    # cv2.imwrite('save_image.jpg',h)
    #------------------------------------------------------------------


cv2.imshow('This is windows', )
cv2.waitKey(0)
cv2.destroyAllWindows()