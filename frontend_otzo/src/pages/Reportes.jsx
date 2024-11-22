import React, { useState } from "react";
import { motion } from "framer-motion";
import axios from "axios";

export function Reportes() {
    const [fecha, setFecha] = useState("");
    const [reportePuntos, setReportePuntos] = useState(null);

    const obtenerReportePuntos = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:5000/api/reportes/reporte-puntos?fecha=${fecha}`);
            setReportePuntos(response.data);
        } catch (error) {
            console.error("Error al obtener el reporte de puntos:", error);
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

            {/* Sección de Reporte de Puntos */}
            <div className="bg-white p-6 rounded shadow-lg mb-8">
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
            </div>

            {/* Espacio para futuras secciones */}
            <div className="bg-white p-6 rounded shadow-lg">
                <h2 className="text-2xl font-bold mb-4">Otros Reportes</h2>
                <p className="text-gray-500">Sección en desarrollo para añadir más reportes en el futuro.</p>
            </div>
        </div>
    );
}
