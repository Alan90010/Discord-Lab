class MonitorEntrenamiento:
    def __init__(self, umbral=0.01):
        self.historial_errores = []
        self.umbral_convergencia = umbral

    def registrar_epoca(self, valor_error):
        if valor_error < self.umbral_convergencia:
            print("[SISTEMA] Entrenamiento completado: Se alcanzó el objetivo de precisión.")
        
        self.historial_errores.append(valor_error)

print("--- Iniciando Monitor de Red Neuronal ---")
monitor = MonitorEntrenamiento(0.01)
contador = 0

while contador < 5:
    entrada = input("Ingrese el error de la Época " + str(contador + 1) + ": ")

    if entrada.replace('.', '', 1).isdigit():
        valor = float(entrada)
        monitor.registrar_epoca(valor)
        print("> Registro exitoso.")
        contador = contador + 1
        
        if valor < monitor.umbral_convergencia:
            break
    else:
        print("> [ERROR] Entrada inválida. Por favor, ingrese un número decimal.")

print("\n--- Resumen de Entrenamiento ---")
historial = monitor.historial_errores

if len(historial) > 0:
    promedio = sum(historial) / len(historial)
    mejor = min(historial)
    
    print("Historial:", historial)
    print("Promedio de Error:", promedio)
    print("Mejor resultado obtenido:", mejor)