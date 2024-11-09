# Servicios para el Modulo de Fidelizacion y Marketing
# Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

# Temas Especiales de Programacion 2 | 1061

from src.models.fidelizacion.fidelizacionModels import *
from src.db import get_connection
from pymysql import DatabaseError

# ---------------------------------------------------------------------------------------------------------------------------

class PuntosService(PuntosModelo):
    def calcular_puntos_compra(self, precio_compra_total, porcentaje_compra_puntos):
        puntos_obtenidos = (precio_compra_total * porcentaje_compra_puntos) / 100
        return round(puntos_obtenidos)
    
    def calcular_puntos_devolucion(self, precio_producto, porcentaje_devolucion_puntos):
        puntos_devolucion = (precio_producto * porcentaje_devolucion_puntos) / 100
        return round(puntos_devolucion)

    def añadir_puntos_compra(self, id_cliente, puntos_compra):
        conexion = get_connection()
        try:
            with conexion.cursor() as cursor:
                #Comenzamos la transaccion
                conexion.begin()

                #Validamos si el cliente existe en la tabla de puntos y que tenga habilitado el poder obtener puntos o algun rango
                cursor.execute("SELECT COUNT(*) FROM puntos WHERE idclientes_puntos = %s AND habilitado = 1", (id_cliente,))
                cliente_existe = cursor.fetchone()[0] > 0
                #print(cliente_existe)

                if not cliente_existe:
                    raise ValueError("La cuenta del cliente no existe o esta Inactiva/Suspendida, por lo tanto no se pudo añadir sus puntos de compra.")

                cursor.execute("UPDATE puntos SET total_puntos = total_puntos + %s, ultima_actualizacionPuntos = NOW() WHERE idclientes_puntos = %s", (puntos_compra, id_cliente))
                #Confirmamos la transaccion
                conexion.commit()

        except DatabaseError as e:
            #Deshacemos la transaccion en caso de error
            conexion.rollback()
            raise e
        finally:
            conexion.close()

    def añadir_puntos_devolucion(self, id_cliente, puntos_devolucion):
        conexion = get_connection()
        try:
            with conexion.cursor() as cursor:
                #Comenzamos la transaccion
                conexion.begin()

                #Validamos si el cliente existe en la tabla de puntos y que tenga habilitado el poder obtener puntos o algun rango
                cursor.execute("SELECT COUNT(*) FROM puntos WHERE idclientes_puntos = %s AND habilitado = 1", (id_cliente,))
                cliente_existe = cursor.fetchone()[0] > 0
                #print(cliente_existe)

                if not cliente_existe:
                    raise ValueError("La cuenta del cliente no existe o esta Inactiva/Suspendida, por lo tanto no se pudo añadir sus puntos de compra.")

                cursor.execute("UPDATE puntos SET total_puntos = total_puntos + %s, ultima_actualizacionPuntos = NOW() WHERE idclientes_puntos = %s", (puntos_devolucion, id_cliente))
                #Confirmamos la transaccion
                conexion.commit()

        except DatabaseError as e:
            #Deshacemos la transaccion en caso de error
            conexion.rollback()
            raise e
        finally:
            conexion.close()

    def descontar_puntos(self, id_cliente, precio_compra_total):
        conexion = get_connection()
        try:
            with conexion.cursor() as cursor:
                #Comenzamos la transaccion
                conexion.begin()

                #Validamos si el cliente existe en la tabla de puntos y que tenga habilitado el poder obtener puntos o algun rango
                cursor.execute("SELECT COUNT(*) FROM puntos WHERE idclientes_puntos = %s AND habilitado = 1", (id_cliente,))
                cliente_existe = cursor.fetchone()[0] > 0
                #print(cliente_existe)

                if not cliente_existe:
                    raise ValueError("La cuenta del cliente no existe o esta Inactiva/Suspendida, por lo tanto no se pudo añadir sus puntos de compra.")

                #Obtenemos los puntos totales del cliente
                cursor.execute("SELECT total_puntos FROM puntos WHERE idclientes_puntos = %s", (id_cliente,))
                resultado = cursor.fetchone()

                if not resultado:
                    raise ValueError("La cuenta del cliente no fue encontrada para realizar el descuento de puntos.")

                puntos_totales = resultado[0]
                if puntos_totales >= precio_compra_total:
                    puntos_restantes = puntos_totales - precio_compra_total
                    cursor.execute("UPDATE puntos SET total_puntos = %s, ultima_actualizacionPuntos = NOW() WHERE idclientes_puntos = %s", (puntos_restantes, id_cliente))
                    #Confirmamos la transaccion
                    conexion.commit()
                    return {"exito": True, "mensaje": "Compra realizada con exito.", "puntos_restantes": puntos_restantes}
                else:
                    return {"exito": False, "mensaje": f"La compra NO fue realizada con exito. Puntos insuficientes. (Puntos Actuales: {puntos_totales} / Puntos Requeridos: {precio_compra_total})."}

        except DatabaseError as e:
            #Deshacemos la transaccion en caso de error
            conexion.rollback()
            raise e
        finally:
            conexion.close()

