def control_biometrico():
    print("--- SISTEMA DE CONTROL BIOMÉTRICO ---")

    nombre = input("Nombre del Ingeniero: ")
    id_empleado = int(input("ID de Empleado: "))

    iris_correcto = input("¿El escaneo de Iris coincide con la base de datos? (si/no): ").lower()
    facial_correcto = input("¿El reconocimiento facial es mayor al 95%? (si/no): ").lower()

    print("\n> Diagnóstico: ", end="")

    if id_empleado <= 0:
        print("¡ALERTA DE SEGURIDAD! ID inválido detectado. Bloqueando accesos y notificando a la policía.")

    elif id_empleado < 100 and iris_correcto == "si" and facial_correcto == "si":
        print(f"Bienvenido, Ingeniero {nombre}. Acceso nivel SENIOR concedido a todas las áreas.")
        print(f"Generando log de entrada para el usuario: {id_empleado}...")

    elif id_empleado >= 100 and iris_correcto == "si" and facial_correcto == "si":
        print(f"Bienvenido, Ingeniero {nombre}. Acceso nivel JUNIOR concedido. Áreas de servidores restringidas.")
        print(f"Generando log de entrada para el usuario: {id_empleado}...")

    else:
        print("Error Biométrico: Identidad no verificada al 100%. Por favor, contacte a seguridad.")

def main():
    control_biometrico()

if __name__ == "__main__":
    main()