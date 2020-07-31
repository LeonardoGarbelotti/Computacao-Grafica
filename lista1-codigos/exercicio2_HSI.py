import cv2
import numpy as np
import math

# LER IMAGEM
img = np.float32(cv2.imread("mulher.jpg"))/255
img2 = cv2.imread("mulher.jpg")
h,w = img.shape[:2]
hnew = int(h/2)
wnew = int(w/2)

# Pegar os pixeis RGB
azul = img[:,:,0] #valor do canal azul
verde = img[:,:,1] # valor do canal verde
vermelho = img[:,:,2] #valor do canal vermelho

# Calcular Intensidade
intensidade = ((vermelho + verde + azul)/3)

# Calcular Saturação
minimo = np.minimum(np.minimum(vermelho, verde), azul)
saturacao = 1 - (3 / (vermelho + verde + azul + 0.001)* minimo) # 0.001-> resolver um problema de divisao por 0

# Calcular Matriz

with np.errstate(divide='ignore', invalid='ignore'): # pra ignorar o \ pra dar uma pulada de linha

    matriz = np.copy(vermelho)

    for i in range(0, azul.shape[0]):
        for j in range(0, azul.shape[1]):
            matriz[i][j] = 0.5 * ((vermelho[i][j] - verde[i][j]) + (vermelho[i][j] - azul[i][j])) / \
                    math.sqrt((vermelho[i][j] - verde[i][j])**2 + 
                     ((vermelho[i][j] - azul[i][j]) * (verde[i][j] - azul[i][j])))
            matriz[i][j] = math.acos(matriz[i][j])

            if azul[i][j] <= verde[i][j]:
                matriz[i][j] = matriz[i][j]
            else:
                matriz[i][j] = ((360 * math.pi) / 180.0) - matriz[i][j]

# Juntar os canais na imagem

img[:,:, 0] = matriz
img[:,:, 1] = saturacao
img[:,:, 2] = intensidade

# Conversão HSL
hslImg = cv2.cvtColor(img2, cv2.COLOR_RGB2HLS)

# REDIMENSIONAR IMAGEM
resizedImg = cv2.resize(img, (wnew, hnew), interpolation=cv2.INTER_AREA)
resizedImg2 = cv2.resize(hslImg, (wnew, hnew), interpolation=cv2.INTER_AREA)

# PLOTAR IMAGENS
cv2.imshow("HSI", resizedImg)
cv2.imshow("HSL OPENCV", resizedImg2)


cv2.waitKey(0)