# ---------------------------------------------------------------------------------------------------------------------------

class RangosService(RangosModelo):
    def asignarRangoInicialAuto(self):
        conexion = get_connection()
        try:
            with conexion.cursor() as cursor:
                #Comenzamos la transaccion
                conexion.begin()

                #Obtenemos todos los usuarios de la tabla clientes que no tienen un registro en la tabla puntos
                cursor.execute(
                    """
                    INSERT INTO puntos (idclientes_puntos, idrango, total_puntos, ultima_actualizacionPuntos, ultima_actualizacionRangos, habilitado)
                    SELECT idCliente, 1, 0, NOW(), NOW(), 1 FROM clientes
                    WHERE idCliente NOT IN (SELECT idclientes_puntos FROM puntos)
                    """
                )
                #Confirmamos la transaccion
                conexion.commit()

                #Validamos si el estado de la cuenta de algun cliente ya ingresado a la tabla puntos paso de 'Activo' a 'Suspendido' o 'Inactivo'
                cursor.execute("UPDATE puntos SET habilitado = 0 WHERE idclientes_puntos IN (SELECT idCliente FROM clientes WHERE Estado IN ('Suspendido', 'Inactivo'))")
                #Confirmamos la transaccion
                conexion.commit()
                return {"mensaje": "Rango 1 asignado a todos los usuarios sin rango y que sus cuentas esten activas"}

        except DatabaseError as e:
            #Deshacemos la transaccion en caso de error
            conexion.rollback()
            raise e
        finally:
            conexion.close()

    def actualizarRangoPorHistorialCompras(self, id_cliente):
        conexion = get_connection()
        try:
            with conexion.cursor() as cursor:
                #Comenzamos la transaccion
                conexion.begin()

                #Validamos si el cliente existe en la tabla de puntos y que tenga habilitado el poder obtener puntos o algun rango
                cursor.execute("SELECT COUNT(*) FROM puntos WHERE idclientes_puntos = %s AND habilitado = 1", (id_cliente,))
                cliente_existe = cursor.fetchone()[0]
                print(cliente_existe)

                if cliente_existe == 0:
                    return {"mensaje": "No se puede actualizar su rango debido a que su cuenta esta Inactiva/Suspendida.", "nuevo_rango": 0}

                else:
                    #Obtenemos la cantidad total de compras del cliente
                    cursor.execute("SELECT COUNT(*) FROM ventas WHERE id_cliente = %s", (id_cliente,))
                    compras_totales = cursor.fetchone()[0]

                    #Determinamos el nuevo rango en funcion del numero total de compras
                    if compras_totales >= 25:
                        nuevo_rango = 6
                    elif compras_totales >= 20:
                        nuevo_rango = 5
                    elif compras_totales >= 15:
                        nuevo_rango = 4
                    elif compras_totales >= 10:
                        nuevo_rango = 3
                    elif compras_totales >= 5:
                        nuevo_rango = 2
                    else:
                        nuevo_rango = 1

                    #Obtenemos el rango actual del cliente
                    cursor.execute("SELECT idrango FROM puntos WHERE idclientes_puntos = %s", (id_cliente,))
                    rango_actual = cursor.fetchone()

                    if nuevo_rango != rango_actual:
                        cursor.execute("UPDATE puntos SET idrango = %s, ultima_actualizacionRangos = NOW() WHERE idclientes_puntos = %s", (nuevo_rango, id_cliente))
                        #Confirmamos la transaccion
                        conexion.commit()
                        return {"mensaje": f"Rango actualizado a {nuevo_rango} despues de {compras_totales} compras.", "nuevo_rango": nuevo_rango}
                    else:
                        return {"mensaje": "La cuenta del cliente ya tiene el rango adecuado para su numero total de compras.", "nuevo_rango": nuevo_rango}

        except DatabaseError as e:
            #Deshacemos la transaccion en caso de error
            conexion.rollback()
            raise e
        finally:
            conexion.close()

    def obtener_rango_cliente_y_porcentajeCompras(self, id_cliente):
        conexion = get_connection()
        try:
            with conexion.cursor() as cursor:
                #Comenzamos la transaccion
                conexion.begin()

                cursor.execute(
                    """
                    SELECT p.idclientes_puntos, p.idrango, p.habilitado, r.porcentaje_puntos FROM puntos p
                    JOIN rangos r ON p.idrango = r.idrango
                    WHERE p.idclientes_puntos = %s
                    """, (id_cliente,))
                #Confirmamos la transaccion
                conexion.commit()

                resultado = cursor.fetchone()

                if resultado:
                    return {"idclientes_puntos": resultado[0], "idrango": resultado[1], "habilitado": resultado[2], "porcentaje_puntos": resultado[3]}
                else:
                    return {"mensaje": "Cliente no encontrado en la tabla puntos"}

        except DatabaseError as e:
            #Deshacemos la transaccion en caso de error
            conexion.rollback()
            raise e
        finally:
            conexion.close()

    def obtener_rango_cliente_y_porcentajeDevolucion(self, id_cliente):
        conexion = get_connection()
        try:
            with conexion.cursor() as cursor:
                #Comenzamos la transaccion
                conexion.begin()

                cursor.execute(
                    """
                    SELECT p.idclientes_puntos, p.idrango, p.habilitado, r.porcentaje_devolucionPuntos FROM puntos p
                    JOIN rangos r ON p.idrango = r.idrango
                    WHERE p.idclientes_puntos = %s
                    """, (id_cliente,))
                #Confirmamos la transaccion
                conexion.commit()

                resultado = cursor.fetchone()

                if resultado:
                    return {"idclientes_puntos": resultado[0], "idrango": resultado[1], "habilitado": resultado[2], "porcentaje_devolucionPuntos": resultado[3]}
                else:
                    return {"mensaje": "Cliente no encontrado en la tabla puntos"}
        
        except DatabaseError as e:
            #Deshacemos la transaccion en caso de error
            conexion.rollback()
            raise e
        finally:
            conexion.close()

# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------

# -> ¡PARA EL MODULO DE VENTAS! <-
# FUNCIONALIDAD QUE CALCULA Y ACTUALIZA LOS PUNTOS DEL CLIENTE
# POR MEDIO DEL PRECIO TOTAL DE LA COMPRA (PUNTOS DE UNA COMPRA)
# Y POR MEDIO DEL PRECIO DEL PRODUCTO (DEVOLUCIONES).

# ASIMISMO, SE CALCULA EL NUMERO TOTAL DE COMPRAS
# QUE TIENE EL CLIENTE ANTES DE HACER LA COMPRA PARA MANTENER O AUMENTAR SU RANGO

# FINALMENTE, SE TIENE LA POSIBILIDAD DE PAGAR
# EL PRECIO TOTAL DE LA COMPRA CON LOS PUNTOS QUE
# TENGA ALMACENADO EL CLIENTE EN SU CUENTA

# REQUISITOS
# id_cliente
# precio_compra_total - Para el precio total de la compra.
# precio_producto - Para el precio del producto. (Devoluciones)

# ESOS 3 REQUISITOS SON NECESARIOS PARA QUE FUNCIONEN LOS SIGUIENTES SERVICIOS:

class CalcularAgregarPuntosCompraActualizarRangoService(PuntosCompraActualizarRangoModelo):
    def obtener_y_asignar_nuevo_Rango(self, id_cliente):
        resultado = RangosService.actualizarRangoPorHistorialCompras(self, id_cliente)
        rango = resultado.get('nuevo_rango')
        if rango == 0:
            print(f"No se actualizo el rango de la cuenta del cliente {id_cliente} debido a que su cuenta se encuentra Inactiva/Suspendida y por ende no puede realizar acciones como obtener un rango.")
            return {"mensaje": "No se actualizo el rango de la cuenta del cliente {id_cliente} debido a que su cuenta se encuentra Inactiva/Suspendida y por ende no puede realizar acciones como obtener un rango."}
        else:
            print(f"Se ha actualizado el rango de la cuenta del cliente {id_cliente} en base al numero total de compras que ha realizado. Rango Asignado: {rango}")
            return {"mensaje": f"Se ha actualizado el rango de la cuenta del cliente {id_cliente} en base al numero total de compras que ha realizado. Rango Asignado: {rango}"}

    def calcular_y_agregar_puntos_compra(self, id_cliente, precio_compra_total):
        if precio_compra_total < 0:
            precio_compra_total = 0
            print("El valor de precio_compra_total no puede ser negativo. No se le calcularon ni agregaron puntos al cliente.")
            return {"mensaje": "El valor de precio_compra_total no puede ser negativo. No se le calcularon ni agregaron puntos al cliente."}
        else:
            resultado1 = RangosService.obtener_rango_cliente_y_porcentajeCompras(self, id_cliente)
            print(f"Diccionario del cliente: {resultado1}")
            
            #Verificamos si el cliente esta habilitado para recibir puntos
            habilitado = resultado1.get('habilitado')
            porcentaje_compra_puntos = resultado1.get('porcentaje_puntos')

            if habilitado != 1:
                print("El cliente no puede obtener puntos. Esto se debe a que su cuenta esta Inactiva/Suspendida y por ende no puede realizar acciones como obtener puntos.")
                return {"mensaje": "El cliente no puede obtener puntos. Esto se debe a que su cuenta esta Inactiva/Suspendida y por ende no puede realizar acciones como obtener puntos."}
            elif porcentaje_compra_puntos is None:
                print("No se encontró el porcentaje de puntos para el cliente.")
                return {"mensaje": "No se encontró el porcentaje de puntos para el cliente."}
            else:
                #Calculamos y agregamos a la cuenta del cliente los puntos obtenidos de la compra
                resultado2 = PuntosService.calcular_puntos_compra(self, precio_compra_total, porcentaje_compra_puntos)
                print(f"Los puntos de una compra han sido calculados correctamente. Puntos Compra Obtenidos: {resultado2}")
                puntos_compra = resultado2
                resultado3 = PuntosService.añadir_puntos_compra(self, id_cliente, puntos_compra)
                print(f"Los puntos de una compra han sido agregados correctamente a la cuenta del cliente en la BD. {id_cliente}")
                return {"mensaje": f"Los puntos de una compra han sido calculados y agregados correctamente a la cuenta del cliente {id_cliente}. Puntos Compra Obtenidos: {resultado2}"}

