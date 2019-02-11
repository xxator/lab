import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('./images/q3.tif',0)
print(img.shape)
median = cv2.medianBlur(img,5)
blur = cv2.blur(img,(5,5))

plt.subplot(131),plt.imshow(img),plt.title('Original')
plt.subplot(132),plt.imshow(average),plt.title('Average Filtering')
plt.subplot(133),plt.imshow(median),plt.title('Median Filtering')

plt.show()

