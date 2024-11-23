import axios from "axios";

export const obtenerTodosLosProductos = () => {
    return axios.get("http://localhost:5000/api/inventario");
};