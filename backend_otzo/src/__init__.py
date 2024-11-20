from flask import Flask
from .routes import ventas
from .routes import fidelizacion
from .routes import clientes
from .routes import administracion

app = Flask(__name__)


def init_app(config):
    # Configuration
    app.config.from_object(config)

    # Blueprints
    app.register_blueprint(ventas.ventas_bp, url_prefix="/api/ventas/")
    app.register_blueprint(fidelizacion.fidelizacion_bp, url_prefix="/api/fidelizacion/")
    app.register_blueprint(clientes.clientes_bp, url_prefix="/api/clientes/")
    app.register_blueprint(administracion.administracion_bp, url_prefix="/api/administracion/")

    return app
