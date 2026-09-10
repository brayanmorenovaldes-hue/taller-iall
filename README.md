# Taller IALL - Procesamiento de Imágenes con OpenCV

Laboratorio educativo de procesamiento digital de imágenes usando Python, NumPy y OpenCV.

## 📚 Contenido de Talleres

### Taller 1: Kernel de Convolución (Filtro 3×3)
**Archivo:** `taller1.py`

Implementa la operación fundamental de convolución usando:
- Matrices NumPy
- Producto de Hadamard (elemento a elemento)
- Kernels de filtrado

**Conceptos:**
- Operaciones matriciales
- Filtros de imagen
- Detección de características

---

### Taller 2: Conversión a Escala de Grises
**Archivo:** `taller2.py`

Demuestra dos métodos de conversión de color a gris:
- **Método manual:** Fórmula de luminancia estándar (ITU-R BT.601)
- **Método optimizado:** Función nativa de OpenCV

**Fórmula utilizada:**
```
Gris = 0.114×Azul + 0.587×Verde + 0.299×Rojo
```

**Conceptos:**
- Espacios de color (BGR, Gris)
- Producto punto ponderado
- Percepción de luminancia

---

### Taller 3: Análisis de Histogramas de Canales
**Archivo:** `taller3_histograma.py`

Visualiza la distribución de intensidades en cada canal de color (BGR).

**Características:**
- ✅ Función reutilizable y documentada
- ✅ Manejo robusto de errores
- ✅ Opción para guardar o mostrar gráficas
- ✅ Información clara de salida

**Uso:**

```bash
# Opción 1: Ejecutar directamente (busca 'foto.jpg')
python taller3_histograma.py

# Opción 2: Usar la función en otro script
from taller3_histograma import analizar_histograma

# Mostrar en pantalla
analizar_histograma('mi_imagen.jpg', guardar=False)

# Guardar como PNG
analizar_histograma('mi_imagen.jpg', guardar=True)
```

**Interpretación de histogramas:**
| Patrón | Significado |
|--------|------------|
| Pico en 255 (canal rojo) | Imagen muy roja/cálida |
| Pico en 0 (todos los canales) | Imagen muy oscura |
| Distribución plana | Colores variados, buena exposición |
| Doble pico | Alto contraste (claros vs. oscuros) |
| Verde más alto | Influencia de iluminación natural |

**Conceptos:**
- Análisis de distribución de color
- Histogramas en visión por computadora
- Detección de exposición/contraste

---

## 🛠️ Instalación

### Requisitos
- Python 3.7+
- pip

### Dependencias

```bash
# Instalar desde requirements.txt
pip install -r requirements.txt
```

**Packages incluidos:**
- `opencv-python` - Procesamiento de imágenes
- `numpy` - Operaciones matriciales
- `matplotlib` - Visualización de gráficas

---

## 📋 Instrucciones de Uso

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/brayanmorenovaldes-hue/taller-iall.git
   cd taller-iall
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar un taller:**
   ```bash
   python taller1.py    # Convolución
   python taller2.py    # Escala de grises
   python taller3_histograma.py  # Histogramas
   ```

4. **Para usar con tus propias imágenes:**
   - Coloca tu imagen en la carpeta del proyecto
   - Modifica la ruta en el script
   - Ejecuta el archivo

---

## 📊 Aplicaciones Prácticas

✅ **Preprocesamiento de datos** para machine learning  
✅ **Detección de características** en visión por computadora  
✅ **Ajuste automático** de exposición y contraste  
✅ **Clasificación de imágenes** basada en características de color  
✅ **Compresión y filtrado** de imágenes

---

## 🔍 Próximas Mejoras

- [ ] Taller 4: Detección de bordes (Sobel, Canny)
- [ ] Taller 5: Filtros gaussianos y blur
- [ ] Taller 6: Transformaciones morfológicas
- [ ] Taller 7: Procesamiento en tiempo real (webcam)
- [ ] Ejemplos con datasets reales

---

## 📝 Notas Importantes

- **OpenCV lee imágenes en BGR**, no en RGB
- Los histogramas son herramientas clave para entender la calidad de la imagen
- Todos los scripts incluyen manejo de errores
- Cada taller es independiente y puede ejecutarse por separado

---

## 📧 Autor

**Brayan Moreno Valdés**  
Proyecto educativo - Laboratorio de Procesamiento de Imágenes

---

## 📄 Licencia

Este proyecto es de código abierto para fines educativos.
