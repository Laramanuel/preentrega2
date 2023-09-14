base_de_datos = {}


def registro_de_usuarios(base_de_datos):
    usuario = input("Ingrese su nombre:")
    contrasenia = input("Ingrese una contraseña:")
    base_de_datos[usuario] = contrasenia
    print("Cuenta de usuario creada con éxito.")
    return base_de_datos


def lectura_de_datos(base_de_datos):
    for usuario, contrasenia in base_de_datos.items():
        print(f"{usuario}: {contrasenia}")
        print("inicio de sesion")


def inicio_de_sesion(base_de_datos):
    usuario = input("Ingrese su nombre de usuario: ")
    contrasenia = input("Ingrese su contraseña:")
    if usuario in base_de_datos.keys() and contrasenia == base_de_datos[usuario]:
        print("Sesión iniciada con éxito")
    else:
        print("Nombre de usuario o contraseña erronéo.")


def guardar_datos(base_de_datos):
    file = open("./base_de_datos.txt", "a")
    texto = f"{base_de_datos}"
    file.write(texto)
    file.close()


base_de_datos = registro_de_usuarios(base_de_datos)
lectura_de_datos(base_de_datos)
inicio_de_sesion(base_de_datos)
guardar_datos(base_de_datos)
