import React, { useState } from "react";
import { motion } from "framer-motion";
import axios from "axios";

export function Reportes() {
    const [fecha, setFecha] = useState("");
    const [reporteActivo, setReporteActivo] = useState("puntos");
    const [reportePuntos, setReportePuntos] = useState(null);
    const [reporteVentas, setReporteVentas] = useState(null);
    const [reporteRangos, setReporteRangos] = useState(null);
    const [reporteAdministracion, setReporteAdministracion] = useState(null);
    const [reporteQuejas, setReporteQuejas] = useState([]);
    const [reporteInventario, setReporteInventario] = useState([]);

    const [error, setError] = useState("");

    const obtenerReportePuntos = async () => {
        resetReportes();
        if (!fecha) {
            setError("Por favor selecciona una fecha.");
            return;
        }
        try {
            const response = await axios.get(`http://127.0.0.1:5000/api/reportes/reporte-puntos?fecha=${fecha}`);
            setReportePuntos(response.data);
        } catch (error) {
            manejarError("puntos");
        }
    };

    const obtenerReporteVentas = async () => {
        resetReportes();
        if (!fecha) {
            setError("Por favor selecciona una fecha.");
            return;
        }
        try {
            const response = await axios.get(`http://127.0.0.1:5000/api/reportes/reporte-ventas?fecha=${fecha}`);
            setReporteVentas(response.data);
        } catch (error) {
            manejarError("ventas");
        }
    };

    const obtenerReporteRangos = async () => {
        resetReportes();
        try {
            const response = await axios.get("http://127.0.0.1:5000/api/reportes/reporte-rangos");
            setReporteRangos(response.data);
        } catch (error) {
            manejarError("rangos");
        }
    };

    const obtenerReporteAdministracion = async () => {
        resetReportes();
        try {
            const response = await axios.get("http://127.0.0.1:5000/api/reportes/reporte-administracion");
            setReporteAdministracion(response.data);
        } catch (error) {
            manejarError("administración");
        }
    };

    const obtenerReporteQuejas = async () => {
        resetReportes();
        try {
            const response = await axios.get("http://127.0.0.1:5000/api/reportes/reporte-quejas");
            const datos = Array.isArray(response.data) ? response.data : [];
            setReporteQuejas(datos);
        } catch (error) {
            manejarError("quejas");
        }
    };

    const obtenerReporteInventario = async () => {
        resetReportes();
        try {
            const response = await axios.get("http://127.0.0.1:5000/api/reportes/reporte-inventario");
            setReporteInventario(response.data);
        } catch (error) {
            manejarError("inventario");
        }
    };

    const resetReportes = () => {
        setReportePuntos(null);
        setReporteVentas(null);
        setReporteRangos(null);
        setReporteAdministracion(null);
        setReporteQuejas([]);
        setReporteInventario(null);
        setError("");
    };

    const manejarError = (tipo) => {
        console.error(`Error al obtener el reporte de ${tipo}:`, error);
        setError(`Ocurrió un error al obtener el reporte de ${tipo}.`);
    };

    return (
        <div className="bg-gradient-to-r from-gray-400 to-gray-500 w-full h-full min-h-[calc(100vh-5rem)] z-0 relative p-6">
            <motion.h1
                initial={{ scale: 0 }}
                animate={{ scale: 1, transition: { delay: 0.5 } }}
                className="text-center text-white text-6xl font-bold mb-8"
            >
                Reportes y Análisis
            </motion.h1>
            <div className="mb-4">
                <button
                    onClick={() => setReporteActivo("puntos")}
                    className={`px-4 py-2 mr-2 ${reporteActivo === "puntos" ? "bg-blue-500 text-white" : "bg-gray-200"} rounded`}
                >
                    Reporte de Puntos
                </button>
                <button
                    onClick={() => setReporteActivo("ventas")}
                    className={`px-4 py-2 mr-2 ${reporteActivo === "ventas" ? "bg-blue-500 text-white" : "bg-gray-200"} rounded`}
                >
                    Reporte de Ventas
                </button>
                <button
                    onClick={() => setReporteActivo("rangos")}
                    className={`px-4 py-2 mr-2 ${reporteActivo === "rangos" ? "bg-blue-500 text-white" : "bg-gray-200"} rounded`}
                >
                    Reporte de Rangos
                </button>
                <button
                    onClick={() => setReporteActivo("administracion")}
                    className={`px-4 py-2 mr-2 ${reporteActivo === "administracion" ? "bg-blue-500 text-white" : "bg-gray-200"} rounded`}
                >
                    Reporte de Administración
                </button>
                <button
                    onClick={() => setReporteActivo("quejas")}
                    className={`px-4 py-2 mr-2 ${reporteActivo === "quejas" ? "bg-blue-500 text-white" : "bg-gray-200"} rounded`}
                >
                    Reporte de Quejas
                </button>
                <button
                    onClick={() => setReporteActivo("inventario")}
                    className={`px-4 py-2 ${reporteActivo === "inventario" ? "bg-blue-500 text-white" : "bg-gray-200"} rounded`}
                >
                    Reporte de Inventario
                </button>
            </div>

            <div className="bg-white p-6 rounded shadow-lg mb-8">
                {error && <p className="text-red-500 font-bold mb-4">{error}</p>}

                {reporteActivo === "puntos" && (
                    <div>
                        <h2 className="text-2xl font-bold mb-4">Reporte de Puntos</h2>
                        <div className="mb-4">
                            <label htmlFor="fecha" className="block text-gray-700 mb-2">Selecciona una fecha:</label>
                            <input
                                id="fecha"
                                type="date"
                                value={fecha}
                                onChange={(e) => setFecha(e.target.value)}
                                className="p-2 border border-gray-300 rounded w-full"
                            />
                        </div>
                        <button
                            onClick={obtenerReportePuntos}
                            className="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 transition"
                        >
                            Generar Reporte
                        </button>
                        <div className="mt-6">
                            {reportePuntos ? (
                                <table className="table-auto w-full border-collapse border border-gray-400">
                                    <thead>
                                        <tr>
                                            <th className="border px-4 py-2">ID Cliente</th>
                                            <th className="border px-4 py-2">Total Puntos</th>
                                            <th className="border px-4 py-2">Última Actualización</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {reportePuntos.map((item, index) => (
                                            <tr key={index}>
                                                <td className="border px-4 py-2">{item.idcliente_puntos}</td>
                                                <td className="border px-4 py-2">{item.total_puntos}</td>
                                                <td className="border px-4 py-2">{item.ultima_actualizacionPuntos}</td>
                                            </tr>
                                        ))}
                                    </tbody>
                                </table>
                            ) : (
                                <p className="text-gray-500">Genera un reporte para ver los datos.</p>
                            )}
                        </div>
                    </div>
                )}

                {reporteActivo === "ventas" && (
                    <div>
                        <h2 className="text-2xl font-bold mb-4">Reporte de Ventas</h2>
                        <button
                            onClick={obtenerReporteVentas}
                            className="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 transition"
                        >
                            Generar Reporte
                        </button>
                        <div className="mt-6">
                            {reporteVentas ? (
                                <table className="table-auto w-full border-collapse border border-gray-400">
                                    <thead>
                                        <tr>
                                            <th className="border px-4 py-2">ID Venta</th>
                                            <th className="border px-4 py-2">Total</th>
                                            <th className="border px-4 py-2">Fecha</th>
                                            <th className="border px-4 py-2">Cliente</th>
                                            <th className="border px-4 py-2">Empleado</th>
                                            <th className="border px-4 py-2">Detalles</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {reporteVentas.map((venta, index) => (
                                            <tr key={index}>
                                                <td className="border px-4 py-2">{venta.id_venta}</td>
                                                <td className="border px-4 py-2">${venta.total_venta}</td>
                                                <td className="border px-4 py-2">{venta.fecha_venta}</td>
                                                <td className="border px-4 py-2">{venta.cliente}</td>
                                                <td className="border px-4 py-2">{venta.empleado}</td>
                                                <td className="border px-4 py-2">
                                                    <ul>
                                                        {venta.detalles.map((detalle, i) => (
                                                            <li key={i}>
                                                                {detalle.nombre_producto} - ${detalle.precio_unitario} x {detalle.cantidad}
                                                            </li>
                                                        ))}
                                                    </ul>
                                                </td>
                                            </tr>
                                        ))}
                                    </tbody>
                                </table>
                            ) : (
                                <p className="text-gray-500">Genera un reporte para ver los datos.</p>
                            )}
                        </div>
                    </div>
                )}

                {reporteActivo === "rangos" && (
                    <div>
                        <h2 className="text-2xl font-bold mb-4">Reporte de Rangos</h2>
                        <button
                            onClick={obtenerReporteRangos}
                            className="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 transition"
                        >
                            Generar Reporte
                        </button>
                        <div className="mt-6">
                            {reporteRangos ? (
                                <table className="table-auto w-full border-collapse border border-gray-400">
                                    <thead>
                                        <tr>
                                            <th className="border px-4 py-2">Rango</th>
                                            <th className="border px-4 py-2">Total de Personas</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {reporteRangos.map((rango, index) => (
                                            <tr key={index}>
                                                <td className="border px-4 py-2">{rango.nombre_rango}</td>
                                                <td className="border px-4 py-2">{rango.total_personas}</td>
                                            </tr>
                                        ))}
                                    </tbody>
                                </table>
                            ) : (
                                <p className="text-gray-500">Genera un reporte para ver los datos.</p>
                            )}
                        </div>
                    </div>
                )}

                {reporteActivo === "administracion" && (
                    <div>
                        <h2 className="text-2xl font-bold mb-4">Reporte de Administración</h2>
                        <button
                            onClick={obtenerReporteAdministracion}
                            className="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 transition"
                        >
                            Generar Reporte
                        </button>
                        <div className="mt-6">
                            {reporteAdministracion ? (
                                <table className="table-auto w-full border-collapse border border-gray-400">
                                    <thead>
                                        <tr>
                                            <th className="border px-4 py-2">Área</th>
                                            <th className="border px-4 py-2">Total Empleados</th>
                                            <th className="border px-4 py-2">IDs de Empleados</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {reporteAdministracion.map((area, index) => (
                                            <tr key={index}>
                                                <td className="border px-4 py-2">{area.area}</td>
                                                <td className="border px-4 py-2">{area.total_empleados}</td>
                                                <td className="border px-4 py-2">{area.empleados}</td>
                                            </tr>
                                        ))}
                                    </tbody>
                                </table>
                            ) : (
                                <p className="text-gray-500">Genera un reporte para ver los datos.</p>
                            )}
                        </div>
                    </div>
                )}

                {reporteActivo === "quejas" && (
                    <div>
                        <h2 className="text-2xl font-bold mb-4">Reporte de Quejas</h2>
                        <button
                            onClick={obtenerReporteQuejas}
                            className="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 transition"
                        >
                            Generar Reporte
                        </button>
                        <div className="mt-6">
                            {reporteQuejas.length > 0 ? (
                                <table className="table-auto w-full border-collapse border border-gray-400">
                                    <thead>
                                        <tr>
                                            <th className="border px-4 py-2">Categoría</th>
                                            <th className="border px-4 py-2">Cantidad</th>
                                            <th className="border px-4 py-2">IDs de Quejas</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {reporteQuejas.map((queja, index) => (
                                            <tr key={index}>
                                                <td className="border px-4 py-2">{queja.categoria}</td>
                                                <td className="border px-4 py-2">{queja.cantidad}</td>
                                                <td className="border px-4 py-2">{queja.ids_quejas.join(", ")}</td>
                                            </tr>
                                        ))}
                                    </tbody>
                                </table>
                            ) : (
                                <p className="text-gray-500">Genera un reporte para ver los datos.</p>
                            )}
                        </div>
                    </div>
                )}
                    {reporteActivo === "inventario" && (
                        <div>
                            <h2 className="text-2xl font-bold mb-4">Reporte de Inventario</h2>
                            <button
                                onClick={obtenerReporteInventario}
                                className="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 transition"
                            >
                                Generar Reporte
                            </button>
                            <div className="mt-6">
                                {reporteInventario && reporteInventario.length > 0 ? (
                                    <table className="table-auto w-full border-collapse border border-gray-400">
                                        <thead>
                                            <tr>
                                                <th className="border px-4 py-2">ID Producto</th>
                                                <th className="border px-4 py-2">ID Inventario</th>
                                                <th className="border px-4 py-2">Nombre Producto</th>
                                                <th className="border px-4 py-2">Cantidad</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {reporteInventario.map((item, index) => (
                                                <tr key={index}>
                                                    <td className="border px-4 py-2">{item.id_producto}</td>
                                                    <td className="border px-4 py-2">{item.id_inventario}</td>
                                                    <td className="border px-4 py-2">{item.nombre_producto}</td>
                                                    <td className="border px-4 py-2">{item.cantidad_producto}</td>
                                                </tr>
                                            ))}
                                        </tbody>
                                    </table>
                                ) : (
                                    <p className="text-gray-500">No hay datos disponibles. Genera un reporte para ver los datos.</p>
                                )}
                            </div>
                        </div>
                    )}
            </div>
        </div>
    );
}
