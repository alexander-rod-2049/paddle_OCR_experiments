from paddleocr import PaddleOCR, draw_ocr

# Inicializar PaddleOCR (usando GPU y soporte para Chino y Inglés)
ocr = PaddleOCR(use_angle_cls=True, lang='ch', use_gpu=True) 

img_path = './data/samples_chinese/test_1.jpg'
result = ocr.ocr(img_path, cls=True)

for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(f"Texto detectado: {line[1][0]} - Confianza: {line[1][1]}")