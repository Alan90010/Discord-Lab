import datetime
import procesador_comandos as procesador

NOMBRE_BOT = "IAn"
HORA_INICIO = datetime.datetime.now()


def comando_saludo(argumento):
    return procesador.obtener_saludo(NOMBRE_BOT)


def comando_recordar(argumento):
    return procesador.procesar_comando_recordar(argumento)


def comando_uptime(argumento):
    return procesador.calcular_uptime(HORA_INICIO)


def comando_ayuda(argumento):
    return procesador.mostrar_ayuda()


COMANDOS_DISPONIBLES = {
    "!saludo": comando_saludo,
    "!recordar": comando_recordar,
    "!uptime": comando_uptime,
    "!ayuda": comando_ayuda,
}


def gestionar_comando(entrada_usuario):
    entrada = entrada_usuario.strip()

    if not entrada.startswith("!"):
        return "Comando no reconocido"

    partes = entrada[1:].split(maxsplit=1)
    comando = "!" + partes[0].lower()
    argumento = partes[1] if len(partes) > 1 else ""

    if comando in COMANDOS_DISPONIBLES:
        return COMANDOS_DISPONIBLES[comando](argumento)

    return "Comando no reconocido"


if __name__ == "__main__":
    print(comando_saludo(""))
    print("Escribe !ayuda para ver los comandos disponibles.")
    while True:
        user_input = input(f"[{NOMBRE_BOT}] Ingrese comando: ").strip()
        if user_input.lower() == "!salir":
            print("Hasta luego")
            break
        print(gestionar_comando(user_input))