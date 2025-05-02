CREATE DATABASE IF NOT EXISTS desafiobdd;
USE desafiobdd;

CREATE TABLE IF NOT EXISTS estudiante (
    rut VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(100),
    edad INT,
    curso VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS evaluacion (
    id_evaluacion INT AUTO_INCREMENT PRIMARY KEY,
    rut_estudiante VARCHAR(20),
    semestre VARCHAR(20),
    asignatura VARCHAR(100),
    nota DECIMAL(3,1),
    FOREIGN KEY (rut_estudiante) REFERENCES estudiante(rut)
);

INSERT INTO estudiante (rut, nombre, edad, curso) VALUES
('12345678-9', 'Julisa Figueroa', 23, 'primero'),
('98765432-1', 'Apolo Figueroa', 4, 'segundo');

INSERT INTO evaluacion (rut_estudiante, semestre, asignatura, nota) VALUES
('12345678-9', '2025-1', 'Matematicas', 6.0),
('98765432-1', '2025-1', 'Fisica', 6.1);