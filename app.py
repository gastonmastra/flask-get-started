'''This is the entrypoint of the API'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import get_environment_config

db = SQLAlchemy()

app = Flask(__name__)

# Obtener la configuracion del ambiente elegido
app.config.from_object(get_environment_config())

# Inicializa la conexion a la BD
db.init_app(app)

@app.before_request
def initialize_database():
    """ Crea las tablas de la BD """
    app.before_request_funcs[None].remove(initialize_database)
    db.create_all()

@app.teardown_appcontext
def shutdown_session(exception=None):
    ''' Disconnect the session '''
    print(exception)
    db.session.remove()

@app.route("/")
def test():
    ''' Chequeo de que la API esta levantada '''
    return "Test ok!"

app.run(port=5000, debug=True, host="0.0.0.0")
