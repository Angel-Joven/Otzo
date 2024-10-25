import React from 'react';
import { motion } from 'framer-motion';

export function Sales() {
  return (
    <>
      <div className='bg-gradient-to-r from-lime-400 to-lime-500 w-full h-full min-h-[calc(100vh-5rem)] z-0 relative'>
        <div>
          <motion.h1 initial={{scale: 0}} animate={{scale: 1, transition: {delay: 0.5}}} className='text-center text-white text-8xl font-bold'>Ventas</motion.h1>
        </div>
        <div className='grid grid-cols-1 grid-rows-1 gap-x-2.5 md:grid-cols-2'>
          <div className='w-full h-full p-4'>
            <div className='w-full h-full bg-white rounded-lg p-4'>
              <div className='shadow-lg rounded-lg p-4 bg-rose-400'>
                <h2 className='font-bold'>Productos</h2>
              </div>
              <div className='h-[calc(20vh)] md:h-[calc(50vh)]'>

              </div>
            </div>
          </div>
          
          <div className='w-full h-full p-4'>
            <div className='w-full h-full bg-white rounded-lg p-4'>
              <div className='shadow-lg rounded-lg p-4 bg-yellow-500'>
                <h2 className='font-bold'>Carrito</h2>
              </div>
              <div className='h-[calc(20vh)] md:h-[calc(50vh)]'>

              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  )
}