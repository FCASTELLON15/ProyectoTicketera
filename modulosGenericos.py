import random
from datetime import datetime
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
        password = input("Ingresa tu contraseña: ").strip()
        if password == '':
            raise ValueError()
    except ValueError:
        print("No ingresaste ninguna contraseña")
    return password    

def ingresarNombre():
    while True:
        try:
            nombre = input('Ingrese un nombre: ').strip().capitalize()
            if not nombre.isalpha():
                raise ValueError()
            assert nombre
            break
        except ValueError:
            print('No podes ingresar numeros ni caracteres, solo letras.')
    return nombre

def ingresarApellido():
        while True:
            try:
                apellido = input('Ingrese un apellido: ').strip().capitalize()
                if not apellido.isalpha():
                    raise ValueError()
                assert apellido
                break
            except ValueError:
                print('No podes ingresar numeros ni caracteres, solo letras.')
            except AssertionError:
                print('No podes ingresar un apellido vacio.')
        return apellido

def ingresarEdad():
        while True:
            try:
                edad = input('Ingresa tu edad: ').strip()
                edad = int(edad)
                break
            except ValueError:
                print('Debes ingresar una edad numerica.')
        return edad

def ingresarDni():
        while True:
            try:
                dni = input('Ingresa tu dni: ').strip()
                dni = int(dni)
                break
            except ValueError:
                print('Debes ingresar un DNI valido.')
        return dni

def ingresarLogin():
        while True:
            try:
                login = input('Ingresa un login (unico) de acceso: ').strip().lower()

                if not login:
                    print('No podes ingresar un login vacio.')
                    continue

                if login[:1].isdigit():
                    raise ValueError()
                break

            except ValueError:
                print('No podes ingresar un numero como primer caracter de tu login.')
        return login

def buscarDni(diccionario,dni):
    #busco en el diccionario, en el campo DNI de cada clave, si esta el nro de DNI
    # si esta devuelve TRUE, de lo contrario FALSE
    return any(info["dni"] == dni for info in diccionario.values())

def crearUsuarioCompra(diccionario):
    #funciona OK
    nombre = ingresarNombre()
    apellido = ingresarApellido()
    while True:
        login = str(ingresarLogin())
        if login in diccionario:
            print('Login ya utilizado. Por favor ingrese otro login.')
            continue
        dni = str(ingresarDni())
        while buscarDni(diccionario,dni):
            print('DNI ya utilizado. Por favor ingrese otro DNI.')
            dni = str(ingresarDni())
        break
    contrasenia = ingresarContraseña()
    edad = str(ingresarEdad())
    rol = 'Compras'

    try:
        archivo = open('Datos/usuarios.txt', 'a')
    except FileNotFoundError:
        print('No se ha podido crear el usuario por problema en la base de datos.')
    
    linea = nombre + ';' + apellido + ';' + dni + ';' + login + ';' + contrasenia + ';' + edad + ';' + rol + '\n'

    archivo.write(linea)
    print('Registro exitoso')
    archivo.close()

def generarIdEvento():

    numero = random.randint(1,1000)
    evento = 'E' + str(numero)
    evento = evento.zfill(4)
    return evento
        
def ingresarFecha():
    while True:
        fecha_str = input("Ingresá la fecha (dd/mm/aaaa): ")
        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            return fecha   # Si entra acá, la fecha es válida
        except ValueError:
            print("Fecha inválida. Intentá de nuevo.")


def crearEvento(diccionario):
    #falta agregar funcionalidades, por ejemplo que el evento no este repetidos
    #Funciona OK!
    try:
        archivo = open('Datos/eventos.txt','a')
    except FileNotFoundError:
        print('Error al abrir el archivo de eventos.')
    else:
        while True:
            #este bucle es para que no se genere un ID igual, en caso que suceda, vuelve a generarlo
            # hasta que cree uno distinto
            idEvento = generarIdEvento()
            if idEvento in diccionario:
                continue
            break
        nombre = ingresarNombre().capitalize()
        fecha = ingresarFecha()
        while True:
            try:
                capacidad = input('Ingrese la capacidad del evento: ')
                capacidad = int(capacidad)
                break
            except ValueError:
                print('Solo puedes ingresar numeros.')
        capacidad = capacidad
        # agrego todos los datos al diccionario que va a esta agrupado por IDEVENTO
        diccionario[idEvento] = {
            'nombreEvento':nombre,
            'fechaEvento': str(fecha),
            'capacidad': capacidad}
        #tammbien actualizamos el archivo agregando la linea al final del mismo
        linea = idEvento + ';' + nombre + ';' + str(fecha) + ';' + str(capacidad) + '\n'
        print('El ID de el nuevo evento es ', idEvento)
        print('Evento creado correctamente y base de datos actualizada.')
        archivo.write(linea)
        archivo.close()

    




    
    


    
        




    
            


    