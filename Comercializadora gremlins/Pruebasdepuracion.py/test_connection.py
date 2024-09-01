from database import connect_to_db

def test_db_connection():
    connection = connect_to_db()
    if connection:
        print("Conexión exitosa")
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()
        print(f"Base de datos actual: {db_name[0]}")
        cursor.close()
        connection.close()
    else:
        print("No se pudo conectar a la base de datos")

if __name__ == "__main__":
    test_db_connection()
