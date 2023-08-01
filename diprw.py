import cv2
import numpy 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# READING AND DISPLAYING ANY IMAGE
# print(cv2.__version__)
img2=cv2.imread("stitch.jpeg",0)
cv2.imshow("images", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Conversion of original image to grayscale and then binary image
#img = cv2.imread("img1.png", 0)
#(thresh, binary_image) = cv2.threshold(img, 175, 255, cv2.THRESH_BINARY)
# Displaying original grayscale image and binary image
#cv2.imshow('Original Image', img)
#cv2.imshow('Binary Image', binary_image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


# image = mpimg.imread("img1.png")
#image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# Displaying the original image
# plt.imshow(image)
#print(image)
#gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Displaying the converted image
#plt.imshow(gray_image, cmap='gray')
