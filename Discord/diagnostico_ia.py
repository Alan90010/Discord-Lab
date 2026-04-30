import math

def imprimir_encabezado():
    print("====================================")
    print("    SISTEMA DE SALUD INTELIGENTE    ")
    print("====================================")

def calcular_imc(peso, estatura):
    return peso / (estatura ** 2)

def evaluar_presion(presion_sistolica):
    if presion_sistolica > 140:
        return "Alta"
    else:
        return "Normal"

imprimir_encabezado()

nombre = input("Nombre del Paciente: ")
peso = float(input("Peso (kg): "))
estatura = float(input("Estatura (m): "))
presion = float(input("Presión Sistólica: "))

resultado_imc = calcular_imc(peso, estatura)
estado_presion = evaluar_presion(presion)
imc_redondeado = math.ceil(resultado_imc)

print("\n--- RESULTADOS DEL ANÁLISIS ---")
print("Paciente:", nombre)
print("IMC Calculado:", imc_redondeado)
print("Estado de Presión:", estado_presion)
print("-------------------------------")