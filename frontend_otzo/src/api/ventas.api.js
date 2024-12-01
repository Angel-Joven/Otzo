import axios from "axios";

export const getAllSales = () => {
    return axios.get("http://localhost:5000/api/ventas/");
};

export const agregarCompra = (compra) => {
    return axios.post("http://localhost:5000/api/ventas/agregar", compra);
}