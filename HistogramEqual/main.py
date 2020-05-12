import cv2  as cv
import matplotlib.pyplot as plt
import numpy as np
from HistogramEqual import HistogramEqual as HisEqual


img = cv.imread('hist5.jpg',0)

histEqual = HisEqual(img)
newimg,hist = histEqual.Equalization()
cv.imwrite('outhist5.jpg',newimg)

newimgmask,histmask = histEqual.EqualizationMask([350,330],100,120)
cv.imwrite('outhist5mask.jpg',newimgmask)

#plt.imshow(,,vmin=0,vmax=255)

