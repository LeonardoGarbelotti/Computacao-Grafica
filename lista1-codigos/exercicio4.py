import cv2
from math import log2

# Otsu implementado manualmente
def otsu():
    img = cv2.imread("papagaio.jpg", 0) # 0 -> cinza
    h, w = img.shape[:2]
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])

    l = 256
    mediaTotal = 0.0
    varTotal = 0.00001
    media_t = 0.0
    w0 = 0.00000000001
    n = -1
    max = -1
    pos = -1

    for t in range(l):
        for i in range(t):
            Pi = hist[i] / (h * w)
            w0 = w0 + Pi
            media_t = media_t + i * Pi
        Pi = hist[t] / (h * w)
        mediaTotal = mediaTotal + t * Pi
        w1 = 1 - w0
        u0 = media_t / w0
        u1 = mediaTotal - media_t / (1 - u0)
        varClasses = w0 * w1 * pow((u1 * u0), 2)
        n = varClasses / varTotal
        if n > max:
            max = n
            pos = t
    return mediaTotal


# LER IMAGEM
imgO = cv2.imread("papagaio.jpg")
img = cv2.imread("papagaio.jpg", 0)
h,w = img.shape[:2]
otsuTh = otsu()

# Otsu Threshold Manual
th, res2 = cv2.threshold(img, otsuTh, 255, cv2.THRESH_BINARY)

# Otsu Threshold OPENCV
th, res = cv2.threshold(img,0,255, cv2.THRESH_OTSU)

# Plot imagem
cv2.imshow("Original", imgO)
cv2.imshow("Otsu Threshold OPENCV", res)
cv2.imshow("Otsu Threshold", res2)
cv2.waitKey(0)  
