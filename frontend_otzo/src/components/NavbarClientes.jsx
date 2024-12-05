/*

Navbar para el Modulo de Clientes
Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

Temas Especiales de Programacion 2 | 1061

*/

import React, { useState } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import { UsarAutenticadorNombre } from "../context/Autenticacion";

export function NavbarClientes() {
  const { logout } = UsarAutenticadorNombre();
  const navigate = useNavigate();
  const location = useLocation();

  const handleLogout = () => {
    logout();
    navigate("/");
  };

  const [isNavbarVisible, setIsNavbarVisible] = useState(false);

  return (
    <motion.nav className="bg-gray-900 h-20">
      <div className="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
        <motion.a
          initial={{ scale: 0 }}
          animate={{ scale: 1, transition: { delay: 0.8 } }}
          href="/"
          className="flex items-center space-x-3 rtl:space-x-reverse"
        >
          <img src="store.png" className="h-12" alt="" />
          <span className="self-center text-2xl font-bold whitespace-nowrap text-white">
            Otzo
          </span>
        </motion.a>
        <button
          onClick={() => setIsNavbarVisible(!isNavbarVisible)}
          data-collapse-toggle="navbar-default"
          type="button"
          className="inline-flex items-center p-2 w-10 h-10 justify-center text-sm rounded-lg md:hidden focus:outline-none focus:ring-2 text-gray-400 hover:bg-gray-700 focus:ring-gray-600"
          aria-controls="navbar-default"
          aria-expanded={isNavbarVisible}
        >
          <span className="sr-only">Open main menu</span>
          <svg
            className="w-5 h-5"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 17 14"
          >
            <path
              stroke="currentColor"
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M1 1h15M1 7h15M1 13h15"
            />
          </svg>
        </button>
        <div
          className={`${
            isNavbarVisible ? "block" : "hidden"
          } w-full md:block md:w-auto zIndex`}
          id="navbar-default"
        >
          <ul className="font-medium flex flex-col p-4 md:p-2 mt-4 border rounded-lg md:flex-row md:space-x-8 rtl:space-x-reverse md:mt-0 md:border-0 bg-gray-800 md:bg-gray-900 border-gray-700 w-full">
            <li>
              <Link
                to={"/indexClientes"}
                className={`block py-2 px-3 mb-2 ${
                  location.pathname === "/indexClientes"
                    ? "text-black font-bold md:text-blue-500 underline"
                    : "text-white"
                } bg-orange-600 rounded md:bg-transparent md:p-0`}
                aria-current="page"
              >
                Inicio
              </Link>
            </li>
            <li>
              <Link
                to={"/clientes"}
                className={`block py-2 px-3 mb-2 ${
                  location.pathname === "/clientes"
                    ? "text-black font-bold md:text-blue-500 underline"
                    : "text-white"
                } bg-yellow-500 rounded md:bg-transparent md:p-0`}
                aria-current="page"
              >
                Clientes
              </Link>
            </li>
            <li>
              <Link
                to={"/ventas"}
                className={`block py-2 px-3 mb-2 ${
                  location.pathname === "/ventas"
                    ? "text-black font-bold md:text-blue-500 underline"
                    : "text-white"
                } bg-green-600 rounded md:bg-transparent md:p-0`}
                aria-current="page"
              >
                Ventas
              </Link>
            </li>
            <li>
              <Link
                to={"/atencioncliente"}
                className={`block py-2 px-3 mb-2 ${
                  location.pathname === "/atencioncliente"
                    ? "text-black font-bold md:text-blue-500 underline"
                    : "text-white"
                } bg-green-600 rounded md:bg-transparent md:p-0`}
                aria-current="page"
              >
                Atención al cliente
              </Link>
            </li>
            <li>
              <button
                onClick={handleLogout}
                className="bg-red-500 text-white px-4 py-2 rounded"
              >
                Cerrar Sesion
              </button>
            </li>
          </ul>
        </div>
      </div>
    </motion.nav>
  );
}
