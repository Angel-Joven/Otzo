import React from 'react';
import { Navbar } from '../components/Navbar';
import { easeInOut, motion } from 'framer-motion';

export function Sales() {
  return (
    <>
      <div className='bg-gradient-to-r from-lime-400 to-lime-500 w-full h-full overflow-x-hidden fixed -z-10'></div>
      <div>
        <motion.h1 initial={{scale: 0}} animate={{scale: 1, transition: {delay: 0.5}}} className='text-center text-white text-8xl font-bold'>Ventas</motion.h1>
      </div>
    </>
  )
}