import cv2
import numpy as np

# LER E REDIMENSIONAR IMAGEM
img = cv2.imread("papagaio.jpg")
img2 = cv2.imread("papagaio.jpg")
h,w = img.shape[:2]
hnew = int(h/2)
wnew = int(w/2)
resizedImg = cv2.resize(img2, (wnew, hnew), interpolation=cv2.INTER_AREA)

# IMAGEM CINZA OPENCV
imgCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
resizedImg2 = cv2.resize(imgCinza, (wnew, hnew), interpolation=cv2.INTER_AREA)

# Pegar os pixeis RGB
bp = img[:,:,0]
gp = img[:,:,1]
rp = img[:,:,2]

media = ((bp + gp + rp)/3)

# IMAGEM CINZA MEDIA

img[:,:, 0] = media
img[:,:, 1] = media
img[:,:, 2] = media

resizedImg3 = cv2.resize(img, (wnew, hnew), interpolation=cv2.INTER_AREA)

# MOSTRAR IMAGEM NA TELA
cv2.imshow("Imagem Original", resizedImg)
cv2.imshow("Cinza OPENCV", resizedImg2)
cv2.imshow("Cinza Media", resizedImg3)
cv2.waitKey(0)