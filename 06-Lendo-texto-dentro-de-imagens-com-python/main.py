import pytesseract
import cv2

# Passo 1: Ler a imagem
imagem = cv2.imread("print_magalu.JPG")

caminho = r"C:\Users\mariaapsouza\AppData\Local\Programs\Tesseract-OCR"

# Passo 2: Pedir para o tesseract extrair o texto da imagem
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
texto = pytesseract.image_to_string(imagem, lang="por")

print(texto)