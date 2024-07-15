
from numpy import imag, invert
import cv as cv2

image = cv2.imread("tiger.png")

cv2.imshow("Image",image)
gray_image=cv2.GaussianBlur(inverted,(21,21) , 0)
invertedBlur=255-blur
sketch=cv2.divide(gray_image,invertedBlur,scale=256.0)
cv2.imwrite("skd.jpg", sketch)
cv2.imshow("Sketch",sketch)
cv2.waitkey(0)