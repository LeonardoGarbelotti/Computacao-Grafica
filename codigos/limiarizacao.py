import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("papagaio.jpg")
#tamanho da imagem
h,w = img.shape[:2]
cv.imshow("Img Original", img)

limiar = 110

imgCinza = np.zeros((h,w), np.uint8)

imgCinza = (img[..., 0]*0.1 + img[..., 1] * 0.65 + img[..., 2] * 0.25).astype('uint8')
cv.imshow("Imagem Cinza", imgCinza)

hist = cv.calcHist([imgCinza],[0], None, [256],[0,256])

max = np.argmax(hist)
print(max)

'''
cv.imshow("Binarizacao opencv", res)

for i in range(h):
    for j in range(w):
        if img[i,j,2] >= limiar:
            binaria[i,j] = 255
        if img[i,j,1] >= limiar2:
            binaria[i,j] = 255
'''
th,res = cv.threshold(img[...,1],220,255,cv.THRESH_BINARY)
cv.imshow("Limiarizado", res)
plt.plot(hist,color = 'r')
plt.xlim([0,255])
plt.show()
cv.waitKey(0)