class CalcularAgregarPuntosDevolucionActualizarRangoService(PuntosDevolucionActualizarRangoModelo):
    def obtener_y_asignar_nuevo_Rango(self, id_cliente):
        resultado = RangosService.actualizarRangoPorHistorialCompras(self, id_cliente)
        rango = resultado.get('nuevo_rango')
        if rango == 0:
            print(f"No se actualizo el rango de la cuenta del cliente {id_cliente} debido a que su cuenta se encuentra Inactiva/Suspendida y por ende no puede realizar acciones como obtener un rango.")
            return {"mensaje": "No se actualizo el rango de la cuenta del cliente {id_cliente} debido a que su cuenta se encuentra Inactiva/Suspendida y por ende no puede realizar acciones como obtener un rango."}
        else:
            print(f"Se ha actualizado el rango de la cuenta del cliente {id_cliente} en base al numero total de compras que ha realizado. Rango Asignado: {rango}")
            return {"mensaje": f"Se ha actualizado el rango de la cuenta del cliente {id_cliente} en base al numero total de compras que ha realizado. Rango Asignado: {rango}"}

    def calcular_y_agregar_puntos_devolucion(self, id_cliente, precio_producto):
        if precio_producto < 0:
            precio_producto = 0
            print("El valor de precio_producto no puede ser negativo. No se le calcularon ni agregaron puntos al cliente.")
            return {"mensaje": "El valor de precio_producto no puede ser negativo. No se le calcularon ni agregaron puntos al cliente."}
        else:
            resultado1 = RangosService.obtener_rango_cliente_y_porcentajeDevolucion(self, id_cliente)
            print(f"Diccionario del cliente: {resultado1}")
            
            #Verificamos si el cliente esta habilitado para recibir puntos
            habilitado = resultado1.get('habilitado')
            porcentaje_devolucion_puntos = resultado1.get('porcentaje_devolucionPuntos')

            if habilitado != 1:
                print("El cliente no puede obtener puntos. Esto se debe a que su cuenta esta Inactiva/Suspendida y por ende no puede realizar acciones como obtener puntos de una devolucion.")
                return {"mensaje": "El cliente no puede obtener puntos. Esto se debe a que su cuenta esta Inactiva/Suspendida y por ende no puede realizar acciones como obtener puntos de una devolucion."}
            elif porcentaje_devolucion_puntos is None:
                print("No se encontro el porcentaje de puntos de devolucion para el cliente.")
                return {"mensaje": "No se encontro el porcentaje de puntos de devolucion para el cliente."}
            else:
                #Calculamos y agregamos a la cuenta del cliente los puntos obtenidos de la devolucion
                resultado2 = PuntosService.calcular_puntos_devolucion(self, precio_producto, porcentaje_devolucion_puntos)
                print(f"Los puntos de una devolucion han sido calculados correctamente. Puntos Devolucion Obtenidos: {resultado2}")
                puntos_devolucion = resultado2
                resultado3 = PuntosService.añadir_puntos_devolucion(self, id_cliente, puntos_devolucion)
                print(f"Los puntos de una devolucion han sido agregados correctamente a la cuenta del cliente en la BD. {id_cliente}")
                return {"mensaje": f"Los puntos de una devolucion han sido calculados y agregados correctamente a la cuenta del cliente {id_cliente}. Puntos Devolucion Obtenidos: {resultado2}"}

