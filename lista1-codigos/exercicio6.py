import cv2
import numpy as np


# LER IMAGEM
img = cv2.imread("mulher.jpg")

# Filtros
filtro_f1 = np.array([[0,1,0],[1,1,1],[0,1,0]])/5
media_f1 = cv2.filter2D(img, -1, filtro_f1)

filtro_f2 = np.array([[1,1,1],[1,1,1],[1,1,1]])/9
media_f2 = cv2.filter2D(img, -1, filtro_f2)

filtro_f3 = np.array([[1,1,1],[1,2,1],[1,1,1]])/10
media_f3 = cv2.filter2D(img, -1, filtro_f3)

filtro_f4 = np.array([[1,2,1],[2,4,2],[1,2,1]])/12
media_f4 = cv2.filter2D(img, -1, filtro_f4)


cv2.imshow("original", img)
cv2.imshow("media 3x3 F1", media_f1)
cv2.imshow("media 3x3 F2", media_f2)
cv2.imshow("media 3x3 F3", media_f3)
cv2.imshow("media 3x3 F4", media_f4)
cv2.waitKey()
