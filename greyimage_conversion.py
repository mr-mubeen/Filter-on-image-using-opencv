import cv2
  
#  herer add your image path 
image = cv2.imread('C:/Users/Mubeen/Desktop/IMG_2487.JPG')

#  convert image to grey
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
#  showing original image
cv2.imshow('Original image',image)
# After conversion
cv2.imshow('Gray image', gray)
  
cv2.waitKey(0)
cv2.destroyAllWindows()