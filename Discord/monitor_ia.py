print("--- TELEMETRÍA DE CLUSTER IA ---")

temp = float(input("Temperatura actual (°C): "))
vram = int(input("Uso de Memoria VRAM (%): "))
enfriamiento = input("¿Enfriamiento activo? (si/no): ").strip().lower()

if vram < 0 or vram > 100:
    print("> Diagnóstico: Error: Lectura de memoria fuera de rango (0-100%).")

elif temp > 90 or vram == 100:
    print("> Diagnóstico: ¡ALERTA CRÍTICA! Apagando servidores para evitar daños físicos.")

elif 75 <= temp <= 90:
    if enfriamiento == "no":
        print("> Diagnóstico: Peligro: Temperatura alta y enfriamiento desactivado. Pausando entrenamiento.")
    else:
        print("> Diagnóstico: Temperatura elevada. Reduciendo velocidad de procesamiento (Throttling).")

elif temp < 75 and vram < 80:
    vram_libre = 100 - vram
    print("> Diagnóstico: Sistema Estable: Entrenamiento en curso a máxima capacidad.")
    print(f"VRAM libre para otros modelos: {vram_libre}%")