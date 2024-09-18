#Funciones para manejar los pendientes en el hogar
#Este archivo debe contener obtener_pendientesH añadir_pendienteH, eliminar_pendienteH
#Recuerde nombrar las funciones exactamente como se menciono anteriormente para que el programa funcione correctamente
#Recuerde que las funciones deben retornar y recibir los parametros mencionados en cada espacio.


#funcion para obtener los pendientes de un usuario (obtener_pendientesH)
#La siguiente funcion recibe el nombre del usuario y retorna un diccionario con los pendientes de ese usuario de la forma
# {'pendientes': [[fecha, id_pendiente, monto, nombre, usuario], [fecha, id_pendiente, monto, nombre, usuario], ...]}
#si el usuario no tiene pendientes registrados se retorna un diccionario vacio
# {'pendientes': []}
#si hay algun error se retorna un diccionario con la llave success en False y un mensaje de error

#tenga en cuenta que el archivo de pendientes tiene la siguiente estructura
#fecha,id_pendiente,monto,nombre,usuario
#tenga en cuenta que los valores estan separados por comas y cada pendiente esta en una linea diferente

#Reto: Modificar la funcion para que retorne solo los ultimos 5 pendientes del usuario para que estos no se salgan del div de pendientes
#para el reto recuerde que el usuario puede tener menos de 5 pendientes registrados

def obtener_pendientesH(usuario):
    ruta_archivo = 'hogarFiles/archivosTxt/pendientes.txt'
    try:
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
            if contenido:
                pendientes = contenido.splitlines()
                # Filtrar pendientes por el nombre del usuario actual
                pendientes_usuario = [linea.split(',') for linea in pendientes if linea.split(',')[4] == usuario]
                return {'pendientes': pendientes_usuario}
            else:
                return {'pendientes': []}
    except FileNotFoundError:
        return {'pendientes': []}
    except Exception as e:
        return {"success": False, "message": str(e)}


#funcion para añadir un pendiente (añadir_pendienteH)
#La siguiente funcion recibe la fecha, id_pendiente, monto, nombre y usuario del pendiente a añadir
#y añade un nuevo pendiente al archivo de pendientes de la forma fecha,id_pendiente,monto,nombre,usuario y luego un salto de linea
#si hay algun error se retorna un mensaje de error
def añadir_pendienteH(fecha, id_pendiente, monto, nombre, usuario):
    #se abre el archivo para añadir un nuevo pendiente
    ruta_archivo = 'hogarFiles/archivosTxt/pendientes.txt'
    try:
        with open(ruta_archivo, 'a') as archivo:
            archivo.write(f"{fecha},{id_pendiente},{monto},{nombre},{usuario}\n")
    except Exception as e:
        raise Exception(f"Error al añadir pendiente: {str(e)}")

#funcion para eliminar un pendiente (eliminar_pendienteH)
#La siguiente funcion recibe el id del pendiente y el nombre del usuario y elimina el pendiente con ese id y usuario del archivo de pendientes
#si hay algun error se retorna un mensaje de error
#Pista: Utilice la funcion splitlines para separar los valores de cada pendiente y luego compare el id y el usuario con los recibidos
#recuerde escribir los pendientes que no se eliminaron en el archivo para finalizar la eliminacion
def eliminar_pendienteH(id_pendiente, usuario):
    # se elimina un pendiente
    ruta_archivo = 'hogarFiles/archivosTxt/pendientes.txt'
    try:
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
            if contenido:
                pendientes = contenido.splitlines()
                pendientes = [linea for linea in pendientes if not (linea.split(',')[1] == id_pendiente and linea.split(',')[4] == usuario)]
                with open(ruta_archivo, 'w') as archivo:
                    for pendiente in pendientes:
                        archivo.write(pendiente + '\n')
    except Exception as e:
        raise Exception(f"Error al eliminar pendiente: {str(e)}")
