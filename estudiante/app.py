from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="julita",
        database="desafiobdd"
    )

@app.route('/estudiantes', methods=["POST"])
def crear_estudiante():
    try:
        data = request.get_json()
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO estudiante (rut, nombre, edad, curso) VALUES (%s, %s, %s, %s)", 
                       (data["rut"], data["nombre"], data["edad"], data["curso"]))
        conn.commit()
        conn.close()
        return jsonify({"message": "Estudiante creado"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/estudiantes', methods=["GET"])
def listar_estudiantes():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM estudiante")
    estudiantes = cursor.fetchall()
    conn.close()
    return jsonify(estudiantes), 200

@app.route('/estudiantes/<rut>', methods=["GET"])
def estudiante_por_rut(rut):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM estudiante WHERE rut = %s", (rut,))
    estudiante = cursor.fetchone()
    conn.close()
    if estudiante:
        return jsonify(estudiante), 200
    else:
        return jsonify({"message": "Estudiante no creado, no exiate"}), 404
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)


