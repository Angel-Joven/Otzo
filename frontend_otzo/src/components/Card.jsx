import React from 'react';
import { easeInOut, motion } from 'framer-motion';
import { Link } from 'react-router-dom';

export function Card({ title, image, route }) {
  return (
    <motion.div initial={{opacity: 0, y: 20}} animate={{opacity: 1, y: 0, transition:{delay: 0.8, duration: 0.5, ease: easeInOut}}} className="min-w-72 max-w-72 min-h-48 max-h-48 p-6 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800/50 dark:border-gray-700/50 overflow-hidden">
      <img src={image} alt="" className="h-16 m-auto" />
      <h5 className="mb-2 text-2xl text-center font-bold tracking-tight text-gray-900 dark:text-white overflow-hidden text-ellipsis whitespace-nowrap">
        {title}
      </h5>
      <div className="flex justify-center">
        <Link
          to={route}
          className="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-orange-700 rounded-lg hover:bg-orange-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-orange-600 dark:hover:bg-orange-700 dark:focus:ring-orange-800"
        >
          Ir al módulo
          <svg
            className="rtl:rotate-180 w-3.5 h-3.5 ms-2"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 14 10"
          >
            <path
              stroke="currentColor"
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M1 5h12m0 0L9 1m4 4L9 9"
            />
          </svg>
        </Link>
      </div>
    </motion.div>
  );
}