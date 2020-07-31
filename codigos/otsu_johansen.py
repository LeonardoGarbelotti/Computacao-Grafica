import cv2
from math import log2


def johansen():
    img = cv2.imread("papagaio.jpg", 0) # 0 -> cinza
    h, w = img.shape[:2]
    hist = cv2.calcHist([img], [0], None, [256], [0, 256]) #calcula o histograma da imagem

    l = 256
    somaProbabilidades = 0.00000001
    entropiaTotal = 0.00000001
    somatorioIntermediario = 0.00000001
    minimo = 257
    pos = -1
    sbt = 0.0
    swt = 0.0
    for t in range(l):
        if t == 0:
            entropiaAtual = ((t + 0.000001) * -1) * log2(t + 0.000001)
        else:
            entropiaAtual = (t * -1) * log2(t)
        for i in range(t-1):
            Pi = hist[i] / (h * w)
            somaProbabilidades = somaProbabilidades + Pi
            entropiaTotal = (-somaProbabilidades) * log2(somaProbabilidades)
        j = t
        while j < 255:
            Pj = hist[j] / (h * w)
            somatorioIntermediario = somatorioIntermediario + Pj
            j += 1
        sbt = log2(somaProbabilidades) + ((1 / somaProbabilidades) * (entropiaAtual + entropiaTotal))
        swt = log2(somatorioIntermediario) + ((1 / somatorioIntermediario) * (entropiaAtual + entropiaTotal))

        res = min(sbt + swt)
        if res < minimo:
            minimo = res
            pos = t
    return somaProbabilidades


def otsu():
    img = cv2.imread("papagaio.jpg", 0) # 0 -> cinza
    h, w = img.shape[:2]
    hist = cv2.calcHist([img], [0], None, [256], [0, 256]) #histograma

    #variaveis
    l = 256
    mediaTotal = 0.0
    varTotal = 0.00001
    media_t = 0.0
    w0 = 0.00000000001
    n = -1
    max = -1
    pos = -1

    # calculos
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


img = cv2.imread("papagaio.jpg", 0) # abre imagem
otsuTh = otsu() # funcao do otsu threshold
johansenTh = johansen() # funcao do johansen threshold

th, res = cv2.threshold(img, otsuTh, 255, cv2.THRESH_BINARY)
th, res2 = cv2.threshold(img, johansenTh, 255, cv2.THRESH_BINARY)
cv2.imshow("Original", img)
cv2.imshow("Otsu Threshold", res)
cv2.imshow("Johansen Threshold", res2)
cv2.waitKey(0)