CREATE TABLE Estudiantes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(45),
    edad INT,
    ciudad VARCHAR(45)
);

-- Insertar datos básicos en la tabla
INSERT INTO Estudiantes (nombre, edad, ciudad) VALUES ('Luna', 20, 'Barranquilla');
INSERT INTO Estudiantes (nombre, edad, ciudad) VALUES ('Sofia', 23, 'Medellín');
INSERT INTO Estudiantes (nombre, edad, ciudad) VALUES ('Luisa', 32, 'Cali');

-- Consultas básicas
-- Consultar todos los registros de la tabla
SELECT * FROM Estudiantes;

-- Filtrar estudiantes por ciudad
SELECT * FROM Estudiantes WHERE ciudad = 'Medellín';

-- Consultar estudiantes mayores de 20 años
SELECT * FROM Estudiantes WHERE edad > 20;
