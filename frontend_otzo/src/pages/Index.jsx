import { Card } from "../components/Card";
import { motion } from "framer-motion";

export function Index() {
  return (
    <>
      <div className="bg-gradient-to-l from-red-400 to-orange-500 w-full h-full min-h-[calc(100vh-5rem)] z-0 relative">
        <div className="relative">
          <motion.h1
            initial={{ scale: 0 }}
            animate={{ scale: 1, transition: { delay: 0.5 } }}
            className="text-white font-bold text-7xl lg:text-8xl text-center"
          >
            Otzo
          </motion.h1>
          <motion.h2
            initial={{ opacity: 0 }}
            animate={{ opacity: 1, transition: { delay: 0.7 } }}
            className="text-white font-bold text-xl text-center"
          >
            Módulos del punto de venta
          </motion.h2>
          <motion.img
            initial={{ opacity: 0 }}
            animate={{ opacity: 0.2, transition: { delay: 0.7 } }}
            src="store.png"
            alt=""
            className="absolute right-0 left-0 top-0 bottom-0 h-full m-auto -z-1 opacity-20"
          />
        </div>
        <div className="p-4 gap-4 flex flex-col items-center flex-wrap md:justify-center md:flex-row">
          <Card
            title={"Módulo de inventario"}
            image={"inventario.png"}
            animation_delay={0.8}
          />
          <Card
            title={"Módulo de ventas"}
            image={"carro.png"}
            route={"/ventas"}
            animation_delay={0.9}
          />
          <Card
            title={"Módulo de atención al cliente"}
            image={"customer-service.png"}
            route={"/atencion"}
            animation_delay={1}
          />
          <Card title={"Módulo de reportes y análisis"} animation_delay={1.1} />
          <Card
            title={"Módulo de lógistica y reabastecimiento"}
            animation_delay={1.3}
          />
          <Card
            title={"Módulo de clientes"}
            image={"clientes.png"}
            route={"/clientes"}
            animation_delay={1.4}
          />
          <Card title={"Módulo de administración"}
            image={"administracion.png"}
            route={"/administracion"}
            animation_delay={1.2}
          />
          <Card
            title={"Módulo de fidelización y marketing"}
            image={"fidelizacion.png"}
            route={"/fidelizacion"}
            animation_delay={1.5}
          />
        </div>
      </div>
    </>
  );
}
