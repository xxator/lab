import cv2
import numpy as np
from matplotlib import pyplot as plt

def laplacefilter(img,mask):
	row,col = img.shape
	blur=np.zeros((row,col))
	for i in range(1,row):
		for j in range(1,col):
			suma = 0
			acount = -1
			bcount = -1
			for a in range(i-1,i+1):
				acount= acount +1
				bcount = 0
				for b in range(j-1,j+1):
					bcount = bcount +1
					suma = suma + (img[a][b]*mask[acount][bcount])
			blur[i][j] = suma/9
	return blur



img = cv2.imread('./images/q4.tif',0)
print(img.shape)
mask = [[1,1,1],[1,-4,1],[1,1,1]]

plt.subplot(231),plt.imshow(img,cmap=plt.cm.gray),plt.title('Original')
lap1 = laplacefilter(img,mask)

plt.subplot(232),plt.imshow(lap1,cmap=plt.cm.gray),plt.title('laplacian mask 1')

# mask = [[0,1,0],[1,-50,1],[0,1,0]]
# lap2 = laplacefilter(img,mask)

# plt.subplot(233),plt.imshow(lap2,cmap=plt.cm.gray),plt.title('laplacian mask 2')

mask = [[-1,-1,-1],[-1,2,-1],[-1,-1,-1]]
lap3 = laplacefilter(img,mask)

plt.subplot(234),plt.imshow(lap3,cmap=plt.cm.gray),plt.title('laplacian mask 3')

# mask = [[0,1,0],[1,-150,1],[0,1,0]]
# lap4 = laplacefilter(img,mask)

# plt.subplot(235),plt.imshow(lap4,cmap=plt.cm.gray),plt.title('laplacian mask 4')
#plt.subplot(133),plt.imshow(median,cmap=plt.cm.gray),plt.title('Median Filtering')

plt.show()

