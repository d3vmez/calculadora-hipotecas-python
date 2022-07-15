from flask import Blueprint , request , jsonify

from app.function_jwt import escribir_token , validarToken

routesAuth = Blueprint("routesAuth", __name__)

@routesAuth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if data['username'] == "Marcos":
        return escribir_token(data=request.get_json())
    else:
        response = jsonify({"message": "Usuario no encontrado"})
        response.status_code = 404
        return response

@routesAuth.route("/validar-token", methods=["POST"])
def validar():
    token = request.headers['Authorization'].split(" ")[1]
    return validarToken(token, True)
