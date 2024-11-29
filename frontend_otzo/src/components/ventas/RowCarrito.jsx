import React from "react";

export default function RowCarrito({
  id_producto,
  nombre_producto,
  imagen_producto,
  cantidad_producto,
  precio_producto,
  cantidad,
  setCarrito,
}) {
  const handleAmount = (e) => {
    const nuevaCantidad = parseInt(e.target.value, 10); // Obtenemos la nueva cantidad ingresada

    setCarrito((prevCarrito) =>
      prevCarrito.map((producto) =>
        producto.id_producto === id_producto
          ? { ...producto, cantidad: nuevaCantidad } // Actualizamos la cantidad del producto
          : producto
      )
    );
  };

  return (
    <div className="p-2 flex items-center justify-between">
      <div className="flex items-center">
        <img src={imagen_producto} alt={nombre_producto} width={50} />
        <p>{nombre_producto}</p>
      </div>
      <div className="flex">
        <input
          type="number"
          name={`input_cantidad_${nombre_producto}`}
          id={`input_cantidad_${nombre_producto}`}
          step={"1"}
          value={cantidad} //CAMBIAR DEFAULT VALUE 1
          onChange={handleAmount} //CAMBIAR SETCARRITO
          max={cantidad_producto}
          min={1}
        />
        <p>
          X{" "}
          <span className="text-green-500 font-bold">
            {precio_producto} MXN
          </span>
        </p>
      </div>
    </div>
  );
}
