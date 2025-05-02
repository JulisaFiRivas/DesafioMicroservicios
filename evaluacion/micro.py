from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def conectar_base_datos():
    parametros = {
        "host": "mysqldb",
        "user": "root",
        "password": "julita",
        "database": "desafiobdd"
    }
    return mysql.connector.connect(**parametros)

#Registrar una nueva evaluación
@app.route('/evaluacion', methods=["POST"])
def registrar_evaluacion():
    info = request.get_json()
    conexion = conectar_base_datos()
    cur = conexion.cursor()

    cur.execute("SELECT * FROM estudiante WHERE rut = %s", (info["rut"],))
    estudiante_existe = cur.fetchone()

    if not estudiante_existe:
        conexion.close()
        return jsonify({"mensaje": "El estudiante no existe en el sistema"}), 400

    sql = "INSERT INTO evaluacion (rut_estudiante, semestre, asignatura, nota) VALUES (%s, %s, %s, %s)"
    valores = (info["rut"], info["semestre"], info["asignatura"], info["nota"])
    cur.execute(sql, valores)
    conexion.commit()
    conexion.close()
    return jsonify({"mensaje": "Evaluación registrada correctamente"}), 200

#Obtener todas las evaluaciones
@app.route('/evaluacion', methods=["GET"])
def obtener_evaluaciones():
    conexion = conectar_base_datos()
    cur = conexion.cursor(dictionary=True)
    cur.execute("SELECT * FROM evaluacion")
    registros = cur.fetchall()
    conexion.close()
    return jsonify(registros), 200

#Obtener evaluaciones por RUT de estudiante
@app.route('/evaluacion/<rut_estudiante>', methods=["GET"])
def buscar_evaluaciones_estudiante(rut_estudiante):
    conexion = conectar_base_datos()
    cur = conexion.cursor(dictionary=True)
    cur.execute("SELECT * FROM evaluacion WHERE rut_estudiante = %s", (rut_estudiante,))
    resultados = cur.fetchall()
    conexion.close()

    if resultados:
        return jsonify(resultados), 200
    else:
        return jsonify({"mensaje": "No se encontraron evaluaciones para el estudiante"}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000)
