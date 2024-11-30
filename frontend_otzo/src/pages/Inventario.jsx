import {
  obtenerTodosLosProductos,
  crearTipoProducto,
  obtenerTodosLosProductosDescontinuados,
  obtenerCategoriasTipoProductos,
  actualizarTipoProducto,
  reabastecerProducto,
  obtenerHistorialDeReabastecimientoPorDia,
} from "../api/inventario.api";
import React, { useState, useEffect } from "react";
import ProductCard from "../components/inventario/ProductCard";
import { useLocation } from "react-router-dom";
import DataTable from "react-data-table-component";

function Inventario() {
  const [data, setData] = useState();
  const [isLoading, setIsLoading] = useState(true);
  const [isDialogAddTypeProductOpen, setIsDialogOpen] = useState(false); // Controla el diálogo
  const location = useLocation(); // Detecta cambios en la ruta
  const [recargarProductos, setRecargarProductos] = useState(false);

  const [descontinuados, setDescontinuados] = useState(false);
  const [productosDescontinuados, setProductosDescontinuados] = useState();

  const [categorias, setCategorias] = useState([]);

  const [isDialogEditTypeProductOpen, setisDialogEditTypeProductOpen] =
    useState(false);

  const [productoAEditar, setProductoAEditar] = useState({});

  const [isDialogReplenishOpen, setIsDialogReplenishOpen] = useState(false);

  const [productoAReabastecer, setProductoAReabastecer] = useState({});

  useEffect(() => {
    obtenerTodosLosProductos()
      .then((res) => {
        console.log(res.data);
        setData(res.data);
        setIsLoading(false);
      })
      .catch((error) => {
        console.error("Error al obtener los productos:", error);
        setIsLoading(false);
      });

    obtenerTodosLosProductosDescontinuados()
      .then((res) => {
        console.log(res.data);
        setProductosDescontinuados(res.data);
      })
      .catch((error) => {
        console.error("Error al obtener los productos descontinuados:", error);
      });
  }, [recargarProductos]);

  useEffect(() => {
    obtenerTodosLosProductosDescontinuados()
      .then((res) => {
        console.log(res.data);
        setProductosDescontinuados(res.data);
      })
      .catch((error) => {
        console.error("Error al obtener los productos descontinuados:", error);
      });
  }, [descontinuados]);

  useEffect(() => {
    obtenerCategoriasTipoProductos()
      .then((res) => {
        console.log(res.data);
        setCategorias(res.data);
      })
      .catch((error) => {
        console.error("Error al obtener los productos descontinuados:", error);
      });
  }, [isDialogAddTypeProductOpen]);

  // Cierra el diálogo al cambiar de página
  useEffect(() => {
    setIsDialogOpen(false);
  }, [location]);

  const changeProductsToDiscontinued = () => {
    setDescontinuados(!descontinuados);
  };

  //ADD PRODUCTS
  const handleModalAddNewTipeProductClick = (e) => {
    // Cierra el diálogo si se hace clic fuera del recuadro
    if (e.target.id === "modalAddProduct") {
      setIsDialogOpen(false);
    }
  };

  const handleFormModalAddNewTipeProduct = async (e) => {
    e.preventDefault();

    const nuevoProducto = {
      nombre_tipo_producto: e.target.add_product_title_input.value,
      imagen_tipo_producto: e.target.add_product_image_input.value,
      categoria_tipo_producto: e.target.add_product_category_input.value,
      descripcion_tipo_producto: e.target.add_product_description_input.value,
      precio_unitario: e.target.add_price_unit_input.value,
      cantidad_maxima_producto: e.target.add_max_quantity_input.value,
    };

    try {
      crearTipoProducto(nuevoProducto).then((res) => {
        console.log("Producto agregado con éxito.");
        setIsDialogOpen(false);
        setRecargarProductos(!recargarProductos);
      });
    } catch (error) {
      console.error("Error al agregar el producto:", error);
    }
  };

  //EDIT PRODUCTS

  const handleModalEditTypeProduct = (e) => {
    // Cierra el diálogo si se hace clic fuera del recuadro
    if (e.target.id === "modalEditProduct") {
      setisDialogEditTypeProductOpen(false);
    }
  };

  const handleFormModalEditTypeProduct = async (e) => {
    e.preventDefault();

    const productoEditado = {
      nombre_tipo_producto: e.target.edit_product_title_input.value,
      imagen_tipo_producto: e.target.edit_product_image_input.value,
      categoria_tipo_producto: e.target.edit_product_category_input.value,
      descripcion_tipo_producto: e.target.edit_product_description_input.value,
      precio_unitario: e.target.edit_price_unit_input.value,
      cantidad_tipo_producto: e.target.edit_amount_product_input.value,
      descontinuado: !e.target.edit_enable_input.checked,
      cantidad_maxima_producto: e.target.edit_max_quantity_input.value,
      id_inventario: e.target.id_inventario.value,
    };

    console.log(productoEditado);

    try {
      actualizarTipoProducto(productoEditado).then((res) => {
        console.log("Producto actualizado con éxito.");
        setisDialogEditTypeProductOpen(false);
        setRecargarProductos(!recargarProductos);
      });
    } catch (error) {
      console.error("Error al actualizar el producto:", error);
    }
  };

  //REABASTECER

  const handleModalReplenishProduct = (e) => {
    // Cierra el diálogo si se hace clic fuera del recuadro
    if (e.target.id === "modalReplenishProduct") {
      setIsDialogReplenishOpen(false);
    }
  };

  const handleFormModalReplenishProduct = async (e) => {
    e.preventDefault();

    const solicitud = {
      id_inventario: e.target.replenish_product_id_input.value,
      cantidad: e.target.replenish_product_quantity_input.value,
    };

    console.log(solicitud);

    try {
      reabastecerProducto(solicitud).then((res) => {
        console.log("Producto reabastecido con éxito.");
        setIsDialogReplenishOpen(false);
        setRecargarProductos(!recargarProductos);
      });
    } catch (error) {
      console.error("Error al reabastecer el producto:", error);
    }
  };

  const [isViewReplenishOpen, setIsViewReplenishOpen] = useState(false);
  const [replenishHistory, setReplenishHistory] = useState([]);

  const handleModalViewReplenish = (e) => {
    // Cierra el diálogo si se hace clic fuera del recuadro
    if (e.target.id === "modalViewReplenish") {
      setIsViewReplenishOpen(false);
    }
  };

  const viewReplenish = () => {
    obtenerHistorialDeReabastecimientoPorDia().then((res) => {
      setReplenishHistory(res.data);
    });
    setIsViewReplenishOpen(true);
  };

  const columns = [
    {
      name: "ID Inventario",
      selector: (row) => row.id_inventario,
    },
    {
      name: "Fecha reabastecimiento",
      selector: (row) => row.dia_reabastecimiento,
    },
    {
      name: "Cantidad de productos",
      selector: (row) => row.cantidad_productos,
    },
  ];

  return (
    <>
      <div className="bg-gradient-to-r from-slate-600 to-gray-500 w-full h-full min-h-[calc(100vh-5rem)] z-0 relative">
        {/* Diálogos */}
        {isDialogAddTypeProductOpen && (
          <dialog
            id="modalAddProduct"
            className="absolute top-0 right-0 left-0 bottom-0 z-10 w-full h-full bg-slate-900/80 flex justify-center items-center"
            onClick={handleModalAddNewTipeProductClick}
          >
            <div
              className="min-h-[50%] min-w-[50%] bg-white rounded-xl p-4 flex flex-col gap-4"
              onClick={(e) => e.stopPropagation()} // Evita cerrar al hacer clic dentro del recuadro
            >
              <p className="font-bold text-xl">Agrega un producto:</p>
              <form onSubmit={handleFormModalAddNewTipeProduct}>
                <label htmlFor="add_product_title_input" className="block">
                  Titulo del producto:
                </label>
                <input
                  id="add_product_title_input"
                  type="text"
                  placeholder="Escribe aquí..."
                  className="w-full max-w-md p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700 placeholder-gray-400"
                />
                <label htmlFor="add_product_image_input" className="block">
                  Imagen del producto:
                </label>
                <input
                  id="add_product_image_input"
                  type="text"
                  placeholder="Escribe aquí..."
                  className="w-full max-w-md p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700 placeholder-gray-400"
                />
                <label htmlFor="add_product_category_input" className="block">
                  Categoria del producto:
                </label>
                <select
                  name="add_product_category_input"
                  id="category"
                  className="w-full max-w-md p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700 placeholder-gray-400"
                >
                  {categorias.map((categoria, index) => {
                    return (
                      <option value={categoria.categoria_producto} key={index}>
                        {categoria.categoria_producto}
                      </option>
                    );
                  })}
                </select>
                <label
                  htmlFor="add_product_description_input"
                  className="block"
                >
                  Descripción del producto:
                </label>
                <textarea
                  id="add_product_description_input"
                  type="text"
                  placeholder="Escribe aquí..."
                  className="w-full max-w-md p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700 placeholder-gray-400"
                ></textarea>
                <label htmlFor="add_price_unit_input" className="block">
                  Precio del producto:
                </label>
                <input
                  id="add_price_unit_input"
                  type="number"
                  step="0.01"
                  placeholder="Introduce tu precio..."
                  className="w-full max-w-md p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700 placeholder-gray-400"
                />
                <label htmlFor="add_max_quantity_input" className="block">
                  Cantidad máxima del producto:
                </label>
                <input
                  id="add_max_quantity_input"
                  type="number"
                  step="1"
                  placeholder="Introduce la cantidad máxima para reabastecer"
                  className="w-full max-w-md p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700 placeholder-gray-400"
                />
                <input
                  type="submit"
                  value="Crear producto"
                  className="block bg-blue-500 rounded-lg p-2 text-white font-bold my-2 cursor-pointer"
                />
              </form>
            </div>
          </dialog>
        )}

        {isDialogEditTypeProductOpen && (
          <dialog
            id="modalEditProduct"
            className="absolute top-0 right-0 left-0 bottom-0 z-10 w-full h-full bg-slate-900/80 flex justify-center items-center"
            onClick={handleModalEditTypeProduct}
          >
            <div
              className="min-h-[50%] min-w-[50%] bg-white rounded-xl p-4 flex flex-col gap-4"
              onClick={(e) => e.stopPropagation()} // Evita cerrar al hacer clic dentro del recuadro
            >
              <p className="font-bold text-xl">Edita un producto:</p>
              <form onSubmit={handleFormModalEditTypeProduct}>
                <label htmlFor="edit_product_title_input" className="block">
                  Titulo del producto:
                </label>
                <input
                  defaultValue={productoAEditar.nombre_tipo_producto}
                  id="edit_product_title_input"
                  type="text"
                  placeholder="Escribe aquí..."
                  className="w-full max-w-md p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700 placeholder-gray-400"
                />
                <label htmlFor="edit_product_image_input" className="block">
                  Imagen del producto:
                </label>
                <input
                  defaultValue={productoAEditar.imagen_tipo_producto}
                  id="edit_product_image_input"
                  type="text"
                  placeholder="Escribe aquí..."
                  className="w-full max-w-md p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700 placeholder-gray-400"
                />
                <label htmlFor="edit_product_category_input" className="block">
                  Categoria del producto:
                </label>
                <select
                  defaultValue={productoAEditar.categoria_tipo_producto}
                  name="edit_product_category_input"
                  id="category"
                  className="w-full max-w-md p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700 placeholder-gray-400"
                >
                  {categorias.map((categoria, index) => {
                    return (
                      <option value={categoria.categoria_producto} key={index}>
                        {categoria.categoria_producto}
                      </option>
                    );
                  })}
                </select>
                <label
                  htmlFor="edit_product_description_input"
                  className="block"
                >
                  Descripción del producto:
                </label>
                <textarea
                  defaultValue={productoAEditar.descripcion_tipo_producto}
                  id="edit_product_description_input"
                  type="text"
                  placeholder="Escribe aquí..."
                  className="w-full max-w-md p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700 placeholder-gray-400"
                ></textarea>
                <label htmlFor="edit_price_unit_input" className="block">
                  Precio del producto:
                </label>
                <input
                  defaultValue={productoAEditar.precio_unitario}
                  id="edit_price_unit_input"
                  type="number"
                  step="0.01"
                  placeholder="Introduce tu precio..."
                  className="w-full max-w-md p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700 placeholder-gray-400"
                />
                <label htmlFor="edit_amount_product_input" className="block">
                  Cantidad del producto:
                </label>
                <input
                  defaultValue={productoAEditar.cantidad_tipo_producto}
                  id="edit_amount_product_input"
                  type="number"
                  step="1"
                  placeholder="Introduce tu precio..."
                  className="w-full max-w-md p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700 placeholder-gray-400"
                />
                <label htmlFor="edit_max_quantity_input" className="block">
                  Cantidad máxima del producto:
                </label>
                <input
                  defaultValue={productoAEditar.cantidad_maxima_producto}
                  id="edit_max_quantity_input"
                  type="number"
                  step="1"
                  placeholder="Introduce la cantidad máxima del producto a reabastecer..."
                  className="w-full max-w-md p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700 placeholder-gray-400"
                />
                <label htmlFor="edit_enable_input" className="hidden">
                  Activo:
                </label>
                <input
                  type="checkbox"
                  id="edit_enable_input"
                  defaultChecked={!productoAEditar.descontinuado}
                  className="hidden"
                ></input>
                <input
                  type="text"
                  className="hidden"
                  defaultValue={productoAEditar.id_inventario}
                  id="id_inventario"
                />
                <input
                  type="submit"
                  value="Editar producto"
                  className="block bg-blue-500 rounded-lg p-2 text-white font-bold my-2 cursor-pointer"
                />
              </form>
            </div>
          </dialog>
        )}

        {isDialogReplenishOpen && (
          <dialog
            id="modalReplenishProduct"
            className="absolute top-0 right-0 left-0 bottom-0 z-10 w-full h-full bg-slate-900/80 flex justify-center items-center"
            onClick={handleModalReplenishProduct}
          >
            <div
              className="min-h-[50%] min-w-[50%] bg-white rounded-xl p-4 flex flex-col gap-4"
              onClick={(e) => e.stopPropagation()} // Evita cerrar al hacer clic dentro del recuadro
            >
              <p className="font-bold text-xl">Reabastece un producto:</p>
              <form onSubmit={handleFormModalReplenishProduct}>
                <label
                  htmlFor="replenish_product_quantity_input"
                  className="block"
                >
                  Cantidad a reabastecer:
                </label>
                <input
                  id="replenish_product_quantity_input"
                  type="number"
                  step="1"
                  placeholder="Introduce la cantidad para agregar..."
                  className="w-full max-w-md p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700 placeholder-gray-400"
                />
                <input
                  type="number"
                  step="1"
                  className="hidden"
                  defaultValue={productoAReabastecer.id_inventario}
                  id="replenish_product_id_input"
                />
                <input
                  type="submit"
                  value="Reabastecer producto"
                  className="block bg-blue-500 rounded-lg p-2 text-white font-bold my-2 cursor-pointer"
                />
              </form>
            </div>
          </dialog>
        )}

        {isViewReplenishOpen && (
          <dialog
            id="modalViewReplenish"
            className="absolute top-0 right-0 left-0 bottom-0 z-10 w-full h-full bg-slate-900/80 flex justify-center items-center"
            onClick={handleModalViewReplenish}
          >
            <div
              className="min-h-[50%] min-w-[50%] bg-white rounded-xl p-4 flex flex-col gap-4"
              onClick={(e) => e.stopPropagation()} // Evita cerrar al hacer clic dentro del recuadro
            >
              <p className="font-bold">
                Historial de reabastecimientos por día:
              </p>
              <DataTable
                columns={columns}
                data={replenishHistory}
                fixedHeader
                theme="default"
                striped={true}
                dense={true}
                pagination={true}
                paginationPerPage={5}
                paginationRowsPerPageOptions={[5, 10]}
              />
            </div>
          </dialog>
        )}

        {/* Barra superior */}
        <div className="flex justify-between text-center bg-slate-800 text-white py-4 px-8">
          <h1 className="text-2xl font-bold">Inventario de productos</h1>
          <button
            className="bg-green-500 p-2 rounded-xl"
            onClick={() => setIsDialogOpen(true)} // Abre el diálogo
          >
            <i className="align-middle fi fi-br-plus"></i> Añadir producto
          </button>
        </div>

        <div className="bg-slate-700 text-white p-4">
          <div className="flex gap-4">
            <button
              onClick={changeProductsToDiscontinued}
              className={`${
                descontinuados ? "bg-green-500" : "bg-red-500"
              } p-2 rounded-xl`}
            >
              {descontinuados
                ? "Ver productos disponibles"
                : "Ver productos descontinuados"}
            </button>
            <button
              className="bg-blue-500 p-2 rounded-xl"
              onClick={viewReplenish}
            >
              Ver historial de reabastecimientos
            </button>
          </div>
        </div>

        {/* Contenido principal */}
        {isLoading ? (
          <div className="flex justify-center my-10">
            <svg
              role="status"
              className="inline h-8 w-8 animate-spin mr-2 text-gray-200 dark:text-gray-600 fill-yellow-400"
              viewBox="0 0 100 101"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                fill="currentColor"
              />
              <path
                d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                fill="currentFill"
              />
            </svg>
          </div>
        ) : (
          <div className="flex p-4 gap-4 flex-wrap">
            {descontinuados
              ? productosDescontinuados.map((producto, index) => {
                  return (
                    <ProductCard
                      key={index}
                      imagen={producto.imagen_producto}
                      titulo={producto.nombre_producto}
                      cantidad={producto.cantidad_producto}
                      categoria={producto.categoria_producto}
                      descripcion={producto.descripcion_producto}
                      precio={producto.precio_unitario}
                      id={producto.id_inventario}
                      descontinuado={producto.descontinuado}
                      cantidad_maxima_producto={
                        producto.cantidad_maxima_producto
                      }
                      recargar={recargarProductos}
                      setRecargar={setRecargarProductos}
                      abrirEditar={setisDialogEditTypeProductOpen}
                      productoAEditar={productoAEditar}
                      cambiarProductoAEditar={setProductoAEditar}
                      abrirReabastecer={setIsDialogReplenishOpen}
                      cambiarProductoAReabastecer={setProductoAReabastecer}
                    />
                  );
                })
              : data.map((producto, index) => {
                  return (
                    <ProductCard
                      key={index}
                      imagen={producto.imagen_producto}
                      titulo={producto.nombre_producto}
                      cantidad={producto.cantidad_producto}
                      categoria={producto.categoria_producto}
                      descripcion={producto.descripcion_producto}
                      precio={producto.precio_unitario}
                      id={producto.id_inventario}
                      descontinuado={producto.descontinuado}
                      cantidad_maxima_producto={
                        producto.cantidad_maxima_producto
                      }
                      recargar={recargarProductos}
                      setRecargar={setRecargarProductos}
                      abrirEditar={setisDialogEditTypeProductOpen}
                      productoAEditar={productoAEditar}
                      cambiarProductoAEditar={setProductoAEditar}
                      abrirReabastecer={setIsDialogReplenishOpen}
                      cambiarProductoAReabastecer={setProductoAReabastecer}
                    />
                  );
                })}
          </div>
        )}
      </div>
    </>
  );
}

export default Inventario;
