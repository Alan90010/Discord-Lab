import datetime

def obtener_saludo(nombre_bot):

    return ("Hola, soy (nombre_bot) y estoy listo para ayudarte.")

def procesar_comando_recordad(comando):
    if not comando:
        return "Error, falta el nombre. Use !recordar [nombre]"

    return f"Entendido! Recordare el nombre: {comando}"

def calcular_uptime(hora_inicio):
    ahora = datetime.datetime.now()
    differencia = ahora - hora_inicio
    segundos = int(differencia.total_seconds())
    return f"Tiempo de actividad: {segundos} segundos"
def mostrar_ayuda():
def iniciar_agente():

def main():
    obtener_saludo(Discordio)
if __name__ == "__main":
    main()