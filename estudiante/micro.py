from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def conectar_bd():
    config = {
        "host": "mysqldb",
        "user": "root",
        "password": "julita",
        "database": "desafiobdd"
    }
    return mysql.connector.connect(**config)

#Agregar un estudiante
@app.route('/estudiante', methods=["POST"])
def agregar_estudiante():
    try:
        nuevo = request.get_json()
        conexion = conectar_bd()
        cur = conexion.cursor()
        query = "INSERT INTO estudiante (rut, nombre, edad, curso) VALUES (%s, %s, %s, %s)"
        valores = (nuevo["rut"], nuevo["nombre"], nuevo["edad"], nuevo["curso"])
        cur.execute(query, valores)
        conexion.commit()
        conexion.close()
        return jsonify({"mensaje": "Estudiante registrado exitosamente"}), 200
    except Exception as error:
        return jsonify({"error": str(error)}), 400

#Obtener todos los estudiantes
@app.route('/estudiante', methods=["GET"])
def obtener_estudiantes():
    conexion = conectar_bd()
    cur = conexion.cursor(dictionary=True)
    cur.execute("SELECT * FROM estudiante")
    resultados = cur.fetchall()
    conexion.close()
    return jsonify(resultados), 200

#Obtener un estudiante por RUT
@app.route('/estudiante/<rut>', methods=["GET"])
def buscar_por_rut(rut):
    conexion = conectar_bd()
    cur = conexion.cursor(dictionary=True)
    cur.execute("SELECT * FROM estudiante WHERE rut = %s", (rut,))
    resultado = cur.fetchone()
    conexion.close()
    if resultado:
        return jsonify(resultado), 200
    else:
        return jsonify({"mensaje": "No se encontró el estudiante con ese RUT"}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)
