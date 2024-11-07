import unittest
from index import app

class TestFidelizacion(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

# ---------------------------------------------------------------------------------------------------------------------------

    def test_ActualizarRangoClienteActivoRangoIgual(self):
        response = self.app.post('/api/fidelizacion/actualizarrango', json={
            "id_cliente": 1 
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 1")
        print("Rango - Cliente Activo - El rango ya lo tiene asigando.", data)

    def test_ActualizarRangoClienteActivo(self):
        response = self.app.post('/api/fidelizacion/actualizarrango', json={
            "id_cliente": 1  #Colocar ID de un cliente que no tenga el rango aun, pero que si cumpla con sus total de compras.
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 2")
        print("Rango - Cliente Activo - Rango actualizado.", data)

    def test_ActualizarRangoClienteInactivo(self):
        response = self.app.post('/api/fidelizacion/actualizarrango', json={
            "id_cliente": 5 # Cliente inactivo
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 3")
        print("Rango - Cliente Inactivo.", data)

    def test_ActualizarRangoClienteSuspendido(self):
        response = self.app.post('/api/fidelizacion/actualizarrango', json={
            "id_cliente": 9 # Cliente suspendido
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 4")
        print("Rango - Cliente Suspendido.", data)

    def test_ActualizarRangoClienteInexistente(self):
        response = self.app.post('/api/fidelizacion/actualizarrango', json={
            "id_cliente": 9999 # Cliente inexistente
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 5")
        print("Rango - Cliente Inexistente.", data)

# ---------------------------------------------------------------------------------------------------------------------------

    def test_calcularPuntosCompraRango1(self):
        response = self.app.post('/api/fidelizacion/calcularptscompra', json={
            "id_cliente": 1,
            "id_rango": 1,
            "precioCompraTotal": 1000
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 6")
        print("Puntos de compra calculados para el rango 1: ", data)

    def test_calcularPuntosCompraRango2(self):
        response = self.app.post('/api/fidelizacion/calcularptscompra', json={
            "id_cliente": 1,
            "id_rango": 2,
            "precioCompraTotal": 1000
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 7")
        print("Puntos de compra calculados para el rango 2: ", data)

    def test_calcularPuntosCompraRango3(self):
        response = self.app.post('/api/fidelizacion/calcularptscompra', json={
            "id_cliente": 1,
            "id_rango": 3,
            "precioCompraTotal": 1000
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 8")
        print("Puntos de compra calculados para el rango 3: ", data)

    def test_calcularPuntosCompraRango4(self):
        response = self.app.post('/api/fidelizacion/calcularptscompra', json={
            "id_cliente": 1,
            "id_rango": 4,
            "precioCompraTotal": 1000
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 9")
        print("Puntos de compra calculados para el rango 4: ", data)

    def test_calcularPuntosCompraRango5(self):
        response = self.app.post('/api/fidelizacion/calcularptscompra', json={
            "id_cliente": 1,
            "id_rango": 5,
            "precioCompraTotal": 1000
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 10")
        print("Puntos de compra calculados para el rango 5: ", data)
    
    def test_calcularPuntosCompraRango6(self):
        response = self.app.post('/api/fidelizacion/calcularptscompra', json={
            "id_cliente": 1,
            "id_rango": 6,
            "precioCompraTotal": 1000
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 11")
        print("Puntos de compra calculados para el rango 6: ", data)

    def test_calcularPuntosCompraClienteInexistente(self):
        response = self.app.post('/api/fidelizacion/calcularptscompra', json={
            "id_cliente": 999999,
            "id_rango": 6,
            "precioCompraTotal": 1000
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 12")
        print("No se calcularon los puntos de su compra ya que el cliente no existe.", data)

    def test_calcularPuntosCompraRangoInexistente(self):
        response = self.app.post('/api/fidelizacion/calcularptscompra', json={
            "id_cliente": 1,
            "id_rango": 99999,
            "precioCompraTotal": 1000
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 13")
        print("No se calcularon los puntos de su compra ya que el rango no existe.", data)

    def test_calcularPuntosCompraRangoClienteInexistente(self):
        response = self.app.post('/api/fidelizacion/calcularptscompra', json={
            "id_cliente": 999999,
            "id_rango": 99999,
            "precioCompraTotal": 1000
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 14")
        print("No se calcularon los puntos de su compra ya que el rango y el cliente no existen.", data)

    def test_calcularPuntosCompraPrecioNegativo(self):
        response = self.app.post('/api/fidelizacion/calcularptscompra', json={
            "id_cliente": 1,
            "id_rango": 1,
            "precioCompraTotal": -100 #Precio Compra negativo
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 15")
        print("No se pudieron calcular los puntos de una compra ya que el precio de la compra no puede ser negativo: ", data)

    def test_añadirPuntosCompra(self):
        response = self.app.post('/api/fidelizacion/addptscompra', json={
            "id_cliente": 1,
            "puntosCompra": 1000
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 16")
        print("Puntos de una compra añadidos con exito: ", data)

# ---------------------------------------------------------------------------------------------------------------------------

    def test_calcularPuntosDevolucionRango1(self):
        response = self.app.post('/api/fidelizacion/calcularptsdevolucion', json={
            "id_cliente": 1,
            "id_rango": 1,
            "precioProducto": 100
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 17")
        print("Puntos de devolucion calculados para el rango 1: ", data)

    def test_calcularPuntosDevolucionRango2(self):
        response = self.app.post('/api/fidelizacion/calcularptsdevolucion', json={
            "id_cliente": 1,
            "id_rango": 2,
            "precioProducto": 100
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 18")
        print("Puntos de devolucion calculados para el rango 2: ", data)

    def test_calcularPuntosDevolucionRango3(self):
        response = self.app.post('/api/fidelizacion/calcularptsdevolucion', json={
            "id_cliente": 1,
            "id_rango": 3,
            "precioProducto": 100
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 19")
        print("Puntos de devolucion calculados para el rango 3: ", data)

    def test_calcularPuntosDevolucionRango4(self):
        response = self.app.post('/api/fidelizacion/calcularptsdevolucion', json={
            "id_cliente": 1,
            "id_rango": 4,
            "precioProducto": 100
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 20")
        print("Puntos de devolucion calculados para el rango 4: ", data)

    def test_calcularPuntosDevolucionRango5(self):
        response = self.app.post('/api/fidelizacion/calcularptsdevolucion', json={
            "id_cliente": 1,
            "id_rango": 5,
            "precioProducto": 100
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 21")
        print("Puntos de devolucion calculados para el rango 5: ", data)
    
    def test_calcularPuntosDevolucionRango6(self):
        response = self.app.post('/api/fidelizacion/calcularptsdevolucion', json={
            "id_cliente": 1,
            "id_rango": 6,
            "precioProducto": 100
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 22")
        print("Puntos de devolucion calculados para el rango 6: ", data)

    def test_calcularPuntosDevolucionClienteInexistente(self):
        response = self.app.post('/api/fidelizacion/calcularptsdevolucion', json={
            "id_cliente": 999999,
            "id_rango": 6,
            "precioProducto": 100
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 23")
        print("No se calcularon los puntos de su devolucion ya que el cliente no existe.", data)

    def test_calcularPuntosDevolucionRangoInexistente(self):
        response = self.app.post('/api/fidelizacion/calcularptsdevolucion', json={
            "id_cliente": 1,
            "id_rango": 99999,
            "precioProducto": 100
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 24")
        print("No se calcularon los puntos de su devolucion ya que el rango no existe.", data)

    def test_calcularPuntosDevolucionRangoClienteInexistente(self):
        response = self.app.post('/api/fidelizacion/calcularptsdevolucion', json={
            "id_cliente": 999999,
            "id_rango": 99999,
            "precioProducto": 100
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 25")
        print("No se calcularon los puntos de su devolucion ya que el rango y el cliente no existen.", data)

    def test_calcularPuntosDevolucionPrecioNegativo(self):
        response = self.app.post('/api/fidelizacion/calcularptsdevolucion', json={
            "id_cliente": 1,
            "id_rango": 1,
            "precioProducto": -100 #Precio Compra negativo
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 26")
        print("No se pudieron calcular los puntos de una devolucion ya que el precio del producto no puede ser negativo: ", data)

    def test_añadirPuntosDevoluciones(self):
        response = self.app.post('/api/fidelizacion/añadirPuntosDevolucion', json={
            "id_cliente": 1,
            "puntosDevolucion": 1000
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 27")
        print("Puntos de una devolucion añadidos con exito: ", data)

# ---------------------------------------------------------------------------------------------------------------------------

    def test_descontarPuntosExactos(self):
        response = self.app.post('/api/fidelizacion/descontarpuntos', json={
            "id_cliente": 1,
            "precioCompraTotal": 100
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 28")
        print("Puntos descontados por haber realizado una compra con exito: ", data)

    def test_descontarPuntosInsuficientes(self):
        response = self.app.post('/api/fidelizacion/descontarpuntos', json={
            "id_cliente": 1,
            "precioCompraTotal": 10000000000000
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 29")
        print("No tienes los puntos necesarios para realizar una compra: ", data)

    def test_descontarPuntosClienteActivo(self):
        response = self.app.post('/api/fidelizacion/descontarpuntos', json={
            "id_cliente": 1,  # Cliente Activo
            "precioCompraTotal": 100
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 30")
        print("Descontar Puntos - Cliente Activo - Compra realizada y pagada con puntos.", data)

    def test_descontarPuntosClienteInactivo(self):
        response = self.app.post('/api/fidelizacion/descontarpuntos', json={
            "id_cliente": 5,  # Cliente inactivo
            "precioCompraTotal": 0
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 31")
        print("Descontar Puntos - Cliente Inactivo.", data)

    def test_descontarPuntosClienteSuspendido(self):
        response = self.app.post('/api/fidelizacion/descontarpuntos', json={
            "id_cliente": 9,  # Cliente suspendido
            "precioCompraTotal": 0
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 32")
        print("Descontar Puntos - Cliente Suspendido.", data)

    def test_descontarPuntosClienteInexistente(self):
        response = self.app.post('/api/fidelizacion/descontarpuntos', json={
            "id_cliente": 9999,  # Cliente inexistente
            "precioCompraTotal": 0
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("PRUEBA 33")
        print("Descontar Puntos - Cliente Inexistente.", data)

# ---------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()

# ---------------------------------------------------------------------------------------------------------------------------
