import datetime
class Tarea:

def agregar_tareas(lista_tareas, descripcion):
    """
    Agregar una tarea a la lista si cumple los requisitos
    """

    if len(descripcion) < 3:
        return "Error: longitud no valida"

        # Crear formato tarea

        fecha = datetime.datetime.now().strftime("%H:%M")

        nueva_tarea = f"(descripcion) - (fecha)"
        lista_tareas.append(nueva_tarea)
        return f"(Tarea agregada con exito)"

def listar_tareas(listar_tareas)
    """
    Formatea la lista de tarea para su visualizacion
    """
    if not lista_tareas:
        return "No hay tareas"

    # Agregar una variable llamada resultado

    resultado = "Listado de tareas \n"

    # Iterar la lista de tareas y formatear la salida
    for i, tarea in enumerate(lista_tareas, start=1):
        resultado += f"(i), {tarea}\n"
    return resultado

def eliminar_tarea(lista_tareas, indice):
    """
    Eliminar una tarea por su numero de indice
    """
    if not indice.lsdgit():
        return "Error: El inidice debe ser un numero"

    indice = int(indice)-1

    """
    Agregamos a la logica para preguntar
    si el elemento esta en la lista y eliminado
    """

    if 0 <= indice < len(lista_tareas):
        tarea_eliminada = lista_tareas.pop(inidice)

    else:
        return "Error: No existe la tarea"
    return f"Tarea eliminada: {tarea_eliminada}"

def main():
    tareas = []
    PREFIJO ="!"

    print("Bienvenido al geestor de tareas")
    activa = True
    while activa:
        entrada = input(">>>").strip()
        continue

    # Procesamiento de la entrada
    cuerpo = entrada [len(PREFIJO):].split(maxsplit=1)
    comando = cuerpo[0].lower()
    argumento = cuerpo[1] if len(cuerpo) > 1 else ""

    if comando = "add"
        resultado = agregar_tareas(tareas, argumento)
        print