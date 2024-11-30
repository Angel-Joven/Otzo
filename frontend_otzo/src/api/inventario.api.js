import axios from "axios";

export const obtenerTodosLosProductosAVender = () => {
    return axios.get("http://localhost:5000/api/inventario/vender");
};

export const obtenerTodosLosProductos = () => {
    return axios.get("http://localhost:5000/api/inventario");
};

export const obtenerTodosLosProductosDescontinuados = () => {
    return axios.get("http://localhost:5000/api/inventario/listar_descontinuados");
}

export const crearTipoProducto = (nuevoProducto) => {
    return axios.post("http://localhost:5000/api/inventario/agregar_tipo_producto", nuevoProducto);
}

export const obtenerCategoriasTipoProductos = () => {
    return axios.get("http://localhost:5000/api/inventario/categorias");
}

export const descontinuarTipoProducto = (productoADescontinuar) => {
    return axios.patch("http://localhost:5000/api/inventario/descontinuar_tipo_producto", productoADescontinuar);
}

export const actualizarTipoProducto = (producto) => {
    return axios.put("http://localhost:5000/api/inventario/actualizar_tipo_producto", producto);
}

export const reabastecerProducto = (solicitud) => {
    return axios.post("http://localhost:5000/api/inventario/reabastecer", solicitud);
}

export const obtenerHistorialDeReabastecimientoPorDia = () => {
    return axios.get("http://localhost:5000/api/inventario/historial_reabastecimiento");
}