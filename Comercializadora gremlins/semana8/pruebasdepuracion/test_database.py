import unittest
import mysql.connector

def connect_to_db():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='logistica_db'
    )
    return connection

class TestDatabaseConnection(unittest.TestCase):
    def test_connection(self):
        connection = connect_to_db()
        self.assertIsNotNone(connection)
        self.assertTrue(connection.is_connected())
        connection.close()

if __name__ == '__main__':
    unittest.main()
