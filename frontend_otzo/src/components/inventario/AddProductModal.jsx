import React, { useState } from "react";

export default function AddProductModal({ modalName, modalContent }) {
  const [isModalOpen, setIsModalOpen] = useState(false);

  const handleModalToClose = (e) => {
    // Cierra el diálogo si se hace clic fuera del recuadro
    if (e.target.id === "modal" + modalName) {
      setIsModalOpen(false);
    }
  };

  return (
    <dialog
      id={`modal${modalName}`}
      className="absolute top-0 right-0 left-0 bottom-0 z-10 w-full h-full bg-slate-900/80 flex justify-center items-center"
      onClick={handleModalToClose}
    >
      <div
        className="min-h-[50%] min-w-[50%] bg-white rounded-xl p-4 flex flex-col gap-4"
        onClick={(e) => e.stopPropagation()} // Evita cerrar al hacer clic dentro del recuadro
      >
        <p>CONTENIDO</p>
      </div>
    </dialog>
  );
}
