# Description: Funciones para manejar los pendientes de los estudiantes

# Funcion para obtener los pendientes de un usuario
def obtener_pendientes(usuario):
    try:
        # Se abre el archivo de pendientes
        with open('estudianteFiles/archivosTxt/pendientes.txt', 'r') as archivo:
            # Se lee el contenido del archivo
            contenido = archivo.read()
            if contenido:
                pendientes = contenido.splitlines()
                # Filtrar pendientes por el nombre del usuario actual
                pendientes_usuario = [linea.split(',') for linea in pendientes if linea.split(',')[4] == usuario]
                # Se retorna una lista con los pendientes del usuario
                return {'pendientes': pendientes_usuario}
            else:
                return {'pendientes': []}
    except FileNotFoundError:
        return {'pendientes': []}
    except Exception as e:
        return {"success": False, "message": str(e)}


# Funcion para añadir un pendiente
def añadir_pendiente(fecha, id_pendiente, monto, nombre, usuario):
    #se abre el archivo para añadir un nuevo pendiente
    try:
        with open('estudianteFiles/archivosTxt/pendientes.txt', 'a') as archivo:
            #se añade el nuevo pendiente al archivo con los datos de fecha, id, monto, nombre y usuario
            archivo.write(f"{fecha},{id_pendiente},{monto},{nombre},{usuario}\n")
    except Exception as e:
        raise Exception(f"Error al añadir pendiente: {str(e)}")

# Funcion para eliminar un pendiente
def eliminar_pendiente(id_pendiente, usuario):
    try:
        with open('estudianteFiles/archivosTxt/pendientes.txt', 'r') as archivo:
            contenido = archivo.read()
            #se verifica si el archivo contiene pendientes
            if contenido:
                #si contiene pendientes se eliminan los pendientes con el id y usuario especificados
                pendientes = contenido.splitlines()
                pendientes = [linea for linea in pendientes if not (linea.split(',')[1] == id_pendiente and linea.split(',')[4] == usuario)]
                with open('estudianteFiles/archivosTxt/pendientes.txt', 'w') as archivo:
                    #se escribe en el archivo los pendientes que no se eliminaron
                    for pendiente in pendientes:
                        archivo.write(pendiente + '\n')
    except Exception as e:
        raise Exception(f"Error al eliminar pendiente: {str(e)}")
