import cv2
import numpy as np
from matplotlib import pyplot as plt
import statistics
def averagefiletering(img):
	row,col = img.shape
	blur = np.zeros((row,col))
	for i in range(row):
		for j in range(col):
			suma = 0
			for a in range(max(0,i-2),min(row,i+2)):
				for b in range(max(0,j-2),min(row,j+2)):
					suma = suma + img[a][b]
			blur[i][j] = suma/25
	return blur

def medianfiletering(img):
	row,col = img.shape
	blur = np.zeros((row,col))
	for i in range(row):
		for j in range(col):
			ar = []
			for a in range(max(0,i-2),min(row,i+2)):
				for b in range(max(0,j-2),min(row,j+2)):
					ar.append(img[a][b])
			if ar:
				blur[i][j] = np.median(np.array(ar))
			
	return blur


img = cv2.imread('./images/q3.tif',0)
print(img.shape)
median = medianfiletering(img)
average = averagefiletering(img)

plt.subplot(131),plt.imshow(img,cmap=plt.cm.gray),plt.title('Original')
plt.subplot(132),plt.imshow(average,cmap=plt.cm.gray),plt.title('Average Filtering')
plt.subplot(133),plt.imshow(median,cmap=plt.cm.gray),plt.title('Median Filtering')

plt.show()

