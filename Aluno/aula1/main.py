import cv2
import numpy as np

# Função para evitar paradas por erros
def nothing(x):
    pass

# Execução da câmera
cap = cv2.VideoCapture(0)

# criação da janela
cv2.namedWindow('trackbars')

# create trackbars

cv2.createTrackbar('l-h', 'trackbars', 0, 179, nothing)
cv2.createTrackbar('l-s', 'trackbars', 1, 255, nothing)
cv2.createTrackbar('l-v', 'trackbars', 0, 255, nothing)
cv2.createTrackbar('u-h', 'trackbars', 255, 255, nothing)
cv2.createTrackbar('u-s', 'trackbars', 255, 255, nothing)
cv2.createTrackbar('u-v', 'trackbars', 255, 255, nothing)

# loop
while (True):
    # leitura do frame
    ret, frame = cap.read()

    #pega os valores das trackbars

    l_h  = cv2.getTrackbarPos('l-h', 'trackbars')
    l_s  = cv2.getTrackbarPos('l-s', 'trackbars')
    l_v  = cv2.getTrackbarPos('l-v', 'trackbars')
    u_h  = cv2.getTrackbarPos('u-h', 'trackbars')
    u_s  = cv2.getTrackbarPos('u-s', 'trackbars')
    u_v  = cv2.getTrackbarPos('u-v', 'trackbars')

    # Array Numpy Lower upper
    lower = np.array([l_h, l_s, l_v])
    upper = np.array([u_h, u_s, u_v])

    # Criando HSV

    hsv = cv2.cvtColor(frame , cv2.COLOR_RGB2HSV)
     
    # criar mask
    
    mask = cv2.inRange(hsv, lower, upper) 

    # Eibir frame original
    cv2.imshow('frame', frame)

    # Exibir mask
    #cv2.imshow('mask', mask)
    #criar resultdo

    result = cv2.bitwise_and(frame, frame, mask = mask)  
    
    # Eibir resultado
    cv2.imshow('result', result)


    # Waitkey
    if cv2.waitKey(1) & 0xFF == ord('s'):
       break
# Finalização
cap.release()
cv2.destroyAllWindows()      

'''import cv2
import numpy as np

# Função vazia para o retorno das trackbars
def nothing(x):
    pass

# Inicialização da câmera
cap = cv2.VideoCapture(0)

# Criação da janela das trackbars
cv2.namedWindow('trackbars')

# Criação das trackbars (H de 0 a 179, S e V de 0 a 255)
cv2.createTrackbar('l-h', 'trackbars', 0, 179, nothing)
cv2.createTrackbar('l-s', 'trackbars', 0, 255, nothing)
cv2.createTrackbar('l-v', 'trackbars', 0, 255, nothing)
cv2.createTrackbar('u-h', 'trackbars', 179, 179, nothing)
cv2.createTrackbar('u-s', 'trackbars', 255, 255, nothing)
cv2.createTrackbar('u-v', 'trackbars', 255, 255, nothing)

while True:
    # 1. Leitura do frame
    ret, frame = cap.read()
    if not ret:
        break

    # 2. Pegar os valores atuais das trackbars
    l_h = cv2.getTrackbarPos('l-h', 'trackbars')
    l_s = cv2.getTrackbarPos('l-s', 'trackbars')
    l_v = cv2.getTrackbarPos('l-v', 'trackbars')
    u_h = cv2.getTrackbarPos('u-h', 'trackbars')
    u_s = cv2.getTrackbarPos('u-s', 'trackbars')
    u_v = cv2.getTrackbarPos('u-v', 'trackbars')

    # 3. Definir os limites usando Numpy Arrays (CORREÇÃO AQUI)
    lower = np.array([l_h, l_s, l_v])
    upper = np.array([u_h, u_s, u_v])

    # 4. Converter o frame original de BGR para HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 5. Criar a máscara (mask) que filtra as cores dentro do intervalo
    mask = cv2.inRange(hsv, lower, upper)

    # 6. Aplicar a máscara no frame original para ver a cor real filtrada (opcional)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # 7. Exibir as janelas
    cv2.imshow('Frame Original', frame)
    cv2.imshow('Mascara (Preto e Branco)', mask)
    cv2.imshow('Resultado (Colorido)', result)

    # Sair ao pressionar 's' ou 'ESC'
    key = cv2.waitKey(1)
    if key == ord('s') or key == 27:
        break

# Finalização
cap.release()
cv2.destroyAllWindows()'''