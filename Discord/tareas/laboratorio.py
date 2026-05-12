class ControlAcceso:
    def __init__(self):
        self.usuarios_autorizados = {
            "2024001": "Investigador",
            "2024002": "Estudiante",
            "2024003": "Administrador"
        }

    def verificar_permisos(self, matricula):
        if matricula == "":
            raise ValueError()
            
        if matricula in self.usuarios_autorizados:
            rol = self.usuarios_autorizados[matricula]
            print(f"> [ACCESO CONCEDIDO] Bienvenido, rol detectado: {rol}.")
        else:
            print("> [ACCESO DENEGADO] Usuario no registrado en la base de datos de IA.")

print("--- Sistema de Seguridad Laboratorio IA - UX ---")
control = ControlAcceso()

while True:
    try:
        id_usuario = input("\nIngrese su matrícula: ")
        control.verificar_permisos(id_usuario)
        print("--- Intento de acceso registrado en el log del servidor ---")
    except ValueError:
        print("> [ERROR] El campo no puede estar vacío.")
        print("--- Intento de acceso registrado en el log del servidor ---")