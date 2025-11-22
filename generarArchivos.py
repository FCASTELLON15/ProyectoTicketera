
import random


def archivoUsuarios():
    
    nombres = ["Valentina", "Abril", "Morena", "Alma", "Zoe",
    "Emma", "Delfina", "Lara", "Mía", "Julieta",
    "Catalina", "Ambar", "Renata", "Isabela", "Camila",
    "Thiago", "Mateo", "Joaquín", "Benjamín", "Lautaro",
    "Santino", "Bautista", "Elías", "Bruno", "Dylan",
    "Simón", "Franco", "Ian", "Gael", "Tomás"]
    apellidos = ["Gómez", "Rodríguez", "Fernández", "López", "Martínez",
    "González", "Pérez", "Sánchez", "Romero", "Suárez",
    "Torres", "Álvarez", "Ramírez", "Ruiz", "Molina",
    "Castro", "Silva", "Moreno", "Ortiz", "Vega",
    "Costa", "Navarro", "Rivas", "Domínguez", "Bravo"]
    
    contrasenas = ["Xy9!aP32",
    "Moon_47$",
    "R3ggaeton#1",
    "Pulse!88",
    "N3onTiger*",
    "SkyFall_91",
    "BeatDrop$22",
    "Blaze!503",
    "NightRun_74",
    "WolfByte#6"]
    
    
    cantidadUsuarios = random.randint(10,12)
    
    try:
        archivo = open('Datos/usuarios.txt', 'w')
    except FileNotFoundError:
        print('El archivo no se ha podido abrir correctamente.')
    else:
        archivo.write('Nombre;Apellido;Dni;Login;Contrasenia;Edad;Rol \n')
        
        for x in range(cantidadUsuarios):
            nombre = nombres[random.randint(0,len(nombres)-1)]
            apellido = apellidos[random.randint(0,len(apellidos)-1)]
            dni = random.randint(1,70000000)
            login = nombre[:1] + apellido
            contrasenia = contrasenas[random.randint(0,len(contrasenas)-1)]
            edad = random.randint(18,35)
            rol = 'Compras'
            linea = nombre + ';' + apellido + ';' + str(dni) + ';' + login.lower() + ';' + contrasenia + ';' + str(edad) + ';' + rol + '\n'
            
            archivo.write(linea)
        print('OK- Archivo de usuarios generado correctamente.')
    archivo.close()


#genero un diccionaro que va a contener los datos del archivo, se usara como base de datos
# para poder buscar informacion si es necesario
def generarDiccionarioUsuarios():
    diccionario = {}
    try:
        archivo = open('Datos/usuarios.txt', 'r')
    except FileNotFoundError:
        print('El archivo no se ha podido abrir correctamente.')
    else:
        contador = True
        for linea in archivo:
            if contador:
                contador = False
            else:
                nombre,apellido,dni,login,contrasenia,edad,rol = linea.strip().split(';')
                
                
                diccionario[login] = {'dni':dni,
                                      'nombre':nombre,
                                      'apellido':apellido,
                                      'contrasenia':contrasenia,
                                      'edad':edad,
                                      'rol':rol}
                
    archivo.close()
        
    return diccionario

#crea el archivo eventos.txt y escribe el header
def archivoEventos():
    try:
        archivo = open('Datos/eventos.txt', 'w')
    except FileNotFoundError:
        print('El archivo no se ha podido abrir correctamente.')
    else:
        archivo.write('IdEvento;IdCompra;Nombre;Apellido;Login \n')
    archivo.close()

#creo el archivo tickets_vendidos.txt y escribe el header   
def archivoTickets():
    try:
        archivo = open('Datos/tickets_vendidos.txt', "w")
    except FileNotFoundError:
        print("El archivo no se ha podido abrir correctamente")
    else:
        archivo.write('id_ticket;id_evento;dni;nombre_apellido;tipo_ticket \n')
    archivo.close()
    
def generar():
    archivoUsuarios()
    archivoEventos()
    archivoTickets()
    return True



    
    


                
