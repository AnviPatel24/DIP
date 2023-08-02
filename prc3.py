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

hid,wid=image3.shape
print("Height is: ",hid)
print("Width is: ",wid)
for i in range(height-2,height+2):
     for j in range(width-2,width+2):
         #print("image[",i,"]","[",j,"]","= ",image3[i][j])
         if(i==height and j==width):
             print("Left",image3[i][j-1])
             print("Top",image3[i-1][j])
             print("Right",image3[i][j+1])
             print("Bottom",image3[i+1][j])
             print("Diagonal left up",image3[i-1][j-1])
             print("Diagonal rightt up",image3[i-1][j+1])
             print("Diagonal left down",image3[i+1][j-1])
             print("Diagonal right down",image3[i+1][j+1])
cv2.waitKey(0)
cv2.destroyAllWindows()