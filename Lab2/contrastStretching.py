import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import matplotlib.cbook as cbook

class ConstS:
    def __init__(self,_img):
        self.a=0
        self.b=255
        self.img=_img

    def Formula(self,Fxy):
        return (Fxy-self.c)*((self.b-self.a)/(self.d-self.c))+self.a

    def contrastS(self):
        rows,columns=self.img.shape
        newimg=[[] for i in range(rows)]
        for i in range(rows):
            for j in range(columns):
                newimg[i].append(self.Formula(self.img[i,j]))
        return np.array(newimg)

    def limitXY(self):
        hist=cv.calcHist([self.img],[0],None,[256],[0,256])


img=cv.imread('contrast.jpg',0)

contrast=ConstS(img)
contrast.limitXY()

#newimg=contrast.contrastS()
#print(img)
#print(newimg)

#plt.subplot(1,2,1),plt.imshow(img,'gray')
#plt.subplot(1,2,2),plt.imshow(newimg,'gray')

#plt.show()
