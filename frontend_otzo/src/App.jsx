import React, { useEffect } from "react";
import { BrowserRouter, Routes, Route, useLocation } from "react-router-dom";
import {
  ObtenerAutenticadorNombre,
  UsarAutenticadorNombre,
} from "./context/Autenticacion"; //Para saber quien se autentico
import { IndexPrincipal } from "./pages/Index"; //Index Principal
import { Ventas } from "./pages/Ventas";
import { Fidelizacion } from "./pages/Fidelizacion";
import { Reportes } from "./pages/Reportes";
import { Clientes } from "./pages/Clientes"; //Clientes - Para solo clientes
import { ClientesAdministracion } from "./pages/ClientesAdministracion"; //Clientes - Para solo administradores
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
import { RutaProtegida } from "./components/RutasProtegidas"; //Proteger rutas para que solo puedan acceder usuarios logeados
import Inventario from "./pages/Inventario";
import "@flaticon/flaticon-uicons/css/all/all.css";

function AppContent() {
  const location = useLocation();
  const { userType } = UsarAutenticadorNombre();

  let navbarToRender;
  //Obtenemos el tipo de usuario que ingreso
  //Si fue un cliente, le carga el navbar de clientes
  //Si fue un administrador, le carga el navbar de administradores
  //Si no fue nadie, entonces le carga el navbar generico
  if (userType === "cliente") {
    navbarToRender = <NavbarClientes />;
  } else if (userType === "administrador") {
    navbarToRender = <NavbarAdministradores />;
  } else {
    navbarToRender = <Navbar />;
  }

  console.log(userType);

  return (
    <>
      {navbarToRender}
      <Routes>
        <Route path="/" element={<IndexPrincipal />} />
        <Route path="/loginClientes" element={<LoginClientes />} />
        <Route
          path="/loginAdministradores"
          element={<LoginAdministradores />}
        />
        <Route
          path="/indexClientes"
          element={
            <RutaProtegida allowedUserTypes={["cliente"]}>
              {" "}
              <IndexClientes />{" "}
            </RutaProtegida>
          }
        />
        <Route
          path="/indexAdministradores"
          element={
            <RutaProtegida allowedUserTypes={["administrador"]}>
              {" "}
              <IndexAdministradores />{" "}
            </RutaProtegida>
          }
        />
        <Route
          path="/ventas"
          element={
            <RutaProtegida allowedUserTypes={["cliente", "administrador"]}>
              {" "}
              <Ventas />{" "}
            </RutaProtegida>
          }
        />
        <Route
          path="/inventario"
          element={
            <RutaProtegida allowedUserTypes={["administrador"]}>
              {" "}
              <Inventario />{" "}
            </RutaProtegida>
          }
        />
        {/* <Route path="/fidelizacion" element={<RutaProtegida allowedUserTypes={['cliente', 'administrador']}> <Fidelizacion /> </RutaProtegida>} /> */}
        <Route
          path="/fidelizacion"
          element={
            <RutaProtegida allowedUserTypes={["administrador"]}>
              {" "}
              <Fidelizacion />{" "}
            </RutaProtegida>
          }
        />
        <Route
          path="/reportes"
          element={
            <RutaProtegida allowedUserTypes={["administrador"]}>
              {" "}
              <Reportes />{" "}
            </RutaProtegida>
          }
        />
        <Route
          path="/atencion"
          element={
            <RutaProtegida allowedUserTypes={["administrador"]}>
              {" "}
              <Atencion />{" "}
            </RutaProtegida>
          }
        />
        <Route
          path="/clientes"
          element={
            <RutaProtegida allowedUserTypes={["cliente"]}>
              {" "}
              <Clientes />{" "}
            </RutaProtegida>
          }
        />
        <Route
          path="/clientesadmin"
          element={
            <RutaProtegida allowedUserTypes={["administrador"]}>
              {" "}
              <ClientesAdministracion />{" "}
            </RutaProtegida>
          }
        />
        <Route
          path="/administracion"
          element={
            <RutaProtegida allowedUserTypes={["administrador"]}>
              {" "}
              <Administracion />{" "}
            </RutaProtegida>
          }
        />
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
