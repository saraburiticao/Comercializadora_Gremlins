# Comercializadora_Gremlins

#Comercializadora_gremlins 

Actividad Semana 8

Comercializadora_Gremlins App

Por:

- Sara C. Buriticá Olaya 
- Camilo S. Cordoba Russi


# Pruebas y Depuracion_Comercializadora_Gremlins

Notas importantes: 

En la semana 8, se complementó el proyecto desarrollado en la semana 7. 
Se retomó el software y se conectó el proyecto a una base de datos en el módulo de administración, con el objetivo de visualizar los usuarios que tienen acceso a la aplicación y realizar pruebas. Para estos fines, el código de la aplicación en la semana 8 presenta algunos aciertos y errores, los cuales fueron depurados posteriormente.

# test de pruebas 

- test de pruebas corresponden a los archivos test_calculator.py , test_database.py, test_dbconecction.py

# depuración

- Folder semana 7. la interfaz de usuario inicial se puede observar en el archivo comercializadora_gremlins_module.py.

- Folder semana 8.   la interfaz de usuario con errores se puede observar en el archivo nuevaUI_gestionusuarios_db.py

- la interfaz de usuario con la depuración aplicada se puede observar en el archivo depuraciondenuevaUI_gestiondeusuarios_db.py


# Importante Correr la Base de Datos en mysql

Descarga la base de datos creada en mysql - logistica_db; la tabla llamada usuarios contiene la siguiente información:
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




# Manual de Usuario - Comercializadora Gremlins

Debajo del mensaje de bienvenida, la aplicación solicita al usuario que seleccione su rol. 

    1. Introducción
       Este sistema permite seleccionar su rol y acceder a funciones específicas.

    2. Roles Disponibles:
       - Gerente: Gestión de importaciones, generación de informes.

       - Administrador: Gestión de usuarios, inventarios y reportes.
       ( el Administrador tiene la posibilidad de ver los usuarios que ingresan a la aplicación haciendo click en el botón gestion de usuarios )

       - Empacador: Empaque de productos, revisión y actualización de inventario.
       - Transportador: Gestión de rutas, monitoreo de entregas.
       - Recepción: Recepción y clasificación de productos.

    3. Uso Básico:
       - Seleccione su rol en la pantalla principal.
       - Use los botones correspondientes para navegar en cada módulo.
       - Presione 'Salir' para cerrar la aplicación.

    4. Si experimenta algún problema o necesita asistencia, 
    por favor contacte al departamento de soporte técnico en el siguiente
      correo: soporte@comercializadoragremlins.com.


Salida de la Aplicación:
Finalmente, la aplicación incluye un botón de Salir en la parte inferior, que permite a los usuarios cerrar la ventana de manera segura cuando terminan de usar la aplicación.


