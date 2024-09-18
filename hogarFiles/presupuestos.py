#Funciones para el manejo de presupuestos de los estudiantes
#Este archivo debe contener las funciones leerPresupuestosH, mostrarTotalPH, editarPresupuestoH, definirMetaH
#Recuerde nombrar las funciones exactamente como se menciono anteriormente para que el programa funcione correctamente
#Recuerde que las funciones deben retornar y recibir los parametros mencionados en cada espacio.



#funcion para leer los presupuestos de un usuario (leerPresupuestosH)
#La siguiente funcion recibe el nombre del usuario y retorna un diccionario con los presupuestos de ese usuario de la forma
# {'alimentacion': 0, 'vivienda': 0, 'servicios': 0, 'Otros': 0, 'Meta': 0}
#si el usuario no tiene presupuestos registrados se retorna un diccionario con los valores en 0
#si hay algun error se retorna un diccionario con los valores en 0 y un mensaje de error
#Pista: al leer el archivo de presupuestos se retorna un diccionario con los valores de los presupuestos de la manera mencionada anteriormente
def leerPresupuestosH(nombre):
    #leer el archivo de presupuestos
    try:
        with open("hogarFiles/archivosTxt/presupuestos.txt", "r") as archivo:
            presupuestos = eval(archivo.read())
            if nombre in presupuestos:
                return presupuestos[nombre]
            else:
                return {"alimentacion": 0, "vivienda": 0,"servicios":0, "Otros": 0, "Meta": 0}
    except Exception as e:
        print("Error al leer el archivo de presupuestos:", e)
        return {"alimentacion": 0, "vivienda": 0,"servicios":0, "Otros": 0, "Meta": 0}


#funcion para mostrar el presupuesto total de un usuario (mostrarTotalPH)
#La siguiente funcion recibe un diccionario con los presupuestos de un usuario y retorna la suma de los presupuestos de todas las categorias excepto la meta
#Recuerde que el diccionario tiene la forma {'alimentacion': 0, 'vivienda': 0, 'servicios': 0, 'Otros': 0, 'Meta': 0}
def mostrarTotalPH(presupuesto):
    return sum(value for key, value in presupuesto.items() if key != 'Meta')


#funcion para editar el presupuesto por categorias de un usuario (editarPresupuestoH)
#La siguiente funcion recibe el nombre del usuario, la categoria a editar y el nuevo presupuesto y edita el presupuesto de esa categoria
#tenga en cuenta que el nuevo presupuesto se pasa como un str y debe ser convertido y que la categoria debe ser una de las siguientes 'alimentacion', 'vivienda', 'servicios', 'Otros'
#esta funcion retorna True si el presupuesto se edito correctamente y False y un mensaje de error si no se pudo editar
#si retorna True el mensaje de error debe ser una cadena vacia
def editarPresupuestoH(name, categoria, nuevoPresupuesto):
    try:
        with open("hogarFiles/archivosTxt/presupuestos.txt", "r") as archivo:
            presupuestos = eval(archivo.read())
        if name not in presupuestos:
            return False, "Usuario no encontrado"
        presupuestos[name][categoria] = int(nuevoPresupuesto)
        with open("hogarFiles/archivosTxt/presupuestos.txt", "w") as archivo:
            archivo.write(str(presupuestos))
        return True, ""
    except Exception as e:
        return False, str(e)


#funcion para definir la meta de ahorro de un usuario (definirMetaH)
#La siguiente funcion recibe el nombre del usuario y la nueva meta de ahorro y edita la meta de ahorro del usuario
#tenga en cuenta que la meta pasada es un str y debe ser convertida
#esta funcion retorna True si la meta se edito correctamente y False y un mensaje de error si no se pudo editar
#si retorna True el mensaje de error debe ser una cadena vacia
#Pista: la meta de ahorro se encuentra en el diccionario de presupuestos con la llave 'Meta'
#Reto: Modificar la funcion para que no permita que la nueva meta sea negativa o 0
def definirMetaH(name, nuevaMeta):
    try:
        with open("hogarFiles/archivosTxt/presupuestos.txt", "r") as archivo:
            presupuestos = eval(archivo.read())
        if name not in presupuestos:
            return False, "Usuario no encontrado"
        presupuestos[name]['Meta'] = int(nuevaMeta)
        with open("hogarFiles/archivosTxt/presupuestos.txt", "w") as archivo:
            archivo.write(str(presupuestos))
        return True, ""
    except Exception as e:
        return False, str(e)


