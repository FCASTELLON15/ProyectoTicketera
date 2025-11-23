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
        
        break
    print('Login exitoso')
    return True,usuario


def main():
    diccionario = generarDiccionarioUsuarios()
    diccionarioEventos = {}

    acceso,usuario = login(diccionario)
    if acceso:
        '''if diccionario[usuario]['rol'] == 'Administrador':
            while True:
                print('1- Crear evento')
                print('2- Salir')
                while True:
                    try:

                        opcion = int(input('Ingresa una opcion: '))
                        assert opcion != 1 or opcion != 2
                        break
                    except ValueError:
                        print('Debes ingresar una opcion valida.')
                    except AssertionError:
                        print('Debes ingresar una opcion valida.')
                if opcion == 1:
                    modulosGenericos.crearEvento(diccionarioEventos)
                    continue
                else:
                    break'''
    


main()
            