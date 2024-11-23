import React, { useState } from "react";
import { motion } from "framer-motion";
import axios from "axios";

export function Reportes() {
    const [fecha, setFecha] = useState(""); // Fecha seleccionada por el usuario
    const [reportePuntos, setReportePuntos] = useState(null); // Estado para el reporte de puntos
    const [reporteVentas, setReporteVentas] = useState(null); // Estado para el reporte de ventas
    const [reporteRangos, setReporteRangos] = useState(null); // Estado para el reporte de rangos
    const [error, setError] = useState(""); // Estado para manejar errores
    const [reporteActivo, setReporteActivo] = useState("puntos"); // Estado para controlar el tipo de reporte

    // Obtener el reporte de puntos
    const obtenerReportePuntos = async () => {
        setReporteVentas(null);
        setReporteRangos(null);
        try {
            const response = await axios.get(`http://127.0.0.1:5000/api/reportes/reporte-puntos?fecha=${fecha}`);
            setReportePuntos(response.data);
        } catch (error) {
            console.error("Error al obtener el reporte de puntos:", error);
            setError("Ocurrió un error al obtener el reporte de puntos.");
        }
    };

    // Obtener el reporte de ventas
    const obtenerReporteVentas = async () => {
        setReportePuntos(null);
        setReporteRangos(null);
        setError("");

        if (!fecha) {
            setError("Por favor selecciona una fecha.");
            return;
        }

        try {
            const response = await axios.get(`http://127.0.0.1:5000/api/reportes/reporte-ventas?fecha=${fecha}`);
            setReporteVentas(response.data);
        } catch (error) {
            console.error("Error al obtener el reporte de ventas:", error);
            setError("Ocurrió un error al obtener el reporte de ventas.");
        }
    };

    // Obtener el reporte de rangos
    const obtenerReporteRangos = async () => {
        setReportePuntos(null);
        setReporteVentas(null);
        setError("");
        try {
            const response = await axios.get("http://127.0.0.1:5000/api/reportes/reporte-rangos");
            setReporteRangos(response.data);
        } catch (error) {
            console.error("Error al obtener el reporte de rangos:", error);
            setError("Ocurrió un error al obtener el reporte de rangos.");
        }
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

            {/* Botones para alternar entre reportes */}
            <div className="mb-4">
                <button
                    onClick={() => {
                        setReporteActivo("puntos");
                        setReportePuntos(null);
                        setReporteVentas(null);
                        setReporteRangos(null);
                    }}
                    className={`px-4 py-2 mr-2 ${reporteActivo === "puntos" ? "bg-blue-500 text-white" : "bg-gray-200"} rounded`}
                >
                    Reporte de Puntos
                </button>
                <button
                    onClick={() => {
                        setReporteActivo("ventas");
                        setReportePuntos(null);
                        setReporteVentas(null);
                        setReporteRangos(null);
                    }}
                    className={`px-4 py-2 mr-2 ${reporteActivo === "ventas" ? "bg-blue-500 text-white" : "bg-gray-200"} rounded`}
                >
                    Reporte de Ventas
                </button>
                <button
                    onClick={() => {
                        setReporteActivo("rangos");
                        setReportePuntos(null);
                        setReporteVentas(null);
                        setReporteRangos(null);
                    }}
                    className={`px-4 py-2 ${reporteActivo === "rangos" ? "bg-blue-500 text-white" : "bg-gray-200"} rounded`}
                >
                    Reporte de Rangos
                </button>
            </div>

            {/* Sección de Reporte Activo */}
            <div className="bg-white p-6 rounded shadow-lg mb-8">
                {reporteActivo === "puntos" ? (
                    <>
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
                        {/* Tabla de resultados */}
                        <div className="mt-6">
                            {reportePuntos ? (
                                Array.isArray(reportePuntos) ? (
                                    <table className="table-auto w-full border-collapse border border-gray-400">
                                        <thead>
                                            <tr>
                                                <th className="border border-gray-400 px-4 py-2">ID Cliente</th>
                                                <th className="border border-gray-400 px-4 py-2">Total Puntos</th>
                                                <th className="border border-gray-400 px-4 py-2">Última Actualización</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {reportePuntos.map((item, index) => (
                                                <tr key={index} className="hover:bg-gray-100">
                                                    <td className="border border-gray-400 px-4 py-2">{item.idcliente_puntos}</td>
                                                    <td className="border border-gray-400 px-4 py-2">{item.total_puntos}</td>
                                                    <td className="border border-gray-400 px-4 py-2">{item.ultima_actualizacionPuntos}</td>
                                                </tr>
                                            ))}
                                        </tbody>
                                    </table>
                                ) : (
                                    <div className="text-red-500 font-semibold mt-4">{reportePuntos.mensaje}</div>
                                )
                            ) : (
                                <p className="text-gray-500">Genera un reporte para ver los datos.</p>
                            )}
                        </div>
                    </>
                ) : reporteActivo === "ventas" ? (
                    <>
                        <h2 className="text-2xl font-bold mb-4">Reporte de Ventas</h2>
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
                            onClick={obtenerReporteVentas}
                            className="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 transition"
                        >
                            Generar Reporte
                        </button>

                        {/* Tabla de resultados */}
                        <div className="mt-6">
                            {reporteVentas ? (
                                Array.isArray(reporteVentas) ? (
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
                                                <tr key={index} className="hover:bg-gray-100">
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
                                    <div className="text-red-500 font-semibold mt-4">{reporteVentas.mensaje}</div>
                                )
                            ) : (
                                <p className="text-gray-500">Genera un reporte para ver los datos.</p>
                            )}
                        </div>
                    </>
                ) : (
                    <>
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
                    </>
                )}
            </div>
        </div>
    );
}