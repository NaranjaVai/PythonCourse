# Diccionario para almacenar la información de usuarios
usuarios_registrados = {}

# Función para registrar un nuevo usuario
def registrar_usuario():
    usuario = input("Ingrese nombre de usuario: ")
    contraseña = input("Ingrese contraseña: ")
    
    if usuario not in usuarios_registrados:
        usuarios_registrados[usuario] = contraseña
        print(f"Usuario {usuario} registrado con éxito")
    else:
        print(f"El usuario {usuario} ya existe. Por favor, elige otro nombre de usuario")

# Función para mostrar la información de todos los usuarios
def mostrar_informacion():
    print("Información de usuarios:")
    for usuario, contraseña in usuarios_registrados.items():
        print(f"Usuario: {usuario}, Contraseña: {contraseña}")

# Función para realizar el login
def login():
    usuario = input("Ingrese nombre de usuario para login: ")
    contraseña = input("Ingrese contraseña: ")
    
    if usuario in usuarios_registrados and usuarios_registrados[usuario] == contraseña:
        print(f"Bienvenido, {usuario}!")
    elif usuario not in usuarios_registrados:
        print("Nombre de usuario incorrecto")
    else:
        print("Contraseña incorrecta. Inténtalo nuevamente")

# Ejemplo de uso del programa
while True:
    print("\n1. Registrar usuario")
    print("2. Mostrar usuarios")
    print("3. Login")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == '1':
        registrar_usuario()
    elif opcion == '2':
        mostrar_informacion()
    elif opcion == '3':
        login()
    elif opcion == '4':
        print("Programa terminado")
        break
    else:
        print("Opción no válida, intentelo nuevamente")
