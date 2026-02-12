import cv2

# Carregar imagem (o caminho deve estar correto)
img = cv2.imread('imagem.jpg')

# Mostrar numa janela
cv2.imshow('Titulo da Janela', img)

# Esperar qualquer tecla para fechar
cv2.waitKey(0)
cv2.destroyAllWindows()


#2. acessar à Webcam

import cv2

cap = cv2.VideoCapture(0) # '0' é a webcam padrão

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Video ao Vivo', frame)

    # Sai ao pressionar a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Converter para Escala de Cinza
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#exemplos no git
#https://github.com/opencv/opencv/tree/master/samples/python