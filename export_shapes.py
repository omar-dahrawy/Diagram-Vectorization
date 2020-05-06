# import the necessary packages
import argparse
import imutils
import cv2
import os
import numpy as np
import shutil

exported_images = []

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="path to the input image")
args = vars(ap.parse_args())

# load the image, convert it to grayscale, blur it slightly,
# and threshold it
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

# find contours in the thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# create export directory
if os.path.isdir("Data"):
    shutil.rmtree("Data",ignore_errors=False, onerror=None)

os.mkdir("Data")
os.mkdir("Data/Cropped Shapes")

# loop over the contours
for c in cnts:
    # compute the center of the contour
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    with open("Data/centers.txt", "a") as centers:
        centers.write("{0},{1}\n".format(cX,cY))
    
    # create bounding rectangle
    x,y,w,h = cv2.boundingRect(c)
    with open("Data/dimensions.txt", "a") as dimensions:
        dimensions.write("{0},{1},{2},{3}\n".format(x,y,w,h))
    #cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    
    # crop shape in image
    crop_img = image[y-10:y+h+10, x-10:x+w+10]
    
    # convert to bianry
    crop_img_gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    crop_img_blurred = cv2.GaussianBlur(crop_img_gray, (5, 5), 0)
    crop_img_thresh = cv2.threshold(crop_img_blurred, 60, 255, cv2.THRESH_BINARY)[1]
    
    # invert binary
    crop_img_final = cv2.bitwise_not(crop_img_thresh)

    # add to array
    exported_images.append(crop_img_final)
    
    # write orientation
    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    with open("Data/orientations.txt", "a") as dimensions:
        dimensions.write("{0}\n".format(box[0][1]-box[1][1]))


# export shapes and create new empty image
counter = 0
for shape in exported_images:
    if counter > 9:
        cv2.imwrite(os.path.join("Data/Cropped Shapes" , str(counter)+'.jpg'), shape)
    else:
        cv2.imwrite(os.path.join("Data/Cropped Shapes" , '0'+str(counter)+'.jpg'), shape)
    counter += 1
new_image = np.zeros((image.shape[0],image.shape[1],3), np.uint8)
new_image[:,0:image.shape[1]] = (255,255,255)
cv2.imwrite(os.path.join("Data/" , 'new-diagram.jpg'), new_image)

# show the output image
#cv2.imshow("Image", image)
#cv2.waitKey(0)

# run prediction script on exported images
import predict
