# Program that transforms your face into a cartoon face

# Import relevant libaries
import cv2
import numpy as np

# Read the image
img = cv2.imread("Icarus.jpg")

# Outer image
gray = cv2.cvColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255,
                                cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY, 9, 9)
# Transform to cartoon
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2. bitwise_and(color, color, mask=edges)

cv2.imshow("Image", img)
cv2.imshow("edges", edges)
cv2.imshow("Cartoon", cartoon)
cv2.waitkey (0)
cv2.destroyAllWindows()

