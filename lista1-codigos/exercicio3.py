import cv2
import numpy as np
from matplotlib import pyplot as plt

# LER IMAGEM
img = cv2.imread("papagaio.jpg")
h,w = img.shape[:2]
totalPixel = h*w

# Imagem Cinza
imgCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Calcula Histograma
hist = cv2.calcHist([imgCinza],[0],None,[256],[0,256])

# Calcula maior probabilidade de uma cor
maxProb = 0
limiar = 0

for i in range(256):
    prob = hist[i]/totalPixel

    if prob > maxProb:
        maxProb = prob
        limiar = i

print(limiar)

# Aplica o limiar
imgNova = np.zeros((h,w), np.uint8)
for i in range(h):
    for j in range(w):
        if img[i,j,0] >= limiar:
            imgNova[i,j] = 255


# Plot imagem
cv2.imshow("Imagem Original", img)
cv2.imshow("Limiar", imgNova)
plt.plot(hist,color = 'b')
plt.xlim([0,255])
plt.show()
cv2.waitKey(0)