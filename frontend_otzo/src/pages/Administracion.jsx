/*

Pagina Principal para el Modulo de Administracion
Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

Temas Especiales de Programacion 2 | 1061

*/

import { React, useEffect, useState } from "react";
import { motion } from "framer-motion";

export function Administracion() {
    return (
     <>
       <div className='bg-gradient-to-r from-red-400 to-red-500 w-full h-full min-h-[calc(100vh-5rem)] z-0 relative'>
         <div>
           <motion.h1 initial={{scale: 0}} animate={{scale: 1, transition: {delay: 0.5}}} className='text-center text-white text-6xl font-bold'>Administracion</motion.h1>
         </div>
       </div>
     </>
   )
}