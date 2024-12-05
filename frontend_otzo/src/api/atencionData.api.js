import axios from "axios";

export const getAllAtenciones = () => {
    return axios.get("http://localhost:5000/api/atencion/");
}

export const obtenerQuejasCliente = (id) => {
    return axios.get(`http://localhost:5000/api/atencion/quejas/${id}`);
}

export const obtenerQuejasPendientes = () => {
    return axios.get("http://localhost:5000/api/atencion/quejas/pendientes");
}

export const crearQueja = (queja) => {
    return axios.post(`http://localhost:5000/api/atencion/quejas/crear`, queja);
}

export const responderQueja = (respuesta) => {
    return axios.patch(`http://localhost:5000/api/atencion/quejas/responder`, respuesta);
}

export const crearSugerencia = (sugerencia) => {
    return axios.post(`http://localhost:5000/api/atencion/sugerencias/crear`, sugerencia);
}