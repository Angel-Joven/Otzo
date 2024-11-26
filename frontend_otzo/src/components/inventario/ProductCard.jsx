import React from "react";
import { motion } from "framer-motion";
import { descontinuarTipoProducto } from "../../api/inventario.api";

export default function ProductCard({
  imagen,
  titulo,
  categoria,
  cantidad,
  descripcion,
  precio,
  id,
  descontinuado,
  recargar,
  setRecargar,
  abrirEditar,
  productoAEditar,
  cambiarProductoAEditar,
}) {
  const descontinuarProducto = () => {
    descontinuarTipoProducto({
      nombre_tipo_producto: titulo,
      imagen_tipo_producto: imagen,
      categoria_tipo_producto: categoria,
      descripcion_tipo_producto: descripcion,
      precio_unitario: precio,
      cantidad_tipo_producto: cantidad,
      descontinuado: true,
      id_inventario: id,
    })
      .then((res) => {
        console.log(res.data);
        setRecargar(!recargar);
      })
      .catch((error) => {
        console.error(
          "No se pudo descontinuar el producto por un error: ",
          error
        );
      });
  };

  const reactivarProducto = () => {
    descontinuarTipoProducto({
      nombre_tipo_producto: titulo,
      imagen_tipo_producto: imagen,
      categoria_tipo_producto: categoria,
      descripcion_tipo_producto: descripcion,
      precio_unitario: precio,
      cantidad_tipo_producto: cantidad,
      descontinuado: false,
      id_inventario: id,
    })
      .then((res) => {
        console.log(res.data);
        setRecargar(!recargar);
      })
      .catch((error) => {
        console.error("No se pudo reactivar el producto por un error: ", error);
      });
  };

  const activarModalEditar = () => {
    cambiarProductoAEditar({
      nombre_tipo_producto: titulo,
      imagen_tipo_producto: imagen,
      categoria_tipo_producto: categoria,
      descripcion_tipo_producto: descripcion,
      precio_unitario: precio,
      cantidad_tipo_producto: cantidad,
      descontinuado: false,
      id_inventario: id,
    });
    abrirEditar(true);
  };

  return (
    <motion.div
      initial={{ scale: 0, opacity: 0 }}
      animate={{ scale: 1, opacity: 1, transition: { delay: 0.2 } }}
      className="bg-slate-800 text-white p-4 w-64 h-80 rounded-xl flex flex-col justify-between"
    >
      {/* Contenedor superior con imagen y etiquetas */}
      <div className="relative">
        <div className="w-full flex justify-center">
          <img src={imagen} alt="producto" className="w-1/2 object-contain" />
        </div>
        <p
          className={`absolute top-0 right-0 p-2 font-bold ${
            cantidad > 10 ? "text-green-500" : "text-red-500"
          }`}
        >
          {cantidad}
        </p>
        <p className="absolute top-0 left-0 p-1 font-bold bg-rose-600 rounded-xl">
          {categoria}
        </p>
      </div>

      {/* Texto del producto */}
      <div className="text-center flex-1 flex flex-col justify-center">
        <p className="font-bold text-xl truncate">{titulo}</p>
        <p className="font-bold text-sm truncate text-yellow-300">
          {precio} MXN
        </p>
        <p className="text-sm overflow-hidden text-ellipsis line-clamp-2">
          {descripcion}
        </p>
      </div>

      {/* Botones */}
      <div className="flex justify-center gap-4 py-2">
        {descontinuado ? null : (
          <button className="bg-green-500 rounded-lg p-2">
            <i className="align-middle fi fi-br-plus"></i>
          </button>
        )}
        <button
          onClick={activarModalEditar}
          className="bg-blue-500 rounded-lg p-2"
        >
          <i className="align-middle fi fi-sr-pencil"></i>
        </button>
        <button
          onClick={descontinuado ? reactivarProducto : descontinuarProducto}
          className={`${
            descontinuado ? "bg-green-500" : "bg-red-500"
          } rounded-lg p-2`}
        >
          {descontinuado ? (
            <i className="fi fi-sr-add"></i>
          ) : (
            <i className="fi fi-sr-clear-alt"></i>
          )}
        </button>
      </div>
    </motion.div>
  );
}
