import React from "react";

function Productos() {
  return (
    <div className="w-full h-full p-4">
      <motion.div
        initial={{ x: -200, opacity: 0 }}
        animate={{ x: 0, opacity: 1, transition: { delay: 0.8 } }}
        className="w-full h-full bg-white/100 rounded-lg p-4 shadow-[0px_4px_6px_0px_rgba(0,_0,_0,_0.1)]"
      >
        <div className="rounded-lg p-4 bg-gray-900 z-10">
          <h2 className="font-bold text-white">
            <i className="align-middle fi fi-sr-boxes"></i> Productos
          </h2>
        </div>
        <div className="h-[calc(25vh)] md:h-[calc(50vh)]">
          <div className="p-4 h-full overflow-y-auto">
            <div className="w-full flex gap-4 items-center">
              <i className="align-middle fi fi-bs-search"></i>
              <input
                className="w-full bg-transparent placeholder:text-gray-900 text-green-700 text-sm border border-gray-200 rounded-md px-3 py-2 transition duration-300 ease focus:outline-none focus:border-green-500 hover:border-green-300 focus:hover:placeholder:text-green-700 shadow-sm focus:shadow"
                placeholder="Buscar..."
                onChange={handleChange}
              />
            </div>
            <DataTable
              className="p-1"
              columns={columns}
              data={records}
              fixedHeader
              customStyles={customStyles}
              progressPending={loading}
              progressComponent={<Spinner />}
            />
            {/* selectableRows */}
          </div>
        </div>
      </motion.div>
    </div>
  );
}

export default Productos;
