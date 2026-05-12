print("--- MÓDULO DE SENSORES (VECTORES) ---")

sensores_distancia = []
suma = 0

for i in range(5):
    distancia = float(input(f"Ingrese distancia sensor {i+1}: "))
    sensores_distancia.append(distancia)
    suma += distancia

promedio = suma / 5

if promedio < 2.0:
    print("Aviso: Reduciendo velocidad global")

print("\n--- MÓDULO DE VISIÓN (MATRICES) ---")

camara_ia = []

for fila in range(3):
    fila_actual = []
    
    for columna in range(3):
        brillo = int(input(f"Fila {fila}, Col {columna} (Brillo 0-255): "))
        
        if brillo > 255:
            brillo = 255
        
        fila_actual.append(brillo)
    
    camara_ia.append(fila_actual)

for fila in camara_ia:
    print(fila)

contador_brillantes = 0

for fila in range(3):
    for columna in range(3):
        if camara_ia[fila][columna] > 200:
            contador_brillantes += 1

print("\nResultado de Análisis IA:")
print(f"Se detectaron {contador_brillantes} píxeles de alta intensidad.")