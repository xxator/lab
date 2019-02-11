
	
# import the OpenCV package
import cv2
 
# load the image with imread()
imageSource = '/home/placements2019/Documents/Parth/iivp/Lenna_(test_image).png'
img = cv2.imread(imageSource,cv2.IMREAD_GRAYSCALE)
 
# copy image to display all 4 variations
horizontal_img = img.copy()
vertical_img = img.copy()
both_img = img.copy()
 
# flip img horizontally, vertically,
# and both axes with flip()
horizontal_img = cv2.flip( img, 0 )
vertical_img = cv2.flip( img, 1 )
both_img = cv2.flip( img, -1 )
 
# display the images on screen with imshow()
#cv2.imshow( "Original", img )
#cv2.imshow( "Horizontal flip", horizontal_img )
#cv2.imshow( "Vertical flip", vertical_img )
#cv2.imshow( "Both flip", both_img )
thresh = 127
(thresh, im_bw) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#cv2.imshow("test" , im_bw)

rows,cols = im_bw.shape
print(rows)
count4 = 0
for j in range(cols):
	for i in range(rows):
		if im_bw[j][i] == 255:
			im_bw[j][i] = 1

print(im_bw) 
for j in range(1,cols-1):
	for i in range(1,rows-1):
		if im_bw[j][i] == 1:
			if im_bw[j+1][i] != 1 and im_bw[j-1][i] != 1 and im_bw[j][i+1] != 1 and im_bw[j][i-1] != 1:
				count4 += 1

count8 = 0
for j in range(1,cols-1):
	for i in range(1,rows-1):
		if im_bw[j][i] == 1:
			if im_bw[j+1][i] != 1 and im_bw[j-1][i] != 1 and im_bw[j][i+1] != 1 and im_bw[j][i-1] != 1 and im_bw[j-1][i-1] != 1 and im_bw[j+1][i+1] != 1 and im_bw[j+1][i-1] != 1 and im_bw[j-1][i+1] != 1:
				count8 += 1  
print(count4)
print(count8)

if count4 == 0:
	print("image is 4 connected")
 
if count8 == 0:
	print("image is 8 connected")

print("image is m connected")

# wait time in milliseconds
# this is required to show the image
# 0 = wait indefinitely
#cv2.waitKey(0)

 
# close the windows
#cv2.destroyAllWindows()