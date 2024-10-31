from src.tests.test_db_connection import test_connection
from config import config
from src import init_app

configuration = config["development"]
app = init_app(configuration)

test_connection()

if __name__ == "__main__":
    app.run()
