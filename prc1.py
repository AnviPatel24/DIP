#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 12:00:21 2023

@author: bmiit202006100110081
"""

import cv2

image = cv2.imread("js2.png",0)
cv2.imshow("Javascript Gray Scale Image",image)

image2 = cv2.imread("js2.png",0)

ret,bin_image=cv2.threshold(image2,73,255,cv2.THRESH_BINARY)
cv2.imshow("Javascript Binary Image",bin_image)

height,width=image.shape
print(height,width)

for i in range(0,height):
    for j in range(0,width):
         if(image[i][j]<125):
             image[i][j]=255
         if(image[i][j]==0):
             image[i][j]=125

cv2.imshow("Javascript White Bordered Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()