import cv2
import numpy as np

# LER IMAGEM
img = cv2.imread("mulher.jpg")
h,w = img.shape[:2]
hnew = int(h/2)
wnew = int(w/2)

#criando outra matriz (imagem) para o YCbCr
ycbcrImg = np.zeros((h,w,3), np.float)

#Conversão direta de RGB para YCbCr utilizando a formula do material
ycbcrImg[:,:,0] = img[:,:,2]*0.2568 + 0.5041*img[:,:,1] + 0.097*img[:,:,0] +16 #Y - de acordo com a fórmula do exercicio
ycbcrImg[:,:,1] = -img[:,:,2]*0.1482 - 0.2910*img[:,:,1] + 0.4392*img[:,:,0] +128 #Cb - de acordo com a fórmula do exercicio
ycbcrImg[:,:,2] = img[:,:,2]*0.4392 - 0.3678*img[:,:,1] - 0.0714*img[:,:,0] +16 #Cr - de acordo com a fórmula do exercicio

# NORMALIZANDO Y ENTRE 0 e 1
Ymax = np.max(ycbcrImg[:,:,0])
Ymin = np.min(ycbcrImg[:,:,0])
ycbcrImg[:,:,0] = (ycbcrImg[:,:,0] - Ymin)/(Ymax - Ymin)

# NORMALIZANDO Cb ENTRE 0 e 1
Cbmax = np.max(ycbcrImg[:,:,1])
Cbmin = np.min(ycbcrImg[:,:,1])
ycbcrImg[:,:,1] = (ycbcrImg[:,:,1] - Cbmin)/(Cbmax - Cbmin)

# NORMALIZANDO Cr ENTRE 0 e 1
Crmax = np.max(ycbcrImg[:,:,2])
Crmin = np.min(ycbcrImg[:,:,2])
ycbcrImg[:,:,2] = (ycbcrImg[:,:,2] - Crmin)/(Crmax - Crmin)

#CONVERSAO YCbCr OPENCV
ycbcrImg = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)

#REDIMENSIONAR IMAGEM
resizedImg = cv2.resize(img, (wnew, hnew), interpolation=cv2.INTER_AREA)
resizedImg2 = cv2.resize(ycbcrImg, (wnew, hnew), interpolation=cv2.INTER_AREA)
resizedImg3 = cv2.resize(ycbcrImg, (wnew, hnew), interpolation=cv2.INTER_AREA)


# PLOTAR IMAGENS
cv2.imshow("Imagem Original", resizedImg)
cv2.imshow("Imagem YCbCr OPENCV", resizedImg2)
cv2.imshow("Imagem YCbCr", resizedImg3)
cv2.waitKey(0)