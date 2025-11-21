from generarArchivos import generarDiccionarioUsuarios
import modulosGenericos
#Login usuario
def login(diccionario):
    
    while True:
        
        usuario = modulosGenericos.ingresarUsuario().lower()
        
        while not usuario in diccionario:
            print("Usuario inexistente. Vuelva a ingresar")
            usuario = modulosGenericos.ingresarUsuario().lower()
        
        password = modulosGenericos.ingresarContraseña()

        while password == '':
            print('Contraseña invalida. Vuelva a ingresar')
            password = modulosGenericos.ingresarContraseña()
        
        while password != diccionario[usuario]:
            print('Contraseña invalida. Vuelva a ingresar')
            password = modulosGenericos.ingresarContraseña()
        print('Login exitoso')
        return True


def main():
    diccionario = generarDiccionarioUsuarios()
    login(diccionario)

main()
            