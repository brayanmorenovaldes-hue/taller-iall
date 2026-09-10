import numpy as np

# ==========================================
# LABORATORIO FINAL: PROGRAMANDO UN KERNEL
# (Convolución / Filtro 3x3)
# ==========================================

print("\n" + "="*50)
print("=== TALLER 1: KERNEL DE CONVOLUCIÓN ===")
print("="*50)

# 1. Crear en NumPy las matrices "Sección de Imagen (I)" y "Kernel (K)"
I = np.array([
    [100, 100, 100],
    [100, 200, 100],
    [100, 100, 100]
], dtype=np.float32)

K = np.array([
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0]
], dtype=np.float32)

print("\n📸 Sección de Imagen (I):")
print(I)
print("\n🎯 Kernel de Afilado (K):")
print(K)

# 2. Calcular el valor central (Producto Hadamard e/ elemento y suma total)
producto_hadamard = I * K
print("\n🔢 Producto Hadamard (I * K):")
print(producto_hadamard)

pixel_central = np.sum(producto_hadamard)

# 3. Imprimir el resultado del píxel central
print(f"\n✅ Valor del píxel central calculado: {pixel_central}")

# 4. Interpretación del resultado
print("\n📊 Interpretación:")
print(f"   - El píxel central original era: 200")
print(f"   - Después del filtro de afilado: {int(pixel_central)}")
print(f"   - Este kernel aumenta el contraste en los bordes")

# 5. Explicación adicional
print("\n📖 Concepto:")
print("   La convolución es una operación fundamental en:")
print("   • Detección de características")
print("   • Filtrado de imágenes")
print("   • Redes neuronales convolucionales (CNNs)")
print("="*50)