import cv2

img = cv2.imread("assets/1.jpg")
if img is None:
    print("Hun? where the image at?")
    exit()

# Gaussian Blur
blurred = cv2.GaussianBlur(img, (9, 9), 0)

# Converting to greyscale for Edge detection
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

# ACanny ED
edges = cv2.Canny(gray, 100, 200)

cv2.imshow("Original", img)
cv2.imshow("Blurred", blurred)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
