import React from 'react'
import { useState } from 'react';
import { Link } from 'react-router-dom';
import { easeInOut, motion } from 'framer-motion';

export function Navbar() {

  const [isNavbarVisible, setIsNavbarVisible] = useState(false);

  // Función para alternar la visibilidad de la navbar
  const toggleNavbar = () => {
    console.log(isNavbarVisible)
    setIsNavbarVisible(!isNavbarVisible);
  };

  return (
  <motion.nav initial={{opacity: 0}} animate={{opacity: 1, transition: {delay: 0.7}}} className="bg-white border-gray-200 dark:bg-gray-900/50">
    <div className="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
      <motion.a initial={{scale: 0}} animate={{scale: 1, transition: {delay: 0.8}}} href="/" className="flex items-center space-x-3 rtl:space-x-reverse">
          <img src="store.png" className="h-12" alt="" />
          <span className="self-center text-2xl font-bold whitespace-nowrap dark:text-white">Otzo</span>
      </motion.a>
      <button onClick={toggleNavbar} data-collapse-toggle="navbar-default" type="button" className="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600" aria-controls="navbar-default" aria-expanded="false">
          <span className="sr-only">Open main menu</span>
          <svg className="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 17 14">
              <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M1 1h15M1 7h15M1 13h15"/>
          </svg>
      </button>
      <div className={`${isNavbarVisible ? "block" : "hidden"} w-full md:block md:w-auto`} id="navbar-default">
        <ul className="font-medium flex flex-col p-4 md:p-2 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 rtl:space-x-reverse md:mt-0 md:border-0 md:bg-white dark:bg-gray-800/20 md:dark:bg-gray-900/20 dark:border-gray-700/20">
          <li>
            <Link to={"/"} className="block py-2 px-3 text-white bg-blue-700 rounded md:bg-transparent md:text-blue-700 md:p-0 dark:text-white md:dark:text-blue-500" aria-current="page">Inicio</Link>
          </li>
          <li>
            <Link to={"/sales"} className="block py-2 px-3 text-white bg-blue-700 rounded md:bg-transparent md:text-blue-700 md:p-0 dark:text-white md:dark:text-blue-500" aria-current="page">Ventas</Link>
          </li>
          <li>
            <Link to={"/fidelizacion"} className="block py-2 px-3 text-white bg-blue-700 rounded md:bg-transparent md:text-blue-700 md:p-0 dark:text-white md:dark:text-blue-500" aria-current="page">Fidelizacion y Marketing</Link>
          </li>
        </ul>
      </div>
    </div>
  </motion.nav>
  )
}