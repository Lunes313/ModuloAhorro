# Description: Este archivo contiene las funciones necesarias para manejar los gastos de los estudiantes

#funcion para leer los gastos de los estudiantes
def leerGastosE(nombre):
    #se abre el archivo de gastos
    try:
        with open("estudianteFiles/archivosTxt/gastos.txt", "r") as archivo:
            #se lee el archivo
            gastos = eval(archivo.read())
            #se verifica si el nombre esta en el archivo
            if nombre in gastos:
                #se retorna el valor de los gastos si el nombre esta
                return gastos[nombre]
            else:
                #se retorna un diccionario con los valores de gastos en 0 si el nombre no esta
                return {"alimentacion": [0], "transporte": [0], "Otros": [0], "Ahorro": 0}
    except Exception as e:
        #se imprime un mensaje de error si no se puede leer el archivo
        print("Error al leer el archivo de gastos:", e)
        return {"alimentacion": [0], "transporte": [0], "Otros": [0], "Ahorro": 0}

#funcion para mostrar el total de lo gastado
def mostrarTotalGastos(gastos):
    #se suman los valores de cada lista en cada categoria de gastos menos ahorro
    gastosTotales = sum(sum(value) for key, value in gastos.items() if key != 'Ahorro')
    #se retorna el total de gastos
    return gastosTotales

#funcion para añadir gastos por categorias
def añadirGastoE(usuario, categoria, nuevoGasto):
    #se abre el archivo de gastos
    try:
        with open("estudianteFiles/archivosTxt/gastos.txt", "r") as archivo:
            #se lee el archivo
            gastos = eval(archivo.read())
        #se verifica si el usuario esta en el archivo
        if usuario not in gastos:
            #se retorna un mensaje de error si el usuario no esta
            return False, "Usuario no encontrado"
        #se verifica si la categoria ya contiene gastos
        if len(gastos[usuario][categoria]) >= 1:
            #se añade el nuevo gasto a la categoria si ya contiene gastos
            gastos[usuario][categoria].append(int(nuevoGasto))
        else:
            #si no contiene gastos se crea una lista con el nuevo gasto
            gastos[usuario][categoria] = [int(nuevoGasto)]
        with open("estudianteFiles/archivosTxt/gastos.txt", "w") as archivo:
            #se escribe el nuevo valor de gastos en el archivo
            archivo.write(str(gastos))
        #se retorna un mensaje de exito si se añade el gasto
        return True, ""
    except Exception as e:
        #se imprime un mensaje de error si no se puede añadir el gasto
        return False, str(e)


#funcion para sumar ahorro
def sumarAhorro(usuario, ahorro):
    #se abre el archivo de gastos
    try:
        with open("estudianteFiles/archivosTxt/gastos.txt", "r") as archivo:
            gastos = eval(archivo.read())
        if usuario not in gastos:
            return False, "Usuario no encontrado"
        #se suma el ahorro al valor de ahorro actual
        gastos[usuario]['Ahorro'] += int(ahorro)
        with open("estudianteFiles/archivosTxt/gastos.txt", "w") as archivo:
            #se escribe el nuevo valor de ahorro en el archivo
            archivo.write(str(gastos))
        return True, ""
    except Exception as e:
        return False, str(e)


#funcion para restar ahorro, su funcionalidad es igual que la de sumar pero se le resta al valor total
def restarAhorro(usuario, ahorro):
    try:
        with open("estudianteFiles/archivosTxt/gastos.txt", "r") as archivo:
            gastos = eval(archivo.read())
        if usuario not in gastos:
            return False, "Usuario no encontrado"
        gastos[usuario]['Ahorro'] -= int(ahorro)
        with open("estudianteFiles/archivosTxt/gastos.txt", "w") as archivo:
            archivo.write(str(gastos))
        return True, ""
    except Exception as e:
        return False, str(e)

#funcion para editar ahorro
def editar_Ahorro(usuario, opcion, ahorro):
    try:
        if opcion == "retirar":
            #si la opcion es retirar se llama a la funcion restarAhorro
            return restarAhorro(usuario, ahorro)
        elif opcion == "Añadir":
            #si la opcion es añadir se llama a la funcion sumarAhorro
            return sumarAhorro(usuario, ahorro)
    except Exception as e:
        return False, str(e)

#Funcion para sumar gastos por categorias
def sumarGastos(usuario):
    try:
        with open("estudianteFiles/archivosTxt/gastos.txt", "r") as archivo:
            gastos = eval(archivo.read())
        if usuario not in gastos:
            return False, "Usuario no encontrado"
        #se suman los valores de cada categoria de gastos y se devuelve un diccionario
        gastosS= { "Alimentacion": sum(gastos[usuario]["Alimentacion"]), "Transporte": sum(gastos[usuario]["Transporte"]), "Otros": sum(gastos[usuario]["Otros"]), "Ahorro": gastos[usuario]["Ahorro"]}
        return gastosS
    except Exception as e:
        return False, str(e)


