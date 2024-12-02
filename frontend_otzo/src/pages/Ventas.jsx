import React, { useState, useEffect } from "react";
import DataTable from "react-data-table-component";
import Spinner from "../components/ventas/Spinner";
import { obtenerTodosLosProductosAVender } from "../api/inventario.api";
import { obtenerAdministradores } from "../api/administracion.api";
import { agregarCompra } from "../api/ventas.api";
import RowCarrito from "../components/ventas/RowCarrito";
import { ObtenerTipoUsuario } from "../context/obtenerUsuarioTipo";

export function Ventas() {
  const { clienteActual, idCliente } = ObtenerTipoUsuario();

  const [administrador, setAdministrador] = useState();

  const [productos, setProductos] = useState([]);
  const [loadingData, setLoadingData] = useState(true);

  const [carrito, setCarrito] = useState([]);

  const [total, setTotal] = useState(0);

  const [cambio, setCambio] = useState(0);

  const [montoRecibido, setMontoRecibido] = useState(0);

  const [metodoPago, setMetodoPago] = useState("efectivo");

  const cambioMetodoPago = (e) => {
    setMetodoPago(e.target.value);
  };

  const [abrirModalCompra, setAbrirModalCompra] = useState(false);

  const manejarAbrirModalCompra = (e) => {
    // Cierra el diálogo si se hace clic fuera del recuadro
    if (e.target.id === "modalCompra") {
      setAbrirModalCompra(false);
      setCambio(0);
    }
  };

  //  Internally, customStyles will deep merges your customStyles with the default styling.
  const customStyles = {
    rows: {
      style: {
        maxHeight: "64px", // override the row height
      },
    },
    headCells: {
      style: {
        paddingLeft: "16px", // override the cell padding for head cells
        paddingRight: "16px",
      },
    },
    cells: {
      style: {
        paddingLeft: "16px", // override the cell padding for data cells
        paddingRight: "16px",
      },
    },
  };

  useEffect(() => {
    // Obtiene los administradores
    obtenerAdministradores().then((res) => {
      const administradores = res.data;
      const indiceAleatorio = Math.floor(
        Math.random() * administradores.length
      );
      const administrador = administradores[indiceAleatorio];
      setAdministrador(administrador.id_empleado);
    });
  }, []);

  const agregarAlCarrito = (producto) => {
    setCarrito((prevCarrito) => {
      // Verificar si el producto ya está en el carrito
      const productoExistente = prevCarrito.find(
        (item) => item.id_inventario === producto.id_inventario
      );

      if (productoExistente) {
        return [...prevCarrito];
      } else {
        // Agregar el producto con cantidad inicial de 1
        return [...prevCarrito, { ...producto, cantidad: 1 }];
      }
    });
  };

  useEffect(() => {
    // Calcula el nuevo total sumando los precios en base a la cantidad
    const nuevoTotal = carrito.reduce(
      (acumulador, producto) =>
        acumulador + producto.cantidad * producto.precio_unitario,
      0 // Valor inicial del acumulador
    );
    setTotal(nuevoTotal); // Actualiza el total con el nuevo cálculo
  }, [carrito]);

  const eliminarDelCarrito = (id_producto) => {
    setCarrito((prevCarrito) =>
      prevCarrito.filter((producto) => producto.id_inventario !== id_producto)
    );
  };

  const comprobarCambio = (e) => {
    setCambio(e.target.value - total);
    setMontoRecibido(e.target.value);
  };

  useEffect(() => {
    if (metodoPago != "efectivo") {
      setCambio(0);
    }
  }, [metodoPago]);

  //Cargar productos
  useEffect(() => {
    obtenerTodosLosProductosAVender()
      .then((res) => {
        console.log(res.data);
        setProductos(res.data);
        setLoadingData(false);
      })
      .catch((error) => {
        console.error("Error al obtener los productos:", error);
      });
  }, []);

  const procesarCompra = () => {
    // Validar que el carrito no esté vacío
    if (carrito.length === 0) {
      alert("El carrito está vacío. Agrega productos antes de comprar.");
      return;
    }

    // Validar si el método de pago es efectivo y el monto es suficiente
    if (metodoPago === "efectivo" && cambio < 0) {
      alert("El monto proporcionado no es suficiente para cubrir el total.");
      return;
    }

    // Preparar los datos para enviar al backend
    const datosCompra = {
      productos: carrito.map(
        ({
          cantidad_maxima_producto,
          cantidad_producto,
          categoria_producto,
          descontinuado,
          descripcion_producto,
          id_inventario,
          imagen_producto,
          nombre_producto,
          precio_unitario,
          cantidad,
        }) => ({
          cantidad_maxima_producto,
          cantidad_producto,
          categoria_producto,
          descontinuado,
          descripcion_producto,
          id_inventario,
          imagen_producto,
          nombre_producto,
          precio_unitario,
          cantidad,
        })
      ),
      total,
      metodo_pago: metodoPago,
      monto_recibido: montoRecibido,
      id_cliente: idCliente,
      id_empleado: administrador,
    };

    console.log(datosCompra);

    // Enviar los datos de compra al backend
    agregarCompra(datosCompra)
      .then((res) => {
        alert("Compra procesada con éxito.");
        // Resetear estados
        setCarrito([]);
        setTotal(0);
        setCambio(0);
        setAbrirModalCompra(false);
      })
      .catch((error) => {
        console.error("Error al procesar la compra:", error);
        alert("Hubo un problema al procesar la compra. Intenta de nuevo.");
      });
  };

  const columns = [
    {
      name: "Acciones",
      cell: (row) => (
        <button
          onClick={() => {
            agregarAlCarrito(row);
          }}
          className="bg-green-500 p-2 text-white font-bold"
        >
          <i className="fi fi-sr-shopping-cart-add"></i> Agregar
        </button>
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

  return (
    <>
      <div className="bg-gradient-to-b from-green-500 to-green-900 w-full h-full min-h-[calc(100vh-5rem)] z-0 relative">
        {abrirModalCompra && (
          <dialog
            id="modalCompra"
            className="absolute top-0 right-0 left-0 bottom-0 z-10 w-full h-full bg-slate-900/80 flex justify-center items-center"
            onClick={manejarAbrirModalCompra}
          >
            <div
              className="min-h-[50%] min-w-[50%] bg-white rounded-xl p-4 flex flex-col gap-4"
              onClick={(e) => e.stopPropagation()} // Evita cerrar al hacer clic dentro del recuadro
            >
              <p className="font-bold">RESUMEN DE COMPRA:</p>
              <p>Total: {total} MXN</p>
              <p>Metodo de pago:</p>
              <select
                name="metodo_pago"
                id="metodo_pago"
                onChange={cambioMetodoPago}
              >
                <option value="efectivo">Efectivo</option>
                <option value="tarjeta">Tarjeta</option>
                <option value="puntos">Puntos</option>
              </select>
              <label htmlFor="input_metodo_pago">
                Monto dado por el cliente:{" "}
              </label>
              {metodoPago == "efectivo" && (
                <>
                  <input
                    type="text"
                    className="block"
                    id="input_metodo_pago"
                    onChange={comprobarCambio}
                  />
                  <p>Cambio: {cambio}</p>
                </>
              )}
              <button
                className="bg-yellow-300 font-bold p-2"
                onClick={procesarCompra}
              >
                Comprar
              </button>
            </div>
          </dialog>
        )}

        <div className="flex justify-between text-center bg-green-800 text-white py-4 px-8">
          <h1 className="text-2xl font-bold">Ventas</h1>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 grid-rows-1 gap-4 p-2">
          <div className="bg-white">
            <div className="bg-gray-900 text-white p-4">
              <p className="font-bold">Productos</p>
            </div>
            <div>
              <DataTable
                columns={columns}
                data={productos}
                fixedHeader
                progressPending={loadingData}
                progressComponent={<Spinner />}
                theme="default"
                customStyles={customStyles}
                striped={true}
                dense={true}
                pagination={true}
                paginationPerPage={5}
                paginationRowsPerPageOptions={[5, 10]}
              />
            </div>
          </div>
          <div className="bg-white">
            <div className="bg-gray-900 text-white p-4 flex justify-between items-center">
              <p className="font-bold">Carrito</p>
              <button
                className="bg-green-500 font-bold p-1"
                onClick={() => {
                  setAbrirModalCompra(true);
                }}
              >
                COMPRAR
              </button>
            </div>
            <div>
              {carrito.map((producto, index) => {
                return (
                  <RowCarrito
                    id_producto={producto.id_inventario}
                    nombre_producto={producto.nombre_producto}
                    imagen_producto={producto.imagen_producto}
                    cantidad_producto={producto.cantidad_producto}
                    precio_producto={producto.precio_unitario}
                    cantidad={producto.cantidad}
                    setCarrito={setCarrito}
                    carrito={carrito}
                    eliminarDelCarrito={eliminarDelCarrito}
                    key={index}
                  />
                );
              })}
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
