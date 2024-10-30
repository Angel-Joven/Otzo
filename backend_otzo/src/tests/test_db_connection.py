from src.db import get_connection


def test_connection():
    connection = get_connection()
    assert connection is not None, "La conexión a la base de datos falló"
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT DATABASE()")
                result = cursor.fetchone()
                print("Conectado a la base de datos:", result)
        finally:
            connection.close()
