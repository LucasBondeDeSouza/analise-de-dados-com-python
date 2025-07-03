import cv2
import mediapipe as mp

# Inicializar o opencv e o mediapipe
webcam = cv2.VideoCapture(0)
soculao_reconhecimento_rosto = mp.solutions.face_detection
reconhecedor_rostos = soculao_reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils

while True:
    # Ler as informações da Webcam
    verificador, frame = webcam.read()

    if not verificador:
        break

    # Reconhecer os rostos que tem alí dentro
    lista_rostos = reconhecedor_rostos.process(frame)

    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            # Desenhar os rostos na imagem
            desenho.draw_detection(frame, rosto)

    cv2.imshow("Rostos na Webcam", frame)

    # Quando apertar ESC, para o loop
    if cv2.waitKey(5) == 27:
        break

webcam.release()