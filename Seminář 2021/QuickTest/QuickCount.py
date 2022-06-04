

"""
# Standard imports
import cv2
import numpy as np;

# Read image
im = cv2.imread("image2.jpg", cv2.IMREAD_GRAYSCALE)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 10 #10
params.maxThreshold = 200 #200

# Filter by Area.
params.filterByArea = True # True
params.minArea = 500 #1500

# Filter by Circularity
params.filterByCircularity = True #True
params.minCircularity = 0.1 #0.1

# Filter by Convexity
params.filterByConvexity = True #True
params.minConvexity = 0.0 #0.87

# Filter by Inertia
params.filterByInertia = True #True
params.minInertiaRatio = 0.0 #0.01

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3:
    detector = cv2.SimpleBlobDetector(params)
else:
    detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs.
keypoints = detector.detect(im)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob
total_count = 0
for i in keypoints:
    total_count = total_count + 1


im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show blobs
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)

print(total_count)
"""

""" 
get the number of white pixels 
multiply by two 
divide by pixels per human 
"""
import os
import numpy as np
from PIL import Image

pixelsPerPerson = 110 
whiteTreshold = 210

def loadImage(file_path):							# loading input picture of bg and fishes
	pil_image = Image.open(file_path)
	numpy_image = np.asarray(pil_image, np.int)		# converting to numpy array
	return numpy_image

def exportImage(numpy_image, output_path):								# converting numpy array back to exportable picture
	pil_image = Image.fromarray(np.clip(np.uint8(numpy_image), 0, 255))
	pil_image.save(output_path)

def countWhitePixels(image):
    whitenedImage = image

    whitePixelCount = 0
    height = image.shape[0]
    width = image.shape[1]

    for i in range(height):
        for j in  range(width):
            if(image[i][j][0] >= whiteTreshold):
                if(image[i][j][1] >= whiteTreshold):
                    if(image[i][j][2] >= whiteTreshold):
                        whitenedImage[i][j] = [255, 255, 255]
                        whitePixelCount += 1
                        continue
            whitenedImage[i][j] = [0, 0, 0]
    
    exportImage(whitenedImage, "whitePeople.png")  
    return whitePixelCount

image = loadImage("image2.jpg")
whitePixels = countWhitePixels(image)
totalPeopleCount = whitePixels * 2 / pixelsPerPerson 
print(int(totalPeopleCount))
#print(image[0])