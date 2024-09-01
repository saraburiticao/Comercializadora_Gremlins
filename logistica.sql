DROP DATABASE IF EXISTS logistica_db;
CREATE DATABASE logistica_db;
USE logistica_db;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    cargo VARCHAR(50) NOT NULL
);

INSERT INTO usuarios (nombre, cargo) VALUES ('Camilo Cordoba', 'Gerente');
INSERT INTO usuarios (nombre, cargo) VALUES ('Carlos Díaz', 'Recepción');
INSERT INTO usuarios (nombre, cargo) VALUES ('Sara Buriticá', 'Administrador');
INSERT INTO usuarios (nombre, cargo) VALUES ('Laura Rivas', 'Transportista');
INSERT INTO usuarios (nombre, cargo) VALUES ('Carolina Molina', 'Asistente de Gerente');
INSERT INTO usuarios (nombre, cargo) VALUES ('Astrid Pineda', 'Atención al Cliente');
INSERT INTO usuarios (nombre, cargo) VALUES ('Estefanía Olaya', 'Transportista');
INSERT INTO usuarios (nombre, cargo) VALUES ('Daniela Ramírez', 'Transportista');

SELECT * FROM usuarios;
