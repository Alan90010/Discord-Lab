import datetime
class Tarea:

def agregar_tareas(lista_Tareas, descripcion):
    """
    Agregar una tarea a la lista si cumple los requisitos
    """

    if len(descripcion) < 3:
        return "Error: longitud no valida"

        # Crear formato tarea

        fecha = datetime.datetime.now().strftime("%H:%M")

        nueva_tarea = f"(descripcion) - (fecha)"
        lista_Tareas.append(nueva_tarea)
        return f"(Tarea agregada con exito)"

