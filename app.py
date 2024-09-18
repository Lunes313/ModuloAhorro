from flask import Flask, jsonify, request
from flask_cors import CORS
from estudianteFiles.presupuestos import mostrarTotalP, leerPresupuestosE, editarPresupuestoE, definirMeta
from estudianteFiles.gastos import leerGastosE, mostrarTotalGastos, añadirGastoE, sumarGastos, editar_Ahorro
from estudianteFiles.pendientes import añadir_pendiente, eliminar_pendiente, obtener_pendientes
from hogarFiles.presupuestos import  leerPresupuestosH, editarPresupuestoH,definirMetaH, mostrarTotalPH
from hogarFiles.gastos import leerGastosH,sumarGastosH,añadirGastoH,editar_AhorroH, mostrarTotalGastosH
from hogarFiles.pendientes import añadir_pendienteH, eliminar_pendienteH, obtener_pendientesH
app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

# Variable global para almacenar el nombre del usuario
# Esta practica no se considera una practica segura, pero ya que trabajamos de manera local no hay problema
name = None

# Funcion para manejar los usuarios
def verificarUsuario(nombre, contrasena):
    # Diccionario con usuarios
    usuarios = {
        "usuario1": {
            "nombre": "Juan",
            "contrasena": "1234",
            "perfil": "Estudiante",
        },
        "usuario2": {
            "nombre": "Ana",
            "contrasena": "1432",
            "perfil": "Estudiante"
        },
        "usuario3": {
            "nombre": "Maria",
            "contrasena": "2431",
            "perfil": "Hogar",
        },
        "usuario4": {
            "nombre": "Laura",
            "contrasena": "1234",
            "perfil": "Hogar",
        },
    }

    for usuario in usuarios.values():
        if usuario["nombre"] == nombre and usuario["contrasena"] == contrasena:
            return usuario["perfil"]
    return False

# Funcion para manejar los usuarios enviados por el formulario de inicio de sesion
# enviandolos a la pagina principal de hogar o estudiante
@app.route('/procesar_datos', methods=['POST'])
def procesar_datos():
    # Obtener datos del formulario
    data = request.get_json()
    nombre = data.get('nombre')
    contrasena = data.get('contrasena')
    resultado = verificarUsuario(nombre, contrasena)

    if resultado:
        global name
        name = nombre
        if resultado == "Estudiante":
            presupuesto = leerPresupuestosE(nombre)
            gastos = leerGastosE(nombre)
        else:
            if resultado == "Hogar":
                presupuesto = leerPresupuestosH(nombre)
                gastos = leerGastosH(nombre)
            else:
                presupuesto = None
                gastos = None
        if presupuesto:
            return jsonify({
                "mensaje": "Acceso permitido",
                "perfil": resultado,
                "presupuesto": presupuesto,
                "gastos": gastos
            })
        else:
            return jsonify({"mensaje": "Acceso permitido, pero no se encontró presupuesto"})
    else:
        return jsonify({"mensaje": "Acceso denegado"})

#Obtener los datos de los usuarios(Estudiante) para mostrarlos en la pagina principal
@app.route('/datos', methods=['GET'])
def get_presupuesto():
    if name is None:
        return jsonify({"mensaje": "No se ha iniciado sesión"})
    else:
        gastado = mostrarTotalGastos(leerGastosE(name))
        totalP = mostrarTotalP(leerPresupuestosE(name))
        #sumar gastos por cada categoria
        gastosS= sumarGastos(name)
        return jsonify({"presupuesto_total": totalP, "gastado": gastado, "presupuestos": leerPresupuestosE(name), "gastosS": gastosS, "gastos": leerGastosE(name), "Meta": leerPresupuestosE(name)["Meta"]})

#Obtener los datos de los usuarios(Hogar) para mostrarlos en la pagina principal
@app.route('/datosH', methods=['GET'])
def get_presupuestoH():
    if name is None:
        return jsonify({"mensaje": "No se ha iniciado sesión"})
    else:
        gastado = mostrarTotalGastosH(leerGastosH(name))
        totalP = mostrarTotalPH(leerPresupuestosH(name))
        #sumar gastos por cada categoria
        gastosS= sumarGastosH(name)
        return jsonify({"presupuesto_total": totalP, "gastado": gastado, "presupuestos": leerPresupuestosH(name), "gastosS": gastosS, "gastos": leerGastosH(name), "Meta": leerPresupuestosH(name)["Meta"]})


# Funcion para manejar presupuestos del estudiante
@app.route('/editar_presupuesto', methods=['POST'])
def editar_presupuesto():
    data = request.get_json()
    usuario = name
    categoria = data.get('categoria')
    nuevo_presupuesto = data.get('nuevoPresupuesto')

    if not categoria or not nuevo_presupuesto:
        return jsonify({"success": False, "message": "Datos incompletos"}), 400

    try:
        exito, mensaje = editarPresupuestoE(usuario, categoria, nuevo_presupuesto)
        if exito:
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "message": mensaje}), 404
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

# Funcion para manejar presupuestos del hogar
@app.route('/editar_presupuestoH', methods=['POST'])
def editar_presupuestoH():
    data = request.get_json()
    usuario = name
    categoria = data.get('categoria')
    nuevo_presupuesto = data.get('nuevoPresupuesto')

    if not categoria or not nuevo_presupuesto:
        return jsonify({"success": False, "message": "Datos incompletos"}), 400

    try:
        exito, mensaje = editarPresupuestoH(usuario, categoria, nuevo_presupuesto)
        if exito:
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "message": mensaje}), 404
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