class PagarPuntosCompraActualizarRangoService(PagarPuntosActualizarRangoModelo):
    def obtener_y_asignar_nuevo_Rango(self, id_cliente):
        resultado = RangosService.actualizarRangoPorHistorialCompras(self, id_cliente)
        rango = resultado.get('nuevo_rango')
        if rango == 0:
            print(f"No se actualizo el rango de la cuenta del cliente {id_cliente} debido a que su cuenta se encuentra Inactiva/Suspendida y por ende no puede realizar acciones como obtener un rango.")
            return {"mensaje": "No se actualizo el rango de la cuenta del cliente {id_cliente} debido a que su cuenta se encuentra Inactiva/Suspendida y por ende no puede realizar acciones como obtener un rango."}
        else:
            print(f"Se ha actualizado el rango de la cuenta del cliente {id_cliente} en base al numero total de compras que ha realizado. Rango Asignado: {rango}")
            return {"mensaje": f"Se ha actualizado el rango de la cuenta del cliente {id_cliente} en base al numero total de compras que ha realizado. Rango Asignado: {rango}"}

    def pagar_con_puntos_compra(self, id_cliente, precio_compra_total):
        if precio_compra_total < 0:
            precio_compra_total = 0
            print("El valor de precio_compra_total no puede ser negativo. No se realizo la compra. Asi tambien no se le calcularon, agregaron o eliminaron puntos al cliente.")
            return {"mensaje": "El valor de precio_compra_total no puede ser negativo. No se realizo la compra. Asi tambien no se le calcularon, agregaron o eliminaron puntos al cliente."}
        else:
            resultado1 = RangosService.obtener_rango_cliente_y_porcentajeCompras(self, id_cliente)
            print(f"Diccionario del cliente: {resultado1}")
            
            #Verificamos si el cliente esta habilitado para realizar compras con puntos
            habilitado = resultado1.get('habilitado')

            if habilitado != 1:
                print("El cliente no puede realizar compras con puntos. Esto se debe a que su cuenta esta Inactiva/Suspendida y por ende no puede realizar acciones como comprar con puntos.")
                return {"mensaje": "El cliente no puede realizar compras con puntos. Esto se debe a que su cuenta esta Inactiva/Suspendida y por ende no puede realizar acciones como comprar con puntos."}
            else:
                #Calculamos y quitamos de la cuenta del cliente los puntos necesarios para la compra
                resultado2 = PuntosService.descontar_puntos(self, id_cliente, precio_compra_total)
                if resultado2.get('exito'):
                    puntos_restantes = resultado2.get('puntos_restantes')
                    print(f"La compra se ha realizado con exito y se le ha restado a la cuenta del cliente los puntos del precio total de la compra. {id_cliente}. Puntos Compra Restantes: {puntos_restantes}")
                    return {"mensaje": f"La compra se ha realizado con exito y se le ha restado a la cuenta del cliente los puntos del precio total de la compra. {id_cliente}. Puntos Compra Restantes: {puntos_restantes}"}
                else:
                    print(resultado2.get('mensaje'))
                    return {"mensaje": resultado2.get('mensaje')}

# ----------------------

# EJEMPLO DE USO 1 - COMPRAS (AGREGAR AL FINAL CUANDO SE CONFIRME LA COMPRA)
# PARA AÑADIR PUNTOS DE UNA COMPRA ES NECESARIO INGRESAR O TENER ALMACENADO LA INFORMACION
# DEL 'id_cliente' Y DE 'precio_compra_total' PARA PASARLOS A ESTOS 2 SERVICIOS.

