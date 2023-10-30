#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 19:12:16 2022

@author: bmiit202006100110081
"""
import cv2 
import numpy as np 


# Loading the image 
img = cv2.imread('2.jpg') 

# preprocess the image 
gray_img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY) 

kernel = np.ones((5,5), np.uint8) 

# Applying threshold 

threshold = cv2.threshold(gray_img, 0, 255, 
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1] 
invert=cv2.bitwise_not(threshold)
img_erosion = cv2.erode(invert, kernel, iterations=1) 

# Apply the Component analysis function 
totalLabels, label_ids, values, centroid = cv2.connectedComponentsWithStats(img_erosion, 4, cv2.CV_32S) 




print("Total",totalLabels)
cv2.imshow("Image", img) 
cv2.imshow("Inveryt",invert)
cv2.imshow("Filtered Components", img_erosion) 
cv2.imshow("Threshold", threshold) 
cv2.waitKey(0)