import axios from "axios";

export const getAllSales = () => {
    return axios.get("http://localhost:5000/api/ventas/");
};

export const agregarCompra = (compra) => {
    return axios.post("http://localhost:5000/api/ventas/agregar", compra);
}

export const obtenerHistorialCompraUsuario = (id_cliente) => {
    return axios.post("http://localhost:5000/api/ventas/ver_historial", id_cliente);
}

export const obtenerHistorialDetallesVenta = (ids_ventas) => {
    return axios.post("http://localhost:5000/api/ventas/ver_historial/detalles_ventas", ids_ventas);
}