import React from 'react';
import { Navbar } from '../components/Navbar';

export function Sales() {
  return (
    <>
      <div className='bg-gradient-to-r from-lime-400 to-lime-500 w-full h-full overflow-x-hidden fixed -z-10'></div>
      <Navbar />
      <div>
        <h1 className='text-center text-white text-8xl font-bold'>Ventas</h1>
      </div>
    </>
  )
}