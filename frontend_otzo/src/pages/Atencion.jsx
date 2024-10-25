import React from 'react';
import { motion } from 'framer-motion';

export function Atencion() {
   return (
    <>
      <div className='bg-gradient-to-r from-blue-400 to-blue-500 w-full h-full min-h-[calc(100vh-5rem)] z-0 relative'>
        <div>
          <motion.h1 initial={{scale: 0}} animate={{scale: 1, transition: {delay: 0.5}}} className='text-center text-white text-8xl font-bold'>Atención al Cliente</motion.h1>
        </div>
      </div>
    </>
  )
}