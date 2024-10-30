from flask import Flask
from .db import get_connection

app = Flask(__name__)


def init_app(config):
    # Configuration
    app.config.from_object(config)

    db = get_connection()

    return app