# LA ESTRUCTURA ES LA SIGUIENTE:

# CalcularAgregarPuntosCompraActualizarRangoService().obtener_y_asignar_nuevo_Rango(id_cliente)
# CalcularAgregarPuntosCompraActualizarRangoService().calcular_y_agregar_puntos_compra(id_cliente, precio_compra_total)

# ----------------------

# EJEMPLO DE USO 2 - DEVOLUCIONES (AGREGAR AL FINAL CUANDO SE CONFIRME LA DEVOLUCION)
# PARA AÑADIR PUNTOS DE UNA DEVOLUCION ES NECESARIO INGRESAR O TENER ALMACENADO LA INFORMACION
# DEL 'id_cliente' Y DE 'precio_producto' PARA PASARLOS A ESTOS 2 SERVICIOS.

# LA ESTRUCTURA ES LA SIGUIENTE:

# CalcularAgregarPuntosDevolucionActualizarRangoService().obtener_y_asignar_nuevo_Rango(id_cliente)
# CalcularAgregarPuntosDevolucionActualizarRangoService().calcular_y_agregar_puntos_devolucion(id_cliente, precio_producto)

# ----------------------

# EJEMPLO DE USO 3 - COMPRAS CON PUNTOS COMO METODO DE PAGO (AGREGAR EN LA VALIDACION DONDE "metodo_pago = 'puntos'")
# PARA REALIZAR UNA COMPRA CON PUNTOS ES NECESARIO INGRESAR O TENER ALMACENADO LA INFORMACION
# DEL 'id_cliente' Y DE 'precio_compra_total' PARA PASARLOS A ESTOS 2 SERVICIOS.

# LA ESTRUCTURA ES LA SIGUIENTE:

# PagarPuntosCompraActualizarRangoService().obtener_y_asignar_nuevo_Rango(id_cliente)
# PagarPuntosCompraActualizarRangoService().pagar_con_puntos_compra(id_cliente, precio_compra_total)

# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------

# -> ¡PARA EL MODULO DE ATENCION A CLIENTES! <-
# FUNCIONALIDAD QUE DEVUELVE EL 'idrango' Y EL 'nombre_rango'
# EN BASE AL 'id_cliente' PROPORCIONADO.

# REQUISITOS
# id_cliente

# ESTE REQUISITO ES NECESARIO PARA QUE FUNCIONE ESTE SERVICIO.

class ObtenerRangoService(ObtenerRangoModelo):
    def obtener_rango_cliente_atencion(self, id_cliente):
        conexion = get_connection()
        try:
            with conexion.cursor() as cursor:
                #Comenzamos la transaccion
                conexion.begin()

                cursor.execute(
                    """
                    SELECT p.idclientes_puntos, p.idrango, r.nombre_rango, p.habilitado FROM puntos p
                    JOIN rangos r ON p.idrango = r.idrango
                    WHERE p.idclientes_puntos = %s
                    """, (id_cliente,)
                )
                #Confirmamos la transaccion
                conexion.commit()

                resultado = cursor.fetchone()

                if resultado:
                    print(f"idcliente_puntos: {resultado[0]}, idrango: {resultado[1]}, nombre_rango: {resultado[2]}, habilitado: {resultado[3]}")
                    return {"idcliente_puntos": resultado[0], "idrango": resultado[1], "nombre_rango": resultado[2], "habilitado": resultado[3]}
                else:
                    return {"mensaje": "Cliente no encontrado en la tabla 'puntos'. Esto se debe a que su cuenta esta Inactiva/Suspendida y por ende no se le asigno un rango."}

        except DatabaseError as e:
            #Deshacemos la transaccion en caso de error
            conexion.rollback()
            raise e
        finally:
            conexion.close()


# EJEMPLO DE USO
# PARA QUE RETORNE EL 'idrango' Y EL 'nombre_rango' DE ALGUN CLIENTE EN ESPECIFICO,
# ES NECESARIO INGRESAR O TENER ALMACENADO LA INFORMACION DEL 'id_cliente' PARA PASARLO A ESTE SERVICIO.

# LA ESTRUCTURA ES LA SIGUIENTE:

# ObtenerRangoService().obtener_rango_cliente_atencion(id_cliente)
    
# ---------------------------------------------------------------------------------------------------------------------------