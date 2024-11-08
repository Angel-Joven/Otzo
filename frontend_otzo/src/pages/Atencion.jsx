import React from 'react';
import { motion } from 'framer-motion';
import DataTable from 'react-data-table-component';
import Spinner from '../components/Spinner';

export function Atencion() {
  return (
    <>
      <div className='bg-gradient-to-r from-blue-400 to-blue-500 w-full h-full min-h-[calc(100vh-5rem)] z-0 relative'>
        <div>
          <motion.h1 initial={{scale: 0}} animate={{scale: 1, transition: {delay: 0.5}}} className='text-center text-white text-6xl font-bold'>Atención al Cliente</motion.h1>
        </div>
        <div className="grid grid-cols-1 grid-rows-1 gap-x-2.5 md:grid-cols-1">
          <div className="w-full h-full p-4">
            <motion.div
              initial={{ x: 200, opacity: 0 }}
              animate={{ x: 0, opacity: 1, transition: { delay: 0.8 } }}
              className="w-full h-full bg-white/100 rounded-lg p-4 shadow-[0px_4px_6px_0px_rgba(0,_0,_0,_0.1)]"
            >
              <div className="shadow-lg rounded-lg p-4 bg-gray-900">
                <h2 className="font-bold text-white">
                  <i className="align-middle fi fi-sr-document"></i>{" "}
                  Quejas
                </h2>
              </div>
              <div className="overflow-x-auto">
                  <table className="min-w-full bg-white">
                  <thead>
                    <tr>
                      <th className="py-2 px-4 border-b text-center">ID Queja</th>
                      <th className="py-2 px-4 border-b text-center">ID Cliente</th>
                      <th className="py-2 px-4 border-b text-center">ID Empleado</th>
                      <th className="py-2 px-4 border-b text-center">Rango Usuario</th>
                      <th className="py-2 px-4 border-b text-center">Descripción</th>
                      <th className="py-2 px-4 border-b text-center">Categoría</th>
                      <th className="py-2 px-4 border-b text-center">Estado de la Queja</th>
                      <th className="py-2 px-4 border-b text-center">Prioridad</th>
                      <th className="py-2 px-4 border-b text-center">Seguimiento</th>
                    </tr>
                  </thead>
                  <tbody>
                  </tbody>
                </table>
                </div>
              <div className="h-[calc(25vh)] md:h-[calc(50vh)]"></div>
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
                  <i className="align-middle fi fi-sr-document"></i>{" "}
                  Sugerencias
                </h2>
              </div>
              <div className="overflow-x-auto">
                  <table className="min-w-full bg-white">
                  <thead>
                    <tr>
                      <th className="py-2 px-4 border-b text-center">ID Sugerencia</th>
                      <th className="py-2 px-4 border-b text-center">ID Cliente</th>
                      <th className="py-2 px-4 border-b text-center">ID Empleado</th>
                      <th className="py-2 px-4 border-b text-center">Descripción</th>
                      <th className="py-2 px-4 border-b text-center">Categoría</th>
                      <th className="py-2 px-4 border-b text-center">Estado de la Sugerencia</th>
                      <th className="py-2 px-4 border-b text-center">Seguimiento</th>
                    </tr>
                  </thead>
                  <tbody>
                  </tbody>
                </table>
                </div>
              <div className="h-[calc(25vh)] md:h-[calc(50vh)]"></div>
            </motion.div>
          </div>
        </div>
      </div>
    </>
  )
}