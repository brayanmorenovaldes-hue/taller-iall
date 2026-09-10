import cv2
import matplotlib.pyplot as plt
import os

def analizar_histograma(ruta_imagen, guardar=True):
    """
    Analiza y visualiza el histograma de canales BGR de una imagen.
    
    Parámetros:
        ruta_imagen (str): Ruta a la imagen a analizar
        guardar (bool): Si True, guarda la gráfica; si False, la muestra en pantalla
    
    Retorna:
        bool: True si el análisis fue exitoso, False en caso de error
    """
    
    if not os.path.exists(ruta_imagen):
        print(f"❌ Error: '{ruta_imagen}' no encontrado")
        return False
    
    imagen = cv2.imread(ruta_imagen)
    
    if imagen is None:
        print("❌ Error: No se pudo leer la imagen")
        return False
    
    # Configurar colores y etiquetas para los canales BGR
    colores = ('b', 'g', 'r')
    etiquetas = ('Canal Azul', 'Canal Verde', 'Canal Rojo')
    
    # Crear figura
    plt.figure(figsize=(12, 5))
    
    # Calcular y graficar histograma de cada canal
    for i, col in enumerate(colores):
        hist = cv2.calcHist([imagen], [i], None, [256], [0, 256])
        plt.plot(hist, color=col, label=etiquetas[i], linewidth=2)
    
    # Configurar gráfica
    plt.title(f"Histograma: {os.path.basename(ruta_imagen)}", fontsize=14, fontweight='bold')
    plt.xlabel("Valor del Píxel (0 - 255)", fontsize=12)
    plt.ylabel("Frecuencia (Cantidad de Píxeles)", fontsize=12)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.xlim([0, 256])
    
    # Guardar o mostrar
    if guardar:
        nombre_salida = ruta_imagen.rsplit('.', 1)[0] + '_histograma.png'
        plt.savefig(nombre_salida, dpi=150, bbox_inches='tight')
        print(f"✅ Histograma guardado como: '{nombre_salida}'")
    else:
        plt.show()
    
    plt.close()
    return True


# ==========================================
# USO DEL SCRIPT
# ==========================================

if __name__ == "__main__":
    # Opción 1: Analizar una imagen específica
    imagen_path = 'foto.jpg'
    
    print("Iniciando análisis de histograma...")
    print(f"Buscando imagen: {imagen_path}\n")
    
    # Ejecutar análisis (guardar=True para guardar, guardar=False para mostrar)
    exito = analizar_histograma(imagen_path, guardar=True)
    
    if exito:
        print("\n✅ Análisis completado exitosamente")
    else:
        print("\n⚠️  Verifica que 'foto.jpg' esté en la misma carpeta que este script")
