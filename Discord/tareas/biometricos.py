patron_maestro = [1, 0, 1, 1, 0]
lectura_sensor = []

print("--- ESCÁNER BIOMÉTRICO DE IA ---")

for i in range(5):
    bit = int(input(f"Ingrese bit {i + 1}: "))
    lectura_sensor.append(bit)

coincidencias = 0
for i in range(5):
    if lectura_sensor[i] == patron_maestro[i]:
        coincidencias += 1

porcentaje_similitud = (coincidencias / 5) * 100

print("\n> Comparando lectura con base de datos...")
print(f"> Coincidencias encontradas: {coincidencias}")
print(f"> Porcentaje de Similitud: {porcentaje_similitud}%")

print(f"\nPatrón Maestro: {patron_maestro}")
print(f"Lectura Sensor: {lectura_sensor}")

if porcentaje_similitud == 100:
    print("ESTADO: ACCESO TOTAL: Identidad Verificada.")
elif porcentaje_similitud >= 60:
    print("ESTADO: ADVERTENCIA: Similitud parcial. Se requiere verificación manual.")
else:
    print("ESTADO: ALERTA: Intruso detectado. Sistema bloqueado.")