
from config import Config, get_environment_config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)

# Obtener la configuracion del ambiente elegido
app.config.from_object(get_environment_config())

# Inicializa la conexion a la BD
db.init_app(app)

@app.before_first_request
def initialize_database():
    """ Crea las tablas de la BD """
    db.create_all()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()

@app.route("/")
def test():
    return "Test ok!"

app.run(port=5001, debug=True, host="0.0.0.0")