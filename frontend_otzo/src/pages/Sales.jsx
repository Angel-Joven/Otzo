import React from 'react';
import { motion } from 'framer-motion';

export function Sales() {
  return (
    <>
      <div className='bg-gradient-to-r from-lime-400 to-lime-500 w-full h-full min-h-[calc(100vh-5rem)] z-0 relative'>
        <div>
          <motion.h1 initial={{scale: 0}} animate={{scale: 1, transition: {delay: 0.5}}} className='text-center text-white text-8xl font-bold'>Ventas</motion.h1>
        </div>
      </div>
    </>
  )
}