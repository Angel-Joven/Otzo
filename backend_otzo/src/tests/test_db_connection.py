from src.db import get_connection


def test_connection():
    connection = get_connection()
    assert connection is not None, "La conexión a la base de datos falló"
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT DATABASE()")
                result = cursor.fetchone()
                print("Conectado a la base de datos:", result[0])
        finally:
            connection.close()


def test_query():
    connection = get_connection()
    assert connection is not None, "La conexión a la base de datos falló"
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT precio_unitario FROM inventario where nombre_producto = (%s)",
                    "Mouse Logitech",
                )
                result = cursor.fetchone()
                print("Conectado a la base de datos:", result[0])
        finally:
            connection.close()

def test_query_fidelizacion():
    connection = get_connection()
    assert connection is not None, "La conexión a la base de datos falló"
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT nombre_rango FROM rangos where idrango = (%s)",
                    1,
                )
                result = cursor.fetchone()
                print("Conectado a la base de datos - FIDELIZACION:", result[0])
        finally:
            connection.close()
