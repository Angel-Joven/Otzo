from src.tests.test_db_connection import test_connection, test_query, test_query_fidelizacion
from config import config
from src import init_app
from flask_cors import CORS

configuration = config["development"]
app = init_app(configuration)
CORS(app, resources={r"*": {"origins": "*"}})

test_connection()
test_query()
test_query_fidelizacion()

if __name__ == "__main__":
    app.run()
