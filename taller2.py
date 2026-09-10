import cv2
import numpy as np
import os

def convertir_a_gris(ruta_imagen, mostrar=True):
    """
    Convierte una imagen a escala de grises usando dos métodos.
    
    Parámetros:
        ruta_imagen (str): Ruta a la imagen
        mostrar (bool): Si True, muestra la imagen; si False, solo procesa
    
    Retorna:
        tuple: (imagen_original, imagen_gris) o (None, None) si falla
    """
    
    if not os.path.exists(ruta_imagen):
        print(f"❌ Error: '{ruta_imagen}' no encontrado")
        return None, None
    
    imagen = cv2.imread(ruta_imagen)
    
    if imagen is None:
        print("❌ Error: No se pudo leer la imagen")
        return None, None
    
    print(f"\n✅ Imagen cargada: {ruta_imagen}")
    print(f"   Dimensiones: {imagen.shape}")
    
    # ==========================================
    # MÉTODO 1: Conversión Manual
    # ==========================================
    print("\n📊 MÉTODO 1: Conversión Manual")
    print("-" * 40)
    
    # Extraer canales BGR
    canal_azul = imagen[:, :, 0].astype(np.float32)
    canal_verde = imagen[:, :, 1].astype(np.float32)
    canal_rojo = imagen[:, :, 2].astype(np.float32)
    
    # Aplicar pesos según ITU-R BT.601
    pesos = np.array([0.114, 0.587, 0.299])
    img_gris_manual = (0.114 * canal_azul + 
                       0.587 * canal_verde + 
                       0.299 * canal_rojo).astype(np.uint8)
    
    print(f"Fórmula: Gris = 0.114×Azul + 0.587×Verde + 0.299×Rojo")
    print(f"Resultado: {img_gris_manual.shape}")
    
    # ==========================================
    # MÉTODO 2: Conversión con OpenCV
    # ==========================================
    print("\n🔧 MÉTODO 2: Función Optimizada OpenCV")
    print("-" * 40)
    
    img_gris_cv2 = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    print(f"Función: cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)")
    print(f"Resultado: {img_gris_cv2.shape}")
    
    # Comparar diferencias
    diferencia = cv2.absdiff(img_gris_manual, img_gris_cv2)
    print(f"\n📈 Comparación: Diferencia máxima = {np.max(diferencia)}")
    print(f"   (valores cercanos a 0 indican métodos equivalentes)")
    
    # ==========================================
    # VISUALIZACIÓN
    # ==========================================
    if mostrar:
        print("\n🖼️  Mostrando resultados...")
        
        fig, axes = plt.subplots(1, 3, figsize=(15, 4))
        
        # Original (convertir BGR a RGB para visualización)
        axes[0].imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
        axes[0].set_title("Original (BGR)")
        axes[0].axis("off")
        
        # Manual
        axes[1].imshow(img_gris_manual, cmap='gray')
        axes[1].set_title("Manual (ITU-R BT.601)")
        axes[1].axis("off")
        
        # OpenCV
        axes[2].imshow(img_gris_cv2, cmap='gray')
        axes[2].set_title("OpenCV (COLOR_BGR2GRAY)")
        axes[2].axis("off")
        
        plt.tight_layout()
        plt.show()
    
    return imagen, img_gris_cv2


# ==========================================
# EJEMPLO DE PÍXEL
# ==========================================
print("\n" + "="*50)
print("=== TALLER 2: CONVERSIÓN A ESCALA DE GRISES ===")
print("="*50)

print("\n📌 EJEMPLO: Píxel Amarillo Puro")
print("-" * 40)

pixel = np.array([0, 255, 255], dtype=np.float32)  # Amarillo en BGR
pesos = np.array([0.114, 0.587, 0.299])
gris_calculado = np.dot(pixel, pesos)

print(f"Píxel BGR: [{pixel[0]}, {pixel[1]}, {pixel[2]}] (Amarillo puro)")
print(f"Pesos: [0.114, 0.587, 0.299]")
print(f"Gris = 0×0.114 + 255×0.587 + 255×0.299")
print(f"Gris = 0 + 149.685 + 76.245")
print(f"\n✅ Valor final: {gris_calculado:.2f} (tono de gris muy claro)")

# ==========================================
# PROCESAR IMAGEN REAL
# ==========================================
print("\n" + "="*50)
print("=== PROCESAMIENTO DE IMAGEN REAL ===")
print("="*50)

import matplotlib.pyplot as plt

ruta = 'imagen.jpg'  # Cambia esto a tu imagen
img_original, img_gris = convertir_a_gris(ruta, mostrar=False)

if img_original is not None:
    print("\n✅ Proceso completado exitosamente")
else:
    print("\n⚠️  Por favor, coloca una imagen llamada 'imagen.jpg' en esta carpeta")

print("\n" + "="*50)
