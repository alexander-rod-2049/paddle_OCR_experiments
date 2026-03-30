# Plan de Exploración — PaddleOCR Learning Lab

El objetivo es aprender cómo funciona PaddleOCR por dentro. La secuencia es: primero entender la teoría de cada etapa, luego verificarla con código real.

---

## Estado actual de la sesión

- [x] Entorno configurado (GPU verificada, scripts base listos)
- [x] Objetivos clarificados: **aprender > performance**
- [ ] Explicación del pipeline (pendiente para próxima sesión)
- [ ] Experimentos (ver roadmap abajo)

---

## El Pipeline de PaddleOCR (próxima sesión: explicar antes de codear)

PaddleOCR encadena 3 modelos independientes. Entender cada uno por separado es la clave:

```
Imagen de entrada
      │
      ▼
┌─────────────────┐
│  1. DETECCIÓN   │  → Encuentra dónde hay texto (bounding boxes)
│  (DBNet)        │    Output: lista de polígonos/rectángulos
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 2. CLASIFICACIÓN│  → Corrige orientación del texto (0°, 90°, 180°...)
│  (opcional)     │    Output: imagen recortada y enderezada
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 3. RECONOCIMIENTO│ → Lee el texto dentro de cada región
│  (CRNN)         │    Output: string + confidence score
└─────────────────┘
```

**Preguntas que queremos responder con código:**
- ¿Qué pasa si desactivo la etapa de clasificación?
- ¿Qué produce cada etapa de forma aislada?
- ¿Por qué un confidence score es bajo en cierta imagen?

---

## Roadmap de Experimentos (ordenado por aprendizaje)

### Experimento 1 — Visualizar cada etapa por separado
**Qué aprende:** Cómo PaddleOCR divide el problema en 3 subproblemas.
**Cómo:** Correr solo `det` (detección), ver las bounding boxes. Luego solo `rec` (reconocimiento) sobre un recorte manual.
**Script a crear:** `scripts/pipeline_stages.py`

---

### Experimento 2 — Comparar modelos: mobile vs server
**Qué aprende:** El trade-off entre velocidad y precisión, y cuándo cada uno falla.
**Cómo:** Correr `det_model_dir` con el modelo `mobile` y luego con `server` sobre la misma imagen. Comparar outputs lado a lado.
**Script a crear:** `scripts/model_comparison.py`

---

### Experimento 3 — Entender el confidence score
**Qué aprende:** Qué hace que un score sea bajo — ¿la imagen? ¿el idioma? ¿la fuente?
**Cómo:** Pasar imágenes de calidades distintas (buena, comprimida, rotada, modo oscuro) y registrar los scores. Ver cuándo cae bajo 0.85.
**Script a crear:** `scripts/confidence_explorer.py`

---

### Experimento 4 — Detección de palabras clave (caso minero)
**Qué aprende:** Cómo usar el output de OCR para lógica de negocio real.
**Cómo:** Si el texto contiene `FALLA`, `INCIDENCIA` o `CRÍTICO` → imprimir MOCK ALERT. Filtrar por confidence antes de evaluar.
**Script a crear:** Extender `scripts/inference_web.py`

---

### Experimento 5 — Chino: impreso vs manuscrito
**Qué aprende:** Los límites del modelo `ch` con escritura a mano.
**Cómo:** Pasar imágenes de `data/samples_chinese/` con texto impreso y manuscrito. Comparar resultados.
**Requiere:** Imágenes de muestra en `data/samples_chinese/`

---

## Notas para retomar

- La explicación teórica del pipeline (diagrama + cada modelo) va **antes** del Experimento 1.
- Todos los scripts deben soportar `use_gpu=True/False` como parámetro.
- Los outputs se guardan en `outputs/` con nombre descriptivo (ej. `exp1_detection_only.json`).
