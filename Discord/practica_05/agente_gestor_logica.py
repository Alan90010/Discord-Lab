import agente_logica as logica

def comando_sumar(argumento):
    return logica.ejecutar_suma(argumento)
 
def comando_multiplicar(argumento):
    return logica.ejecutar_multiplicacion(argumento)
 
def comando_definir(argumento):
    return logica.buscar_en_diccionario(argumento)
 
def comando_validar(argumento):
    return logica.validar_variable(argumento)
 
def comando_fecha(argumento):
    return logica.obtener_fecha_completa()
 
def comando_historial(argumento):
    if not logica.historial_comandos:
        return "Aún no hay comandos registrados."
    res = "Últimos comandos ejecutados:\n"
    for i, cmd in enumerate(logica.historial_comandos, 1):
        res += f"{i}. {cmd}\n"
    return res
 
def comando_libre(entrada_completa):
    return logica.analizar_comando(entrada_completa)
 
COMANDOS_DISPONIBLES = {
    "!sumar": comando_sumar,
    "!multiplicar": comando_multiplicar,
    "!definir": comando_definir,
    "!validar": comando_validar,
    "!fecha": comando_fecha,
    "!historial": comando_historial,
}

def gestionar_comando(entrada_usuario):
    entrada = entrada_usuario.strip().lower()
 
    if not entrada.startswith("!"):
        return " Usa '!' para indicar un comando (ej: !sumar 2 3)."
 
    partes = entrada.split(" ", 1)
    comando = partes[0]
    argumento = partes[1] if len(partes) > 1 else None
 
    if comando == "!ayuda":
        lista = ", ".join(COMANDOS_DISPONIBLES.keys())
        return f"Comandos gestionados: {lista}, !hora, !ayuda"
 
    if comando in COMANDOS_DISPONIBLES:
        return COMANDOS_DISPONIBLES[comando](argumento)
 
    return comando_libre(entrada_usuario)
  
if __name__ == "__main__":
    print("--- Gestor de Comandos (agente_gestor_logica.py) ---")
    print("Escribe '!ayuda' para ver los comandos disponibles.")
    while True:
        user_input = input("Usuario >> ")
        if user_input.lower() in ["salir", "exit"]:
            break
        print(f"Gestor >> {gestionar_comando(user_input)}\n")
 