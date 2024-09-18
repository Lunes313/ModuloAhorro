# Funciones para manejar los gastos de los estudiantes

#Funciones para manejar los gastos de los estudiantes
def leerGastosH(nombre):
    try:
        with open("hogarFiles/archivosTxt/gastos.txt", "r") as archivo:
            gastos = eval(archivo.read())
            if nombre in gastos:
                return gastos[nombre]
            else:
                return {"alimentacion": [0], "vivienda": [0],"servicios": [0], "Otros": [0], "Ahorro": 0}
    except Exception as e:
        print("Error al leer el archivo de gastos:", e)
        return {"alimentacion": [0], "vivienda": [0],"servicios": [0], "Otros": [0], "Ahorro": 0}

#funcion para mostrar el total de lo gastado
def mostrarTotalGastosH(gastos):
    #se suman los valores de cada lista en cada categoria
    gastosTotales = sum(sum(value) for key, value in gastos.items() if key != 'Ahorro')
    return gastosTotales

#funcion para añadir gastos por categorias
def añadirGastoH(usuario, categoria, nuevoGasto):
    try:
        with open("hogarFiles/archivosTxt/gastos.txt", "r") as archivo:
            gastos = eval(archivo.read())
        if usuario not in gastos:
            return False, "Usuario no encontrado"
        if len(gastos[usuario][categoria]) >= 1:
            gastos[usuario][categoria].append(int(nuevoGasto))
        else:
            gastos[usuario][categoria] = [int(nuevoGasto)]
        with open("hogarFiles/archivosTxt/gastos.txt", "w") as archivo:
            archivo.write(str(gastos))
        return True, ""
    except Exception as e:
        return False, str(e)


#funcion para sumar ahorro

def sumarAhorro(usuario, ahorro):
    try:
        with open("hogarFiles/archivosTxt/gastos.txt", "r") as archivo:
            gastos = eval(archivo.read())
        if usuario not in gastos:
            return False, "Usuario no encontrado"
        gastos[usuario]['Ahorro'] += int(ahorro)
        with open("hogarFiles/archivosTxt/gastos.txt", "w") as archivo:
            archivo.write(str(gastos))
        return True, ""
    except Exception as e:
        return False, str(e)


#funcion para restar ahorro
def restarAhorro(usuario, ahorro):
    try:
        with open("hogarFiles/archivosTxt/gastos.txt", "r") as archivo:
            gastos = eval(archivo.read())
        if usuario not in gastos:
            return False, "Usuario no encontrado"
        gastos[usuario]['Ahorro'] -= int(ahorro)
        with open("hogarFiles/archivosTxt/gastos.txt", "w") as archivo:
            archivo.write(str(gastos))
        return True, ""
    except Exception as e:
        return False, str(e)

#funcion para editar ahorro
def editar_AhorroH(usuario, opcion, ahorro):
    try:
        if opcion == "retirar":
            return restarAhorro(usuario, ahorro)
        elif opcion == "Añadir":
            return sumarAhorro(usuario, ahorro)
    except Exception as e:
        return False, str(e)

#Funcion para sumar gastos por categorias
def sumarGastosH(usuario):
    try:
        with open("hogarFiles/archivosTxt/gastos.txt", "r") as archivo:
            gastos = eval(archivo.read())
        if usuario not in gastos:
            return False, "Usuario no encontrado"
        gastosS= { "Alimentacion": sum(gastos[usuario]["Alimentacion"]), "Vivienda": sum(gastos[usuario]["Vivienda"]),"Servicios": sum(gastos[usuario]["Servicios"]), "Otros": sum(gastos[usuario]["Otros"]), "Ahorro": gastos[usuario]["Ahorro"]}
        return gastosS
    except Exception as e:
        return False, str(e)


