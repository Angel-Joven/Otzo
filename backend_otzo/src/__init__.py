from flask import Flask
from .routes import ventas

app = Flask(__name__)


def init_app(config):
    # Configuration
    app.config.from_object(config)

    # Blueprints
    app.register_blueprint(ventas.ventas_bp, url_prefix="/api/ventas/")

    return app
