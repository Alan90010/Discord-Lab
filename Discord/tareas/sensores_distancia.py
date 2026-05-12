print("--- MÓDULO DE SENSORES (VECTORES) ---")

sensores_distancia = []
for i in range(5):
    distancia = float(input(f"Ingrese distancia sensor {i + 1}: "))
    sensores_distancia.append(distancia)

promedio_distancia = sum(sensores_distancia) / 5
print(f"Promedio de proximidad: {promedio_distancia}m.")

if promedio_distancia < 2.0:
    print("Aviso: Reduciendo velocidad global")
else:
    print("Estado: Seguro.")

print("\n--- MÓDULO DE VISIÓN (MATRICES) ---")
print("Llenando matriz de cámara 3x3:")

camara_ia = []
for f in range(3):
    fila = []
    for c in range(3):
        brillo = int(input(f"Fila {f}, Col {c} (Brillo 0-255): "))
        
        if brillo > 255:
            brillo = 255
            
        fila.append(brillo)
    camara_ia.append(fila)

print("\nVisualización de la imagen capturada:")
for fila in camara_ia:
    print(fila)

puntos_brillantes = 0
for fila in camara_ia:
    for pixel in fila:
        if pixel > 200:
            puntos_brillantes = puntos_brillantes + 1

print("\nResultado de Análisis IA:")
print(f"Se detectaron {puntos_brillantes} píxeles de alta intensidad.")