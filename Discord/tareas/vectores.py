puntajes_sentimiento = [0, 0, 0]

print("--- ANALIZADOR DE SENTIMIENTOS IA ---")

for i in range(5):
    voto = int(input(f"Palabra {i + 1} - Clasificación (0, 1, 2): "))
    if 0 <= voto <= 2:
        puntajes_sentimiento[voto] += 1

print(f"\nEstado final del vector de características: {puntajes_sentimiento}")

valor_maximo = puntajes_sentimiento[0]
indice_ganador = 0

for j in range(1, 3):
    if puntajes_sentimiento[j] > valor_maximo:
        valor_maximo = puntajes_sentimiento[j]
        indice_ganador = j

if indice_ganador == 0:
    print("Resultado de IA: La frase es Positiva")
elif indice_ganador == 1:
    print("Resultado de IA: La frase es Neutral")
else:
    print("Resultado de IA: La frase es Negativa")