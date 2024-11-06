import axios from "axios";

export const FidelizacionData = () => {
    return axios.get("http://localhost:5000/api/fidelizacion/");
};