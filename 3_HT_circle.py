import cv2
import numpy as np

img = cv2.imread("assets/2.png")
if img is None:
    print("Error: Image not found.")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)

blurred = cv2.GaussianBlur(thresh, (9, 9), 2)

# para
circles = cv2.HoughCircles(
    blurred,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=100,         
    param1=150,         
    param2=50,           
    minRadius=40,        
    maxRadius=100)

# drawinggg
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)     
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)          #CP

cv2.imshow("HT Circle Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
