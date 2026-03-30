# Project: PaddleOCR Exploration Lab

Entorno de aprendizaje para entender cómo funciona PaddleOCR: su pipeline, sus modelos y sus capacidades. La integración en proyectos productivos (monitoreo minero, asistente de chino) es el horizonte, pero **aprender es el objetivo principal**. La performance es secundaria.

---

## Objetivo General

**Aprender PaddleOCR**: entender su pipeline, qué hace cada etapa, qué modelos usa y por qué. Cada experimento debe responder una pregunta concreta sobre cómo funciona la herramienta. La performance (GPU vs CPU, latencia) es un eje secundario, no el foco.

---

## Proyectos Destino

| # | Proyecto | Prioridad | Caso de uso OCR |
|---|----------|-----------|-----------------|
| 1 | **Web Monitor Minero** | Alta | Leer capturas de pantalla de UIs web (tablas, alertas, KPIs) |
| 2 | **Asistente de Chino** | Media | Reconocer caracteres escritos a mano y dictados |

---

## Stack

- **OS**: WSL2 Ubuntu
- **Python**: 3.12
- **Engine**: PaddlePaddle 2.6.0 (Fluid)
- **GPU**: RTX 3050 (`gpu:0` — verificado y funcional)
- **CPU fallback**: i5-13420H (para entornos sin GPU)
- **Git**: rodrigo.engr.lang@gmail.com

El código debe soportar modo dual: `use_gpu=True` para procesamiento local rápido, `use_gpu=False` para portabilidad a servidores o laptops de colegas.

---

## Ejes de Exploración

### 1. Versatilidad Lingüística
Comparar precisión entre caracteres latinos (Español/Inglés) y logogramas (Chino simplificado y tradicional).

### 2. Sensibilidad de Hardware
Medir latencia y throughput alternando GPU vs CPU para determinar el trade-off real.

### 3. Robustez Visual
Probar el comportamiento ante:
- Capturas de baja resolución o con modo oscuro
- Texto manuscrito (dictados de chino)
- Texto rotado o en ángulos no estándar

### 4. Extracción de Metadata
Ir más allá del texto crudo: evaluar la utilidad de **bounding boxes** y **confidence scores** para filtrado y alertas automatizadas.

---

## Roadmap de Experimentos

### Fase 1 — Visión Web (Proyecto Minero)
- [ ] Inferencia básica sobre capturas reales con `inference_web.py`
- [ ] Análisis de estructura: ¿mantiene el orden de lectura en tablas complejas?
- [ ] Prueba de ruido: sombras, modo oscuro, compresión JPEG
- [ ] Detección de palabras clave (`INCIDENCIA`, `FALLA`, `CRÍTICO`) → MOCK ALERT
- [ ] Filtrar resultados con confidence < 0.85

### Fase 2 — Escritura y Chino (Proyecto Personal)
- [ ] Reconocimiento de trazos con el modelo `ch` (handwriting)
- [ ] Mapear output de Paddle a significados (mini-diccionario)

---

## Estado Actual

- GPU verificada y operativa.
- Imagen de prueba: `data/samples_web/test_web.png`
- Scripts disponibles: `test_gpu.py`, `inference_web.py`, `basic_inference.py`

> El plan detallado de experimentos y el estado de progreso vive en [EXPLORATION_PLAN.md](EXPLORATION_PLAN.md). Ese es el archivo a abrir al retomar una sesión.

---

## Estructura del Repositorio

```
paddle_OCR_experiments/
├── data/
│   ├── samples_web/       # Capturas de pantalla de UIs web
│   └── samples_chinese/   # Imágenes con caracteres chinos
├── scripts/               # Scripts de inferencia y utilidades
├── outputs/               # Resultados crudos (JSON + imágenes anotadas)
└── PROJECT_CONTEXT.md
```
