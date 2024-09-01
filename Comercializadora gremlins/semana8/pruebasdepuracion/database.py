import mysql.connector

def connect_to_db():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='logistica_db'
    )
    return connection

def get_users():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM usuarios")  # Ajusta la consulta según tu esquema
    users = cursor.fetchall()
    connection.close()
    return users
