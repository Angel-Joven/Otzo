import React from 'react';
import { motion } from 'framer-motion';

export function Sales() {
  return (
    <>
      <div className='bg-gradient-to-t from-lime-600 to-lime-500 w-full h-full min-h-[calc(100vh-5rem)] z-0 relative'>
        <div>
          <motion.h1 initial={{scale: 0}} animate={{scale: 1, transition: {delay: 0.5}}} className='text-center text-white text-6xl md:text-8xl font-bold'>Ventas</motion.h1>
        </div>
        <div className='grid grid-cols-1 grid-rows-1 gap-x-2.5 md:grid-cols-2'>
          <div className='w-full h-full p-4'>
            <motion.div initial={{x: -200, opacity: 0}} animate={{x: 0, opacity: 1, transition: {delay: 0.8}}} className='w-full h-full bg-white/80 rounded-lg p-4'>
              <div className='shadow-lg rounded-lg p-4 bg-rose-400'>
                <h2 className='font-bold'>Productos</h2>
              </div>
              <div className='h-[calc(20vh)] md:h-[calc(50vh)]'>

              </div>
            </motion.div>
          </div>
          
          <div className='w-full h-full p-4'>
            <motion.div initial={{x: 200, opacity: 0}} animate={{x: 0, opacity: 1, transition: {delay: 0.8}}} className='w-full h-full bg-white/80 rounded-lg p-4'>
              <div className='shadow-lg rounded-lg p-4 bg-yellow-500'>
                <h2 className='font-bold'>Carrito</h2>
              </div>
              <div className='h-[calc(20vh)] md:h-[calc(50vh)]'>

              </div>
            </motion.div>
          </div>
        </div>
        <div className='p-4 flex justify-center md:justify-end'>
          <div className='bg-white p-3 w-full md:w-auto md:p-4 rounded-lg'>
            <h3 className='font-bold text-3xl mb-4'><span className='text-red-400'>Total: </span>$250 MXN</h3>
            <button className='bg-green-500 p-3 rounded-xl w-full text-white font-bold'>Pagar ahora</button>
          </div>
        </div>
      </div>
    </>
  )
}