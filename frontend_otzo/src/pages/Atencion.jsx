import React from 'react';
import { motion } from 'framer-motion';

export function Atencion() {
   return (
    <>
      <div className='bg-gradient-to-r from-blue-400 to-blue-500 w-full h-full min-h-[calc(100vh-5rem)] z-0 relative'>
        <div>
          <motion.h1 initial={{scale: 0}} animate={{scale: 1, transition: {delay: 0.5}}} className='text-center text-white text-8xl font-bold'>Atención al Cliente</motion.h1>
        </div>
        <div className="grid grid-cols-1 grid-rows-1 gap-x-2.5 md:grid-cols-2">
          <div className="w-full h-full p-4">
            <motion.div
              initial={{ x: 200, opacity: 0 }}
              animate={{ x: 0, opacity: 1, transition: { delay: 0.8 } }}
              className="w-full h-full bg-white/100 rounded-lg p-4 shadow-[0px_4px_6px_0px_rgba(0,_0,_0,_0.1)]"
            >
              <div className="shadow-lg rounded-lg p-4 bg-gray-900">
                <h2 className="font-bold text-white">
                  <i className="align-middle fi fi-sr-document"></i>{" "}
                  Quejas
                </h2>
              </div>
              <div className="h-[calc(25vh)] md:h-[calc(50vh)]"></div>
            </motion.div>
          </div>

          <div className="w-full h-full p-4">
            <motion.div
              initial={{ x: 200, opacity: 0 }}
              animate={{ x: 0, opacity: 1, transition: { delay: 0.8 } }}
              className="w-full h-full bg-white/100 rounded-lg p-4 shadow-[0px_4px_6px_0px_rgba(0,_0,_0,_0.1)]"
            >
              <div className="shadow-lg rounded-lg p-4 bg-gray-900">
                <h2 className="font-bold text-white">
                  <i className="align-middle fi fi-sr-document"></i>{" "}
                  Sugerencias
                </h2>
              </div>
              <div className="h-[calc(25vh)] md:h-[calc(50vh)]"></div>
            </motion.div>
          </div>
        </div>
      </div>
    </>
  )
}