# Funcion para manejar gastos del estudiante
@app.route('/editar_gasto', methods=['POST'])
def editar_gasto():
    data = request.get_json()
    usuario = name
    categoria = data.get('categoria')
    nuevo_gasto = data.get('nuevoGasto')

    if not categoria or not nuevo_gasto:
        return jsonify({"success": False, "message": "Datos incompletos"}), 400

    try:
        exito, mensaje = añadirGastoE(usuario, categoria, nuevo_gasto)
        if exito:
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "message": mensaje}), 404
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

# Funcion para manejar gastos del hogar
@app.route('/editar_gastoH', methods=['POST'])
def editar_gastoH():
    data = request.get_json()
    usuario = name
    categoria = data.get('categoria')
    nuevo_gasto = data.get('nuevoGasto')

    if not categoria or not nuevo_gasto:
        return jsonify({"success": False, "message": "Datos incompletos"}), 400

    try:
        exito, mensaje = añadirGastoH(usuario, categoria, nuevo_gasto)
        if exito:
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "message": mensaje}), 404
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

# Funcion para manejar la meta de ahorro del estudiante
@app.route('/definir_meta', methods=['POST'])
def definir_meta():
    data = request.get_json()
    usuario = name
    nueva_meta = data.get('meta')

    if not nueva_meta:
        return jsonify({"success": False, "message": "Meta no proporcionada"}), 400

    try:
        exito, mensaje = definirMeta(usuario, nueva_meta)
        if exito:
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "message": mensaje}), 404
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

# Funcion para manejar la meta de ahorro del hogar
@app.route('/definir_metaH', methods=['POST'])
def definir_metaH():
    data = request.get_json()
    usuario = name
    nueva_meta = data.get('meta')

    if not nueva_meta:
        return jsonify({"success": False, "message": "Meta no proporcionada"}), 400

    try:
        exito, mensaje = definirMetaH(usuario, nueva_meta)
        if exito:
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "message": mensaje}), 404
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

# Funcion para manejar ahorro del estudiante
@app.route('/ahorro', methods=['POST'])
def editarAhorro():
    data = request.get_json()
    usuario = name
    ahorro = data.get('ahorro')
    opcion = data.get('opcion')

    if not ahorro or not opcion:
        return jsonify({"success": False, "message": "Datos incompletos"}), 400

    try:
        exito, mensaje = editar_Ahorro(usuario, opcion, ahorro)
        if exito:
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "message": mensaje}), 404
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


# Funcion para manejar ahorro del hogar
@app.route('/ahorroH', methods=['POST'])
def editarAhorroH():
    data = request.get_json()
    usuario = name
    ahorro = data.get('ahorro')
    opcion = data.get('opcion')

    if not ahorro or not opcion:
        return jsonify({"success": False, "message": "Datos incompletos"}), 400

    try:
        exito, mensaje = editar_AhorroH(usuario, opcion, ahorro)
        if exito:
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "message": mensaje}), 404
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


# Funcion para manejar pendientes del estudiante
@app.route('/añadir_pendiente', methods=['POST'])
def añadir_pendiente_route():
    data = request.get_json()
    fecha = data.get('fecha')
    id_pendiente = data.get('id_pendiente')
    monto = data.get('monto')
    nombre = data.get('nombre')

    if name is None:
        return jsonify({"success": False, "message": "No se ha iniciado sesión"}), 401

    if not (fecha and id_pendiente and monto and nombre):
        return jsonify({"success": False, "message": "Datos incompletos"}), 400

    try:
        añadir_pendiente(fecha, id_pendiente, monto, nombre, name)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

# Funcion para manejar pendientes del hogar
@app.route('/añadir_pendienteH', methods=['POST'])
def añadir_pendiente_routeH():
    data = request.get_json()
    fecha = data.get('fecha')
    id_pendiente = data.get('id_pendiente')
    monto = data.get('monto')
    nombre = data.get('nombre')

    if name is None:
        return jsonify({"success": False, "message": "No se ha iniciado sesión"}), 401

    if not (fecha and id_pendiente and monto and nombre):
        return jsonify({"success": False, "message": "Datos incompletos"}), 400

    try:
        añadir_pendienteH(fecha, id_pendiente, monto, nombre, name)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

# Funcion para eliminar pendientes del estudiante
@app.route('/eliminar_pendiente', methods=['POST'])
def eliminar_pendiente_route():
    data = request.get_json()
    id_pendiente = data.get('id_pendiente')

    if name is None:
        return jsonify({"success": False, "message": "No se ha iniciado sesión"}), 401

    if not id_pendiente:
        return jsonify({"success": False, "message": "ID del pendiente no proporcionado"}), 400

    try:
        eliminar_pendiente(str(id_pendiente), name)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

# Funcion para eliminar pendientes del hogar
@app.route('/eliminar_pendienteH', methods=['POST'])
def eliminar_pendiente_routeH():
    data = request.get_json()
    id_pendiente = data.get('id_pendiente')

    if name is None:
        return jsonify({"success": False, "message": "No se ha iniciado sesión"}), 401

    if not id_pendiente:
        return jsonify({"success": False, "message": "ID del pendiente no proporcionado"}), 400

    try:
        eliminar_pendienteH(str(id_pendiente), name)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

# Funcion para obtener pendientes del estudiante
@app.route('/pendientes', methods=['GET'])
def get_pendientes():
    if name is None:
        return jsonify({"success": False, "message": "No se ha iniciado sesión"}), 401

    try:
        return jsonify(obtener_pendientes(name))
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

# Funcion para obtener pendientes del hogar
@app.route('/pendientesH', methods=['GET'])
def get_pendientesH():
    if name is None:
        return jsonify({"success": False, "message": "No se ha iniciado sesión"}), 401

    try:
        return jsonify(obtener_pendientesH(name))
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
