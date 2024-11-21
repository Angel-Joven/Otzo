from flask import Flask
from routes import reportes_bp

app = Flask(__name__)

# Registrar Blueprint
app.register_blueprint(reportes_bp)

if __name__ == '__main__':
    app.run(debug=True)