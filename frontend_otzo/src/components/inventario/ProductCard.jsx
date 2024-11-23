import React from "react";
import { motion } from "framer-motion";

export default function ProductCard({
  imagen,
  titulo,
  categoria,
  cantidad,
  descripcion,
}) {
  return (
    <motion.div
      initial={{ scale: 0, opacity: 0 }}
      animate={{ scale: 1, opacity: 1, transition: { delay: 0.2 } }}
      className="bg-slate-800 text-white p-2 w-64 rounded-xl"
    >
      <div className="relative">
        <img src={imagen} alt="producto" className="w-24 m-auto" />
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
      <div className="text-center">
        <p className="font-bold text-xl truncate">{titulo}</p>
        <p className="overflow-ellipsis truncate">{descripcion}</p>
      </div>
      <div className="flex justify-center gap-4 py-2">
        <button className="bg-green-500 rounded-2xl p-2">
          <i className="align-middle fi fi-br-plus"></i>
        </button>
        <button className="bg-blue-500 rounded-2xl p-2">
          <i className="align-middle fi fi-sr-pencil"></i>
        </button>
        <button className="bg-red-500 rounded-2xl p-2">
          <i className="align-middle fi fi-br-minus"></i>
        </button>
      </div>
    </motion.div>
  );
}
