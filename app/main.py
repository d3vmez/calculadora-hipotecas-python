
from flask import Flask , jsonify , request
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv

from app.routes.auth import routesAuth
from app.routes.calculadora import calculadora_blueprint

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(routesAuth, url_prefix="/api")
app.register_blueprint(calculadora_blueprint, url_prefix="/api")

if __name__ == "__main__":
    load_dotenv()
    app.run(None , 8859 , True)
