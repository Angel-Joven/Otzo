import { Navbar } from "../components/Navbar";
import { Card } from "../components/Card";
import { easeInOut, motion } from 'framer-motion';

export function Index() {
  return(
    <>
      <div className="bg-gradient-to-l from-red-400 to-orange-500 w-full h-full overflow-x-hidden fixed -z-10"></div>
      <Navbar />
      <div className="relative">
        <motion.h1 initial={{scale: 0}} animate={{scale: 1, transition: {delay: 0.5}}} className="text-white font-bold text-7xl lg:text-8xl text-center">Otzo</motion.h1>
        <motion.h2 initial={{opacity: 0}} animate={{opacity: 1, transition: {delay: 0.7}}} className="text-white font-bold text-xl text-center">Módulos del punto de venta</motion.h2>
        <motion.img initial={{opacity: 0}} animate={{opacity: 0.2, transition: {delay: 0.7}}}  src="store.png" alt="" className="absolute right-0 left-0 top-0 bottom-0 h-full m-auto -z-10 opacity-20" />
      </div>
      <div className="p-4 gap-4 flex flex-col items-center flex-wrap md:justify-center md:flex-row">
        <Card title={"Módulo de inventario"} image={"inventario.png"} />
        <Card title={"Módulo de ventas"} image={"carro.png"} route={"/sales"}/>
        <Card title={"Módulo de atención al cliente"} />
        <Card title={"Módulo de reportes y análisis"} />
        <Card title={"Módulo de administración"} />
        <Card title={"Módulo de lógistica y reabastecimiento"} />
        <Card title={"Módulo de control de calidad y auditoria"} />
        <Card title={"Módulo de fidelización y marketing"} />
      </div>
    </>
  );
}