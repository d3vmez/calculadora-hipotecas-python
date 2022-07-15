from flask import jsonify
from jwt import encode, decode
from jwt import exceptions
from os import getenv
from datetime import datetime, timedelta

def fecha_expiracion(dias: int):
    hoy = datetime.now()
    fechaExpiracion = hoy + timedelta(dias)
    return fechaExpiracion

def escribir_token(data: dict):
    token = encode(payload={**data, "exp": fecha_expiracion(2)}, key=getenv("SECRET_KEY"), algorithm="HS256")
    return token.encode("UTF-8")

def validarToken(token, output = False):
    try:
        if output:
            return decode(token, key=getenv("SECRET_KEY"), algorithms="HS256")
        decode(token , key=getenv("SECRET_KEY") , algorithms="HS256")

        if not token:
            return jsonify({'message': 'a valid token is missing'})

    except exceptions.DecodeError:
        response = jsonify({"message" : "Invalid Token"})
        response.status_code = 401
        return response

    except exceptions.ExpiredSignatureError:
        response = jsonify({"message" : "Expired Token"})
        response.status_code = 401
        return response



