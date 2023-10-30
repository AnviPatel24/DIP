#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 13:38:24 2023

@author: bmiit202006100110081
"""


import cv2 
import numpy as np 


# Loading the image 
img = cv2.imread('10.jpg') 

# preprocess the image
gray_img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY) 

kernel = np.ones((2,2), np.uint8)

# Applying threshold  
otsu_threshold, image_result = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU,)


invert=cv2.bitwise_not(image_result)
img_erosion = cv2.erode(invert, kernel, iterations=1) 
kernel2=np.ones((8,8),np.uint8)
img_dilation=cv2.dilate(img_erosion,kernel2,iterations=1)
# Apply the Component analysis function 
totalLabels, label_ids, values, centroid = cv2.connectedComponentsWithStats(img_dilation, 4, cv2.CV_32S) 




print("Total",totalLabels)
cv2.imshow("Image", img) 
cv2.imshow("Inveryt",invert)
cv2.imshow("Filtered Components", img_dilation) 
cv2.waitKey(0)
