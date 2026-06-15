from tareas_agente import agregar_tarea, listar_tareas, eliminar_tarea

def main():
    tareas = []
    PREFIJO = "!"

    print("=== Agente Procesador de Tareas ===")
    print("Comandos disponibles:")
    print("!add [texto]   -> Agregar una tarea")
    print("!list          -> Listar tareas")
    print("!del [numero]  -> Eliminar una tarea")
    print("!exit          -> Salir")
    print()

    while True:
        entrada = input(">> ").strip()

        if not entrada.startswith(PREFIJO):
            if entrada:
                print("Recuerda usar '!' para comandos.")
            continue

        cuerpo = entrada[len(PREFIJO):].split(maxsplit=1)
        comando = cuerpo[0].lower()
        argumento = cuerpo[1] if len(cuerpo) > 1 else ""

        if comando == "exit":
            print("Saliendo del agente...")
            break

        elif comando == "add":
            print(agregar_tarea(tareas, argumento))

        elif comando == "list":
            print(listar_tareas(tareas))

        elif comando == "del":
            print(eliminar_tarea(tareas, argumento))

        else:
            print(f"Error: Comando '!{comando}' no reconocido.")

        print("-" * 20)


if __name__ == "__main__":
    main()
