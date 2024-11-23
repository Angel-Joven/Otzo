import { obtenerTodosLosProductos } from "../api/inventario.api";
import React, { useState, useEffect } from "react";
import { motion } from "framer-motion";
import ProductCard from "../components/inventario/ProductCard";

function Inventario() {
  const columns = [
    {
      name: "ID",
      selector: (row) => row.id_inventario,
    },
    {
      name: "Imagen",
      cell: (row) => <img src={row.imagen_producto} className="max-w-20" />,
    },
    {
      name: "Nombre",
      selector: (row) => row.nombre_producto,
    },
    {
      name: "Categoria",
      selector: (row) => row.categoria_producto,
    },
    {
      name: "Cantidad",
      selector: (row) => row.cantidad_producto,
    },
    {
      name: "Descripción",
      selector: (row) => row.descripcion_producto,
    },
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
  ];
  const [data, setData] = useState();
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    obtenerTodosLosProductos()
      .then((res) => {
        console.log(res.data);
        setData(res.data);
        setIsLoading(false);
      })
      .catch((error) => {
        console.error("Error al obtener los productos:", error);
        setIsLoading(false);
      });
  }, []);

  return (
    <>
      <div className="bg-gradient-to-r from-slate-600 to-gray-500 w-full h-full min-h-[calc(100vh-5rem)] z-0 relative">
        <div className="flex justify-between text-center bg-slate-800 text-white py-4 px-8">
          <h1 className="text-2xl font-bold">Inventario de productos</h1>
          <button className="bg-green-500 p-2 rounded-xl">
            <i className="align-middle fi fi-br-plus"></i> Añadir producto
          </button>
        </div>
        {isLoading ? (
          <p className="text-center text-white font-bold text-2xl p-4">
            Cargando productos...
          </p>
        ) : (
          <div className="flex p-4">
            {data.map((producto, index) => {
              return (
                <ProductCard
                  key={index}
                  imagen={producto.imagen_producto}
                  titulo={producto.nombre_producto}
                  cantidad={producto.cantidad_producto}
                  categoria={producto.categoria_producto}
                  descripcion={producto.descripcion_producto}
                />
              );
            })}
          </div>
        )}
      </div>
    </>
  );
}

export default Inventario;
