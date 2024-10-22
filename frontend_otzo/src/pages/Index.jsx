import { Navbar } from "../components/Navbar";
import { Card } from "../components/Card";

export function Index() {
  return(
    <>
      <div className="bg-gradient-to-l from-red-400 to-orange-500 w-full h-full overflow-x-hidden fixed -z-10"></div>
      
      <Navbar />
      <div className="relative">
        <h1 className="text-white font-bold text-7xl lg:text-8xl text-center">Otzo</h1>
        <h2 className="text-white font-bold text-xl text-center">Módulos del punto de venta</h2>
        <img src="store.png" alt="" className="absolute right-0 left-0 top-0 bottom-0 h-full m-auto -z-10 opacity-20" />
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