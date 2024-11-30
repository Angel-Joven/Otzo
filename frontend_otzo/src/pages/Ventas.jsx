import React, { useState, useEffect } from "react";
import DataTable from "react-data-table-component";
import Spinner from "../components/ventas/Spinner";
import { obtenerTodosLosProductosAVender } from "../api/inventario.api";
import RowCarrito from "../components/ventas/RowCarrito";

export function Ventas() {
  const [productos, setProductos] = useState([]);
  const [loadingData, setLoadingData] = useState(true);

  const [carrito, setCarrito] = useState([]);

  const [total, setTotal] = useState(0);

  const [cambio, setCambio] = useState(0);

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

  const comprobarCambio = (e) => {
    setCambio(e.target.value - total);
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
              <button className="bg-yellow-300 font-bold p-2">Comprar</button>
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
