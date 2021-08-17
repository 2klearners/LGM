#Importing Libraries
import cv2
#Read Image
a=cv2.imread("02.png")
#Convert Color Image(RBG) into Gray Scale(B & W)
gray_image=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
cv2.imwrite("1.png",gray_image)
#Inverted Image
invert_image=255-gray_image
cv2.imwrite("2.png",invert_image)
#Blurred Image
blurred=cv2.GaussianBlur(invert_image,(21,21),0)
cv2.imwrite("3.png",blurred)
#inverted Blurred
inverted_blurred=255-blurred
cv2.imwrite("4.png",inverted_blurred)
#Pencil Sketch
pencil_sketch=cv2.divide(gray_image,inverted_blurred,scale=256.0)
cv2.imwrite("5.png",pencil_sketch)
#Show Original and Converted Image
cv2.imshow("original image", a)
cv2.imshow("Gray Image", gray_image)
cv2.imshow("Invert Image", invert_image)
cv2.imshow("Blurred Image",blurred)
cv2.imshow("Inverted Blurred", inverted_blurred)
cv2.imshow("pencil sketch", pencil_sketch)
