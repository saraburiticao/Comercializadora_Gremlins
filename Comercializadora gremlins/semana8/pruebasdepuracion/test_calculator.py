import unittest
import mysql.connector

# Función para obtener todos los usuarios desde la base de datos
def get_all_users():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="logistica_db"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    users = cursor.fetchall()
    conn.close()
    return users

class TestDatabaseQueries(unittest.TestCase):
    def test_get_all_users(self):
        # Ejecuta la consulta
        users = get_all_users()
        
        # Define el resultado esperado
        expected_users = [
            (1, 'Camilo Cordoba', 'Gerente'),
            (2, 'Carlos Díaz', 'Recepción'),
            (3, 'Sara Buriticá', 'Administrador'),
            (4, 'Laura Rivas', 'Transportista'),
            (5, 'Carolina Molina', 'Asistente de Gerente'),
            (6, 'Astrid Pineda', 'Atención al Cliente'),
            (7, 'Estefanía Olaya', 'Transportista'),
            (8, 'Daniela Ramírez', 'Transportista')
        ]
        
        # Verifica que los resultados sean los esperados
        self.assertEqual(users, expected_users)

if __name__ == '__main__':
    unittest.main()




