# Python program to explain cv2.circle() method
    
# importing cv2
import cv2
import numpy as np
import os
    
# Reading an image in default mode
image = cv2.imread('Data/new-diagram.jpg')

# Red color in BGR
color = (0, 0, 0)

# Line thickness of -1 px (fill)
thickness = -1

# Reading shape centers from file
centers = open('Data/centers.txt', 'r').readlines()
categories = open('Data/categories.txt', 'r').readlines()
dimensions = open('Data/dimensions.txt', 'r').readlines()
orientations = open('Data/orientations.txt', 'r').readlines()

counter = 0

# Reading each line
for center in centers:
    # Center coordinates
    cX = int(center.split(',')[0])
    cY = int(center.split(',')[1])
    center_coordinates = (cX, cY)
    
    # Dimensions
    x = int(dimensions[counter].split(',')[0])
    y = int(dimensions[counter].split(',')[1])
    w = int(dimensions[counter].split(',')[2])
    h = int(dimensions[counter].split(',')[3])
    
    
    # Drawing the circle
    if categories[counter] == "Circle\n":
        image = cv2.circle(image, center_coordinates, int(w/2), color, thickness)
        
    # Drawing the rectangle
    if categories[counter] == "Square\n":
        image = cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,0),-1)
    
    # Drawing the triangle
    if categories[counter] == "Triangle\n":
        pt1 = (x, y+h)
        pt2 = (x+w, y+h)
        pt3 = (x+int(w/2), y)
        triangle_cnt = np.array( [pt1, pt2, pt3] )
        cv2.drawContours(image, [triangle_cnt], 0, (0,0,0), -1)
    
    # Drawing the line
    if categories[counter] == "Line\n":
        if int(orientations[counter]) < 20:
            image = cv2.line(image,(x,y),(x-w,y+h),(0,0,0),5)
        else:
            image = cv2.line(image,(x,y),(x+w,y+h),(0,0,0),5)
    
    
    #cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    counter+=1

    
# Exporting the image
cv2.imwrite(os.path.join('Data/' , 'new-diagram.jpg'), image)
