import cv2

# Correct URL for the MJPEG stream
url = 'http://192.168.1.6:5050/'  # Ensure this URL is correct

cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Error: Couldn't open video stream")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        cv2.imshow("IP Camera", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
