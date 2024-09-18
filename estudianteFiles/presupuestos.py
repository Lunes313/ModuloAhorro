# Description: Funciones para manejar los presupuestos de los estudiantes

#funcion para leer los presupuestos del txt
def leerPresupuestosE(nombre):
    #leer el archivo de presupuestos
    try:
        with open("estudianteFiles/archivosTxt/presupuestos.txt", "r") as archivo:

            presupuestos = eval(archivo.read())
            #si el nombre del estudiante esta en el archivo, retornar el presupuesto
            if nombre in presupuestos:
                return presupuestos[nombre]
            else:
                #si no esta, retornar un diccionario con los valores en 0
                return {"alimentacion": 0, "transporte": 0, "Otros": 0, "Meta": 0}
    except Exception as e:
        #si hay un error, retornar un diccionario con los valores en 0
        print("Error al leer el archivo de presupuestos:", e)
        return {"alimentacion": 0, "transporte": 0, "Otros": 0, "Meta": 0}


#funcion para mostrar el presupuesto total
def mostrarTotalP(presupuesto):
    #retornar la suma de los valores del diccionario presupuesto sin contar la meta
    return sum(value for key, value in presupuesto.items() if key != 'Meta')


#funcion para editar el presupuesto por categorias
def editarPresupuestoE(name, categoria, nuevoPresupuesto):
    try:
        with open("estudianteFiles/archivosTxt/presupuestos.txt", "r") as archivo:
            presupuestos = eval(archivo.read())
        if name not in presupuestos:
            return False, "Usuario no encontrado"
        #actualizar el presupuesto de la categoria con el nuevo valor
        presupuestos[name][categoria] = int(nuevoPresupuesto)
        with open("estudianteFiles/archivosTxt/presupuestos.txt", "w") as archivo:
            #escribir el diccionario actualizado en el archivo
            archivo.write(str(presupuestos))
        return True, ""
    except Exception as e:
        return False, str(e)


#funcion para definir la meta de ahorro
def definirMeta(name, nuevaMeta):
    try:
        with open("estudianteFiles/archivosTxt/presupuestos.txt", "r") as archivo:
            presupuestos = eval(archivo.read())
        if name not in presupuestos:
            return False, "Usuario no encontrado"
        #actualizar la meta con el nuevo valor en el diccionario
        presupuestos[name]['Meta'] = int(nuevaMeta)
        with open("estudianteFiles/archivosTxt/presupuestos.txt", "w") as archivo:
            #escribir el diccionario actualizado en el archivo
            archivo.write(str(presupuestos))
        return True, ""
    except Exception as e:
        return False, str(e)

