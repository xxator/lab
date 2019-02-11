import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def matlab_style_gauss2D(shape=(3,3),sigma=0.5):
    """
    2D gaussian mask - should give the same result as MATLAB's
    fspecial('gaussian',[shape],[sigma])
    """
    m,n = [(ss-1.)/2. for ss in shape]
    y,x = np.ogrid[-m:m+1,-n:n+1]
    h = np.exp( -(x*x + y*y) / (2.*sigma*sigma) )
    h[ h < np.finfo(h.dtype).eps*h.max() ] = 0
    sumh = h.sum()
    if sumh != 0:
        h /= sumh
    return h

img = cv2.imread('./images/q2.tif',0)
print(img.shape)

print(matlab_style_gauss2D((5,5)))

blur3 = cv2.GaussianBlur(img,(3,3),0)

blur5 = cv2.GaussianBlur(img,(5,5),0)

blur7 = cv2.GaussianBlur(img,(7,7),0)

blur9 = cv2.GaussianBlur(img,(9,9),0)

fig = plt.figure(figsize=(8, 5))
pl1 = plt.subplot(2,3,1)

pl1.imshow(img,cmap=plt.cm.gray)


pl2 = plt.subplot(2,3,2)
pl2.imshow(blur3,cmap=plt.cm.gray)
pl2.set_axis_off()
#pl2.set_xlable('3x3 gausian blur')

pl3 = plt.subplot(2,3,3)
pl3.imshow(blur5,cmap=plt.cm.gray)
pl3.set_axis_off()
#pl3.set_xlable('5x5 gausian blur')

pl4 = plt.subplot(2,3,4)
pl4.imshow(blur7,cmap=plt.cm.gray)
pl4.set_axis_off()
#pl4.set_xlable('7x7 gausian blur')

pl5 = plt.subplot(2,3,5)
pl5.imshow(blur9,cmap=plt.cm.gray)
pl5.set_axis_off()
#pl5.set_xlable('9x9 gausian blur')
fig.tight_layout()
plt.show()