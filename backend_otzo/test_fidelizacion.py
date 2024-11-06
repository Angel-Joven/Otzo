import unittest
from index import app

class TestFidelizacion(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

# ---------------------------------------------------------------------------------------------------------------------------

    def test_calcularPuntosCompraRango1(self):
        response = self.app.post('/api/fidelizacion/calcularptscompra', json={
            "id_cliente": 1,
            "id_rango": 1,
            "precioCompraTotal": 1000
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn("Puntos de una compra calculados con exito", data["message"])
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("Puntos de compra calculados para el rango 1: ", data)

    def test_calcularPuntosCompraRango2(self):
        response = self.app.post('/api/fidelizacion/calcularptscompra', json={
            "id_cliente": 1,
            "id_rango": 2,
            "precioCompraTotal": 1000
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn("Puntos de una compra calculados con exito", data["message"])
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("Puntos de compra calculados para el rango 2: ", data)

    def test_calcularPuntosCompraRango3(self):
        response = self.app.post('/api/fidelizacion/calcularptscompra', json={
            "id_cliente": 1,
            "id_rango": 3,
            "precioCompraTotal": 1000
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn("Puntos de una compra calculados con exito", data["message"])
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("Puntos de compra calculados para el rango 3: ", data)

    def test_calcularPuntosCompraRango4(self):
        response = self.app.post('/api/fidelizacion/calcularptscompra', json={
            "id_cliente": 1,
            "id_rango": 4,
            "precioCompraTotal": 1000
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn("Puntos de una compra calculados con exito", data["message"])
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("Puntos de compra calculados para el rango 4: ", data)

    def test_calcularPuntosCompraRango5(self):
        response = self.app.post('/api/fidelizacion/calcularptscompra', json={
            "id_cliente": 1,
            "id_rango": 5,
            "precioCompraTotal": 1000
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn("Puntos de una compra calculados con exito", data["message"])
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("Puntos de compra calculados para el rango 5: ", data)
    
    def test_calcularPuntosCompraRango6(self):
        response = self.app.post('/api/fidelizacion/calcularptscompra', json={
            "id_cliente": 1,
            "id_rango": 6,
            "precioCompraTotal": 1000
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn("Puntos de una compra calculados con exito", data["message"])
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("Puntos de compra calculados para el rango 6: ", data)

# ---------------------------------------------------------------------------------------------------------------------------

    def test_calcularPuntosDevolucionRango1(self):
        response = self.app.post('/api/fidelizacion/calcularptsdevolucion', json={
            "id_cliente": 1,
            "id_rango": 1,
            "precioProducto": 100
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn("Puntos de una devolucion calculados con exito", data["message"])
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("Puntos de devolucion calculados para el rango 1: ", data)

    def test_calcularPuntosDevolucionRango2(self):
        response = self.app.post('/api/fidelizacion/calcularptsdevolucion', json={
            "id_cliente": 1,
            "id_rango": 2,
            "precioProducto": 100
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn("Puntos de una devolucion calculados con exito", data["message"])
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("Puntos de devolucion calculados para el rango 2: ", data)

    def test_calcularPuntosDevolucionRango3(self):
        response = self.app.post('/api/fidelizacion/calcularptsdevolucion', json={
            "id_cliente": 1,
            "id_rango": 3,
            "precioProducto": 100
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn("Puntos de una devolucion calculados con exito", data["message"])
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("Puntos de devolucion calculados para el rango 3: ", data)

    def test_calcularPuntosDevolucionRango4(self):
        response = self.app.post('/api/fidelizacion/calcularptsdevolucion', json={
            "id_cliente": 1,
            "id_rango": 4,
            "precioProducto": 100
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn("Puntos de una devolucion calculados con exito", data["message"])
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("Puntos de devolucion calculados para el rango 4: ", data)

    def test_calcularPuntosDevolucionRango5(self):
        response = self.app.post('/api/fidelizacion/calcularptsdevolucion', json={
            "id_cliente": 1,
            "id_rango": 5,
            "precioProducto": 100
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn("Puntos de una devolucion calculados con exito", data["message"])
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("Puntos de devolucion calculados para el rango 5: ", data)
    
    def test_calcularPuntosDevolucionRango6(self):
        response = self.app.post('/api/fidelizacion/calcularptsdevolucion', json={
            "id_cliente": 1,
            "id_rango": 6,
            "precioProducto": 100
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn("Puntos de una devolucion calculados con exito", data["message"])
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("Puntos de devolucion calculados para el rango 6: ", data)

# ---------------------------------------------------------------------------------------------------------------------------

    def test_añadirPuntosCompra(self):
        for _ in range(3):
            response = self.app.post('/api/fidelizacion/addptscompra', json={
                "id_cliente": 1,
                "puntosCompra": 1000
            })
            data = response.get_json()
            self.assertEqual(response.status_code, 200)
            self.assertIn("Puntos de una compra añadidos con exito", data["message"])
            print("---------------------------------------------------------------------------------------------------------------------------")
            print("Puntos de una compra añadidos con exito: ", data)

# ---------------------------------------------------------------------------------------------------------------------------

    def test_añadirPuntosDevoluciones(self):
        for _ in range(3):
            response = self.app.post('/api/fidelizacion/añadirPuntosDevolucion', json={
                "id_cliente": 1,
                "puntosDevolucion": 1000
            })
            data = response.get_json()
            self.assertEqual(response.status_code, 200)
            self.assertIn("Puntos de una devolucion añadidos con exito", data["message"])

# ---------------------------------------------------------------------------------------------------------------------------

    def test_descontarPuntosExactos(self):
        response = self.app.post('/api/fidelizacion/descontarpuntos', json={
            "id_cliente": 1,
            "precioCompraTotal": 100
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn("Puntos descontados con exito", data["message"])

# ---------------------------------------------------------------------------------------------------------------------------

    def test_descontarPuntosInsuficientes(self):
        response = self.app.post('/api/fidelizacion/descontarpuntos', json={
            "id_cliente": 1,
            "precioCompraTotal": 10000
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertIn("Puntos Insuficientes", data["message"])

# ---------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()

# ---------------------------------------------------------------------------------------------------------------------------
