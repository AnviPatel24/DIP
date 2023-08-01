#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 12:36:46 2023

@author: bmiit202006100110081
"""

import cv2
image3=cv2.imread("js2.png",0)
cv2.imshow("Gray Scale Image",image3)
height=int(input("Enter Height: "))
width=int(input("Enter Width: "))

print("Inputted Height is: ",height)
print("Inputted Width is: ",width)

for i in range(height-2,width+2):
    for j in range(height-2,width+2):
        
cv2.waitKey(0)
cv2.destroyAllWindows()