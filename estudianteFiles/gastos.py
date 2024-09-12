# Funciones para manejar los gastos de los estudiantes

#Funciones para manejar los gastos de los estudiantes
def leerGastosE(nombre):
    try:
        with open("estudianteFiles/gastos.txt", "r") as archivo:
            gastos = eval(archivo.read())
            if nombre in gastos:
                return gastos[nombre]
            else:
                return {"alimentacion": [0], "transporte": [0], "Otros": [0], "Ahorro": 0}
    except Exception as e:
        print("Error al leer el archivo de gastos:", e)
        return {"alimentacion": [0], "transporte": [0], "Otros": [0], "Ahorro": 0}

#funcion para mostrar el total de lo gastado
def mostrarTotalGastos(gastos):
    #se suman los valores de cada lista en cada categoria
    gastosTotales = sum(sum(value) for key, value in gastos.items() if key != 'Ahorro')
    return gastosTotales

