import os
from paddleocr import PaddleOCR

# Inicializar OCR con soporte en español y GPU
ocr = PaddleOCR(use_angle_cls=True, lang='es', use_gpu=True)

img_path = 'data/samples_web/test_web.png'

print(f"--- Iniciando OCR en: {img_path} ---")

if not os.path.exists(img_path):
    print(f"Error: No encontré la imagen en {img_path}")
else:
    # Ejecutar inferencia
    result = ocr.ocr(img_path, cls=True)

    # Procesar resultados
    for idx in range(len(result)):
        res = result[idx]
        if res is None: 
            print("No se detectó texto en la imagen.")
            break
            
        for line in res:
            coords = line[0]     # Caja delimitadora
            text = line[1][0]    # Texto detectado
            conf = line[1][1]    # Nivel de confianza (0.0 a 1.0)
            
            # Formateo para lectura rápida
            status = "✅" if conf > 0.85 else "⚠️"
            print(f"{status} [{conf:.2f}] -> {text}")

print("--- Fin del proceso ---")