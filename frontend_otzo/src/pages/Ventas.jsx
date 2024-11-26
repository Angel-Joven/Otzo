import { React, useEffect, useState } from "react";
import { motion } from "framer-motion";
import DataTable from "react-data-table-component";
import "@flaticon/flaticon-uicons/css/all/all.css";
import Spinner from "../components/ventas/Spinner";
import axios from "axios";

import { obtenerTodosLosProductos } from "../api/inventario.api";

export function Ventas() {
  // TABLA PRODUCTOS:
  const [records, setRecords] = useState([]);
  const [loading, setLoading] = useState(true);

  const columns = [
    {
      name: "Acciones",
      cell: (row) => (
        <motion.button
          whileHover={{ scale: 1.1 }}
          whileTap={{ scale: 0.9 }}
          onClick={() => agregarAlCarrito(row)}
          className="bg-green-500 p-2 rounded-xl text-white font-bold"
        >
          <i className="fi fi-sr-shopping-cart-add"></i> Agregar
        </motion.button>
      ),
    },
    {
      name: "ID",
      selector: (row) => row.id_inventario,
    },
    {
      name: "Imagen",
      cell: (row) => <img src={row.imagen_producto} width={50} />,
    },
    {
      name: "Nombre",
      selector: (row) => row.nombre_producto,
    },
    {
      name: "Disponibles",
      selector: (row) => row.cantidad_producto,
    },
    {
      name: "Precio",
      selector: (row) => "$" + row.precio_unitario + " MXN",
    },
    {
      name: "Categoria",
      selector: (row) => row.categoria_producto,
    },
  ];

  const customStyles = {
    cells: {
      style: {
        padding: "2px", // Reduce el espacio interior de las celdas
      },
    },
    rows: {
      style: {
        minHeight: "20px", // Reduce la altura mínima de las filas
      },
    },
    headCells: {
      style: {
        padding: "2px", // Reduce el espacio interior de las celdas de encabezado
      },
    },
  };

  // TODO: CARGAR DATA DEL BACKEND
  useEffect(() => {
    obtenerTodosLosProductos()
      .then((res) => {
        console.log(res.data);
        setRecords(res.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error al obtener los productos:", error);
      });
  }, []);

  const handleChange = (e) => {
    const filteredRecords = data.filter((record) => {
      return record.producto
        .toLowerCase()
        .includes(e.target.value.toLowerCase());
    });

    setRecords(filteredRecords);
  };

  //TABLA CARRITO:
  // Añade este estado para manejar los productos en el carrito
  const [carrito, setCarrito] = useState([]);

  // Modifica la función agregarAlCarrito
  const agregarAlCarrito = (producto) => {
    setCarrito((prevCarrito) => {
      // Verifica si el producto ya está en el carrito
      const productoExistente = prevCarrito.find(
        (item) => item.nombre_producto === producto.nombre_producto
      );

      if (productoExistente) {
        // Si el producto ya existe, incrementa la cantidad sin exceder el máximo disponible
        return prevCarrito.map((item) =>
          item.nombre_producto === producto.nombre_producto
            ? {
                ...item,
                cantidad_producto: Math.min(
                  item.cantidad + 1,
                  item.cantidad_producto
                ),
              }
            : item
        );
      } else {
        // Si el producto no existe, añádelo al carrito con una cantidad inicial de 1
        return [...prevCarrito, { ...producto, cantidad: 1 }];
      }
    });
  };

  // Función para manejar cambios en la cantidad directamente en el carrito
  const actualizarCantidad = (producto, nuevaCantidad) => {
    setCarrito((prevCarrito) =>
      prevCarrito.map((item) =>
        item.nombre_producto === producto.nombre_producto
          ? {
              ...item,
              cantidad: Math.min(
                Math.max(nuevaCantidad, 1),
                item.cantidad_producto
              ),
            }
          : item
      )
    );
  };

  // Función para eliminar un producto del carrito
  const eliminarDelCarrito = (producto) => {
    setCarrito((prevCarrito) => {
      const nuevoCarrito = prevCarrito.filter(
        (item) => item.nombre_producto !== producto.nombre_producto
      );
      return nuevoCarrito;
    });
  };

  // Función para calcular el total de la compra
  const calcularTotal = () => {
    return carrito
      .reduce(
        (total, item) => total + item.precio_unitario * item.cantidad_producto,
        0
      )
      .toFixed(2);
  };

  // Nuevo estado para el método de pago
  const [metodoPago, setMetodoPago] = useState("Tarjeta de crédito");

  // Nuevo estado para el efectivo dado
  const [efectivoDado, setEfectivoDado] = useState();
  const [cambio, setCambio] = useState(0);

  // Función para manejar el cambio cuando el efectivo dado cambia
  const manejarEfectivoDado = (e) => {
    const montoEfectivo = parseFloat(e.target.value) || 0;
    setEfectivoDado(montoEfectivo);
    setCambio((montoEfectivo - calcularTotal()).toFixed(2));
  };

  useEffect(() => {
    if (metodoPago === "Efectivo") {
      setCambio((efectivoDado - calcularTotal()).toFixed(2));
    }
  }, [carrito, efectivoDado]);

  // ... (función para calcular el total)

  // Función para manejar la compra, ahora incluye el cálculo del cambio si se paga en efectivo
  const manejarCompra = async () => {
    const datosCompra = {
      detalles_venta: carrito.map((item) => ({
        producto: item.nombre_producto,
        cantidad: item.cantidad_producto,
        precio: item.precio_unitario,
      })),
      metodo_pago: metodoPago,
      total: calcularTotal(),
      monto_recibido: metodoPago === "Efectivo" ? efectivoDado : null, // Enviar efectivo dado solo si es en efectivo
      cambio: metodoPago === "Efectivo" ? cambio : null, // Enviar el cambio solo si es en efectivo
      id_cliente: 1,
      id_empleado: 1,
    };

    try {
      const respuesta = await axios.post(
        "http://localhost:5000/api/ventas/test",
        datosCompra
      );
      console.log("Respuesta del backend:", respuesta.data);
      alert("Compra realizada exitosamente");
    } catch (error) {
      console.error("Error al realizar la compra:", error);
      alert("Hubo un error al realizar la compra. Intenta nuevamente.");
    }
  };

  return (
    <>
      <div className="bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-lime-500 via-green-500 to-green-500 w-full h-full min-h-[calc(100vh-5rem)] z-0 relative">
        <div>
          <motion.h1
            initial={{ scale: 0 }}
            animate={{ scale: 1, transition: { delay: 0.5 } }}
            className="text-center text-white text-3xl md:text-6xl font-bold"
          >
            Ventas
          </motion.h1>
        </div>

        <div className="grid grid-cols-1 grid-rows-1 gap-x-2.5 xl:grid-cols-2">
          <div className="w-full h-full p-4">
            <motion.div
              initial={{ x: -200, opacity: 0 }}
              animate={{ x: 0, opacity: 1, transition: { delay: 0.8 } }}
              className="bg-white/100 rounded-lg p-4 shadow-[0px_4px_6px_0px_rgba(0,_0,_0,_0.1)]"
            >
              <div className="rounded-lg p-4 bg-gray-900 z-10">
                <h2 className="font-bold text-white">
                  <i className="align-middle fi fi-sr-boxes"></i> Productos
                </h2>
              </div>
              <div className="h-[calc(25vh)] md:h-[calc(50vh)]">
                <div className="p-4 h-full overflow-y-auto">
                  <div className="w-full flex gap-4 items-center">
                    <i className="align-middle fi fi-bs-search"></i>
                    <input
                      className="w-full bg-transparent placeholder:text-gray-900 text-green-700 text-sm border border-gray-200 rounded-md px-3 py-2 transition duration-300 ease focus:outline-none focus:border-green-500 hover:border-green-300 focus:hover:placeholder:text-green-700 shadow-sm focus:shadow"
                      placeholder="Buscar..."
                      onChange={handleChange}
                    />
                  </div>
                  <DataTable
                    className="p-1"
                    columns={columns}
                    data={records}
                    fixedHeader
                    customStyles={customStyles}
                    progressPending={loading}
                    progressComponent={<Spinner />}
                  />
                  {/* selectableRows */}
                </div>
              </div>
            </motion.div>
          </div>

          <div className="w-full h-full p-4">
            <motion.div
              initial={{ x: 200, opacity: 0 }}
              animate={{ x: 0, opacity: 1, transition: { delay: 0.8 } }}
              className="bg-white/100 rounded-lg p-4 shadow-[0px_4px_6px_0px_rgba(0,_0,_0,_0.1)]"
            >
              <div className="rounded-lg p-4 bg-gray-900">
                <h2 className="font-bold text-white">
                  <i className="align-middle fi fi-sr-shopping-cart"></i>{" "}
                  Carrito
                </h2>
              </div>
              <div className="h-[calc(25vh)] md:h-[calc(50vh)]">
                {carrito.length > 0 ? (
                  carrito.map((item, index) => (
                    <div
                      key={index}
                      className="flex justify-between items-center mb-2 px-4 py-2"
                    >
                      <span className="font-bold">{item.nombre_producto}</span>
                      <div className="flex items-center gap-2">
                        <input
                          type="number"
                          className="w-16 text-center border rounded-md"
                          value={item.cantidad_producto}
                          onChange={(e) =>
                            actualizarCantidad(
                              item,
                              parseInt(e.target.value, 10)
                            )
                          }
                        />
                        <span>x ${item.precio_unitario.toFixed(2)} MXN</span>
                        <button
                          onClick={() => eliminarDelCarrito(item)}
                          className="bg-red-500 p-1 rounded-full text-white"
                        >
                          <i className="fi fi-sr-trash"></i>
                        </button>
                      </div>
                    </div>
                  ))
                ) : (
                  <p className="text-center">El carrito está vacío.</p>
                )}
              </div>
              {/* Sección del total, método de pago y botón de compra */}
              <div className="mt-4 p-4 bg-gray-100 rounded-lg">
                <h3 className="font-bold text-xl">
                  Total:{" "}
                  <span className="text-green-700">${calcularTotal()} MXN</span>
                </h3>
                <label
                  htmlFor="metodoPago"
                  className="block mt-2 mb-1 font-medium"
                >
                  Método de pago:
                </label>
                <select
                  id="metodoPago"
                  value={metodoPago}
                  onChange={(e) => setMetodoPago(e.target.value)}
                  className="w-full p-2 border rounded-md"
                >
                  <option value="Tarjeta de crédito">Tarjeta de crédito</option>
                  <option value="Tarjeta de débito">Tarjeta de débito</option>
                  <option value="PayPal">PayPal</option>
                  <option value="Transferencia bancaria">
                    Transferencia bancaria
                  </option>
                  <option value="Efectivo">Efectivo</option>
                </select>

                {metodoPago === "Efectivo" && (
                  <div className="mt-4">
                    <label
                      htmlFor="efectivoDado"
                      className="block mb-2 font-medium"
                    >
                      Monto dado por el cliente:
                    </label>
                    <input
                      type="number"
                      id="efectivoDado"
                      value={efectivoDado}
                      onChange={manejarEfectivoDado}
                      className="w-full p-2 border rounded-md"
                      placeholder="Ingresa el monto dado"
                    />
                    {efectivoDado > 0 && (
                      <div className="mt-2">
                        <p>
                          Cambio: <strong>${cambio} MXN</strong>
                        </p>
                      </div>
                    )}
                  </div>
                )}

                <button
                  onClick={manejarCompra}
                  className="mt-4 bg-green-500 p-3 rounded-xl w-full text-white font-bold"
                >
                  Comprar ahora
                </button>
              </div>
            </motion.div>
          </div>
        </div>
      </div>
    </>
  );
}
