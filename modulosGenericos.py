
def ingresarUsuario():
    try:
        usuario = input('Ingrese su login: ').strip()
        if usuario == '':
            raise ValueError()
    except ValueError:
        print("No podes ingresar un usuario vacio.")
    return usuario

def ingresarContraseña():
    try:
        password = input("Ingresa tu contraseña: ")
        if password == '':
            raise ValueError()
    except ValueError:
        print("No ingresaste ninguna contraseña")
    return password    