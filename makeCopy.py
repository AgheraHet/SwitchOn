"""
This Code is to generat 100 copy of one image with image name 1.jpe to 100.jpg 
"""


import cv2

img =  cv2.imread(r'one.jpg')

for i in range(100):
    name = "pics\\"+str(i+1)+".jpg"
    cv2.imwrite(name,img)