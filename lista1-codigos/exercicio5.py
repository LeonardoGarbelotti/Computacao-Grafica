import cv2


# LER IMAGEM
img = cv2.imread("flor.jpg")

# Aplica o filtro da mediana
mediana_3x3 = cv2.medianBlur(img, 3)
mediana_5x5 = cv2.medianBlur(img, 5)
mediana_7x7 = cv2.medianBlur(img, 7)


# Plot imagem
cv2.imshow("Imagem Original", img)
cv2.imshow("Mediana 3x3", mediana_3x3)
cv2.imshow("Mediana 5x5", mediana_5x5)
cv2.imshow("Mediana 7x7", mediana_7x7)
cv2.waitKey(0)

