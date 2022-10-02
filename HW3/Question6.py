import cv2 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
  
# Read the image. 
img = cv2.imread('inputq6.png') 

im = mpimg.imread('inputq6.png')
imgplot = plt.imshow(im)


# Apply bilateral filter

bilateral = cv2.bilateralFilter(img, 15, 75,75)

# Save the output. 
cv2.imwrite('bilateral.png',bilateral) 
