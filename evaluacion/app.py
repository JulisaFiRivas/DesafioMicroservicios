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

@app.route('/evaluacion', methods=["POST"])
def crear_evaluacion():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estudiante WHERE rut= %s", (data["rut"],))
    if cursor.fetchone() is None:
        conn.close()
        return jsonify({"message": "Estudiante no creado, no exiate"}), 400
    cursor.execute("INSERT INTO evaluacion (rut_estudiante, semestre, asignatura, nota) VALUES (%s, %s, %s, %s)", (data["rut"], data["semestre"], data["asignatura"], data["nota"]))
    conn.commit()
    conn.close()
    return jsonify({"message": "Evaluacion creada"}), 200

@app.route('/evaluacion', methods=["GET"])
def listar_evaluaciones():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM evaluacion")
    evaluaciones = cursor.fetchall()
    conn.close()
    return jsonify(evaluaciones), 200

@app.route('/evaluaciones/<rut_estudiante>', methods=["GET"])
def evaluaciones_por_rut(rut_estudiante):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM evaluacion WHERE rut_estudiante = %s", (rut_estudiante,))
    evaluaciones = cursor.fetchall()
    conn.close()
    if evaluaciones:
        return jsonify(evaluaciones), 200
    else:
        return jsonify({"message": "No hay evaluaciones para este estudiante"}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3001)


