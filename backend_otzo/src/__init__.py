from flask import Flask
from .routes import ventas
from .routes import fidelizacion

app = Flask(__name__)


def init_app(config):
    # Configuration
    app.config.from_object(config)

    # Blueprints
    app.register_blueprint(ventas.ventas_bp, url_prefix="/api/ventas/")
    app.register_blueprint(
        fidelizacion.fidelizacion_bp, url_prefix="/api/fidelizacion/"
    )

    return app
