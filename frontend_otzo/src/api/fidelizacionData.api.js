/*

API para el Modulo de Fidelizacion y Marketing
Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

Temas Especiales de Programacion 2 | 1061

*/

import axios from "axios";

export const FidelizacionData = () => {
    return axios.get("http://localhost:5000/api/fidelizacion/");
};