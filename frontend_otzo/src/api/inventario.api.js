import axios from "axios";

export const obtenerTodosLosProductos = () => {
    return axios.get("http://localhost:5000/api/inventario");
};

export const obtenerTodosLosProductosDescontinuados = () => {
    return axios.get("http://localhost:5000/api/inventario/listar_descontinuados");
}

export const crearTipoProducto = (nuevoProducto) => {
    return axios.post("http://localhost:5000/api/inventario/agregar_tipo_producto", nuevoProducto);
}