import axios from "axios";

export const obtenerAdministradores = () => {
    return axios.get("http://localhost:5000/api/administracion/administradores");
};