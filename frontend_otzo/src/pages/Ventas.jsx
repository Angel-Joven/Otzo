import { React, useEffect, useState } from "react";
import { motion } from "framer-motion";
import DataTable from "react-data-table-component";
import "@flaticon/flaticon-uicons/css/all/all.css";
import Spinner from "../components/Spinner";

export function Ventas() {
  const columns = [
    {
      name: "Acciones",
      cell: (row) => (
        <button
          onClick={() => manejarboton(row)}
          className="bg-green-500 p-2 rounded-xl text-white font-bold"
        >
          <i className="fi fi-sr-shopping-cart-add"></i> Agregar
        </button>
      ),
    },
    {
      name: "Producto",
      selector: (row) => row.producto,
    },
    {
      name: "Cantidad",
      selector: (row) => row.disponibles,
    },
    {
      name: "Precio",
      selector: (row) => row.precio,
    },
    {
      name: "Categoria",
      selector: (row) => row.precio,
    },
  ];

  const data = [
    {
      producto: "Coca cola",
      disponibles: 10,
      precio: 12.5,
      categoria: "Bebida",
    },
    {
      producto: "Sabritas",
      disponibles: 15,
      precio: 18.5,
      categoria: "Snack",
    },
    {
      producto: "Donitas",
      disponibles: 15,
      precio: 18.5,
      categoria: "Snack",
    },
    {
      producto: "Pepsi",
      disponibles: 15,
      precio: 18.5,
      categoria: "Snack",
    },
    {
      producto: "Maruchan",
      disponibles: 15,
      precio: 18.5,
      categoria: "Snack",
    },
    {
      producto: "Sabritas",
      disponibles: 15,
      precio: 18.5,
      categoria: "Snack",
    },
  ];

  const manejarboton = (row) => {
    console.log(row);
  };

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

  const [records, setRecords] = useState([]);
  const [loading, setLoading] = useState(true);

  // TODO: CARGAR DATA DEL BACKEND
  useEffect(() => {
    const timeout = setTimeout(() => {
      setRecords(data);
      setLoading(false);
    }, 2000);

    return () => clearTimeout(timeout);
  }, []);

  const handleChange = (e) => {
    const filteredRecords = data.filter((record) => {
      return record.producto
        .toLowerCase()
        .includes(e.target.value.toLowerCase());
    });

    setRecords(filteredRecords);
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
        <div className="grid grid-cols-1 grid-rows-1 gap-x-2.5 md:grid-cols-2">
          <div className="w-full h-full p-4">
            <motion.div
              initial={{ x: -200, opacity: 0 }}
              animate={{ x: 0, opacity: 1, transition: { delay: 0.8 } }}
              className="w-full h-full bg-white/100 rounded-lg p-4 shadow-[0px_4px_6px_0px_rgba(0,_0,_0,_0.1)]"
            >
              <div className="shadow-lg rounded-lg p-4 bg-gray-900 z-10">
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
                    columns={columns}
                    data={records}
                    fixedHeader
                    customStyles={customStyles}
                    progressPending={loading}
                    progressComponent={<Spinner />}
                    onSelectedRowsChange={(data) => console.log(data)}
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
              className="w-full h-full bg-white/100 rounded-lg p-4 shadow-[0px_4px_6px_0px_rgba(0,_0,_0,_0.1)]"
            >
              <div className="shadow-lg rounded-lg p-4 bg-gray-900">
                <h2 className="font-bold text-white">
                  <i className="align-middle fi fi-sr-shopping-cart"></i>{" "}
                  Carrito
                </h2>
              </div>
              <div className="h-[calc(25vh)] md:h-[calc(50vh)]"></div>
            </motion.div>
          </div>
        </div>
        <div className="hidden p-4 flex justify-center md:justify-end">
          <div className="bg-white p-3 w-full md:w-auto md:p-4 rounded-lg">
            <h3 className="font-bold text-3xl mb-4">
              <span className="text-red-400">Total: </span>$250 MXN
            </h3>
            <button className="bg-green-500 p-3 rounded-xl w-full text-white font-bold">
              Pagar ahora
            </button>
          </div>
        </div>
      </div>
    </>
  );
}
