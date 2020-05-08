import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import matplotlib.cbook as cbook

class ConstS:
    def __init__(self,_img):
        self.a=0
        self.b=255
        self.img=_img
        self.c=0
        self.d=255

    def Formula(self,Fxy):
        return (((Fxy-self.c)*((self.b-self.a)/(self.d-self.c)))+self.a)%256

    def Stretch(self):
        rows,columns=self.img.shape
        newimg=[[] for i in range(rows)]
        for i in range(rows):
            for j in range(columns):
                newimg[i].append(self.Formula(self.img[i,j]))
        return np.array(newimg)

    def CDlimit(self,l=0):
        hist,bins =np.histogram(self.img.flatten(),256,[0,256])
        
        self.c=np.min(self.img)
        self.d=np.max(self.img)

        rows,columns=self.img.shape
        l=(rows*columns*l)/100
        if(l!=0):
            i=self.c
            while True:
                if(hist[i]>=int(l)):
                    self.c=i
                    break
                i=i+1
    
            i=self.d
            while True:
                if(hist[i]>=int(l)):
                    self.d=i
                    break
                i=i-1

def addOutlier(img,r,c):
    for i in range(r):
        for j in range(c):
            img[i,j]=1

img=cv.imread('contrast.jpg',0)

#ContrastStretching sin outlier
contrast=ConstS(img)
contrast.CDlimit()
newimg=contrast.Stretch()

cv.imwrite('outimg.jpg',newimg)

#Agregando outlier a la imagen
addOutlier(img,30,30)
cv.imwrite('imgoutlier.jpg',img)

#Aplicando ContrastStretch con limites
contrast1=ConstS(img)
contrast1.CDlimit(15)
newimg1=contrast.Stretch()

cv.imwrite('outimgoutlier.jpg',newimg1)


