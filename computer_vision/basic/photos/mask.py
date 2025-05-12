import cv2
import numpy as np

# Placeholder function for trackbars
def sapkota(x):
    pass

# Open the video file
cap = cv2.VideoCapture(r'C:\\Users\\Kantipur\\Desktop\\New folder\\photos\\video\\video1.mp4')

# Create a window with trackbars for HSV range selection
cv2.namedWindow("uhh see this")
cv2.createTrackbar('lb', "uhh see this", 0, 255, sapkota)
cv2.createTrackbar('lg', "uhh see this", 0, 255, sapkota)
cv2.createTrackbar('lr', "uhh see this", 0, 255, sapkota)
cv2.createTrackbar('ub', "uhh see this", 0, 255, sapkota)
cv2.createTrackbar('ug', "uhh see this", 0, 255, sapkota)
cv2.createTrackbar('ur', "uhh see this", 0, 255, sapkota)

while True:
    ret, frame = cap.read()  # Read a frame from the video
    if ret:  # Check if the frame was successfully grabbed
        img = cv2.resize(frame, (500, 500))  # Resize the image for easier viewing
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # Convert the image to HSV

        # Get the values from the trackbars
        LB = cv2.getTrackbarPos('lb', "uhh see this")
        LG = cv2.getTrackbarPos('lg', "uhh see this")
        LR = cv2.getTrackbarPos('lr', "uhh see this")
        UB = cv2.getTrackbarPos('ub', "uhh see this")
        UG = cv2.getTrackbarPos('ug', "uhh see this")
        UR = cv2.getTrackbarPos('ur', "uhh see this")

        # Create numpy arrays for the lower and upper boundaries of the color range
        lo = np.array([LB, LG, LR])
        up = np.array([UB, UG, UR])

        # Apply the mask and bitwise AND operation to extract the color range
        mask = cv2.inRange(hsv_img, lo, up)
        res = cv2.bitwise_and(img, img, mask=mask)

        # Display the results
        cv2.imshow("res", res)
        cv2.imshow("mask", mask)
        cv2.imshow("hsv_image", hsv_img)  # Display the original HSV image
        cv2.imshow("SEE ME", img)  # Display the original image

        # Break the loop when the user presses the 'p' key
        if cv2.waitKey(1) & 0xFF == ord('p'):
            break
    else:
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
