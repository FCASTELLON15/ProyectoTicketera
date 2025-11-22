from generarArchivos import generarDiccionarioUsuarios
import modulosGenericos
#Login usuario
def login(diccionario):
    
    while True:
        
        usuario = modulosGenericos.ingresarUsuario().lower()
        
        if not usuario in diccionario:
            print("Usuario inexistente. Vuelva a ingresar")
            continue
        
        password = modulosGenericos.ingresarContraseña()

        while password == '':
            print('Contraseña invalida. Vuelva a ingresar')
            password = modulosGenericos.ingresarContraseña()
        
        while password != diccionario[usuario]['contrasenia']:
            print('Contraseña invalida. Vuelva a ingresar')
            password = modulosGenericos.ingresarContraseña()
        print('Login exitoso')
        return True


def main():
    diccionario = generarDiccionarioUsuarios()
    acceso = login(diccionario)
    if acceso:
        modulosGenericos.crearUsuarioCompra(diccionario)
main()
            