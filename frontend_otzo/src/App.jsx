import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Index } from "./pages/Index";
import { Ventas } from "./pages/Ventas";
import { Fidelizacion } from "./pages/Fidelizacion";
import { Atencion } from "./pages/Atencion";
import "./App.css";
import { Navbar } from "./components/Navbar";

function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<Index />} />
        <Route path="/ventas" element={<Ventas />} />
        <Route path="/fidelizacion" element={<Fidelizacion />} />
        <Route path="/atencion" element={<Atencion />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
