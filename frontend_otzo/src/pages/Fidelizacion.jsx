import React from 'react';
import { motion } from 'framer-motion';

export function Fidelizacion() {
  return (
    <>
      <div className='bg-gradient-to-r from-purple-400 to-purple-500 w-full h-full overflow-x-hidden fixed -z-10'></div>
      <div>
        <motion.h1 initial={{scale: 0}} animate={{scale: 1, transition: {delay: 0.5}}} className='text-center text-white text-8xl font-bold'>Fidelizacion y Marketing</motion.h1>
      </div>
    </>
  )
}