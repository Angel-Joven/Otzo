import React, { useEffect } from 'react';
import { BrowserRouter, Routes, Route, useLocation } from "react-router-dom";
import { ObtenerAutenticadorNombre, UsarAutenticadorNombre } from "./context/Autenticacion"; //Para saber quien se autentico
import { IndexPrincipal } from "./pages/Index"; //Index Principal
import { Ventas } from "./pages/Ventas";
import { Fidelizacion } from "./pages/Fidelizacion";
import { Reportes } from "./pages/Reportes";
import { Clientes } from "./pages/Clientes";
import { Administracion } from "./pages/Administracion";
import { Atencion } from "./pages/Atencion";
import { LoginClientes } from "./pages/loginClientes"; //Login Clientes
import { LoginAdministradores } from "./pages/loginAdministradores"; //Login Administradores
import { IndexClientes } from "./pages/IndexClientes"; //Index Para Clientes
import { IndexAdministradores } from "./pages/IndexAdministradores"; //Index Para Administradores
import "./App.css";
import { Navbar } from "./components/Navbar"; //Navbar general
import { NavbarClientes } from "./components/NavbarClientes"; //Navbar para clientes
import { NavbarAdministradores } from "./components/NavbarAdministradores"; //Navbar para los administradores
import { RutaProtegida } from './components/RutasProtegidas';

function AppContent() {
  const location = useLocation();
  const { userType } = UsarAutenticadorNombre();

  let navbarToRender;
  //Obtenemos el tipo de usuario que ingreso
  //Si fue un cliente, le carga el navbar de clientes
  //Si fue un administrador, le carga el navbar de administradores
  //Si no fue nadie, entonces le carga el navbar generico
  if (userType === 'cliente') {
    navbarToRender = <NavbarClientes />;
  } else if (userType === 'administrador') {
    navbarToRender = <NavbarAdministradores />;
  } else {
    navbarToRender = <Navbar />;
  }

  console.log(userType)

  return (
    <>
      {navbarToRender}
      <Routes>
        <Route path="/" element={<IndexPrincipal />} />
        <Route path="/loginClientes" element={<LoginClientes />} />
        <Route path="/loginAdministradores" element={<LoginAdministradores />} />
        <Route path="/indexClientes" element={<RutaProtegida> <IndexClientes /> </RutaProtegida>} />
        <Route path="/indexAdministradores" element={<RutaProtegida> <IndexAdministradores /> </RutaProtegida>} />
        <Route path="/ventas" element={<RutaProtegida> <Ventas /> </RutaProtegida>} />
        <Route path="/fidelizacion" element={<RutaProtegida> <Fidelizacion /> </RutaProtegida>} />
        <Route path="/reportes" element={<RutaProtegida> <Reportes /> </RutaProtegida>} />
        <Route path="/atencion" element={<RutaProtegida> <Atencion /> </RutaProtegida>} />
        <Route path="/clientes" element={<RutaProtegida> <Clientes /> </RutaProtegida>} />
        <Route path="/administracion" element={<RutaProtegida> <Administracion /> </RutaProtegida>} />
      </Routes>
    </>
  );
}

function App() {
  return (
    <ObtenerAutenticadorNombre>
      <BrowserRouter>
        <AppContent />
      </BrowserRouter>
    </ObtenerAutenticadorNombre>
  );
}

export default App;
