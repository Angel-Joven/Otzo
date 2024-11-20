import { React, useEffect, useState } from "react";
import { motion } from "framer-motion";

export function Reportes() {
    return (
     <>
       <div className='bg-gradient-to-r from-gray-400 to-gray-500 w-full h-full min-h-[calc(100vh-5rem)] z-0 relative'>
         <div>
           <motion.h1 initial={{scale: 0}} animate={{scale: 1, transition: {delay: 0.5}}} className='text-center text-white text-6xl font-bold'>Reportes y Analisis</motion.h1>
         </div>
       </div>
     </>
   )
}