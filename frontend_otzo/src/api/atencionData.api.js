import axios from "axios";

export const getAllAtenciones = () => {
    return axios.get("http://localhost:5000/api/atencion/");
}