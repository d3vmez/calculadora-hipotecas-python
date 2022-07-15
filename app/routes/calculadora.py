import json
from types import SimpleNamespace

from flask import Blueprint , request , Flask
from flask_cors import cross_origin , CORS

from app.function_jwt import validarToken

from app.models.Hipoteca import Hipoteca
from app.models.HipotecaDTO import HipotecaDTO
from app.models.Simulacion import Simulacion
from app.services.impl.HipotecaFijaServicio import HipotecaFijaServicio
from app.services.impl.HipotecaVariableServicio import HipotecaVariableServicio
from app.services.impl.SimulacionServicio import SimulacionServicio

calculadora_blueprint = Blueprint("calculadora_blueprint", __name__)

hipotecaFijaServicio = HipotecaFijaServicio()
hipotecaVariableServicio = HipotecaVariableServicio()
simulacionServicio = SimulacionServicio()


@calculadora_blueprint.before_request
def validar_token_middleware():
    print(1)
    token = request.headers['Authorization'].split(" ")[1]
    return validarToken(token,False)

@calculadora_blueprint.route("/calculadora", methods=["POST"])
def calculadora():

    print(request.headers['Authorization'].split(" ")[1])
    # Almacenar el JSON recibido en un objeto Hipoteca
    print(type(request.json['capitalInmueble']))
    hipoteca = Hipoteca(request.json['totalIntereses'], request.json['capitalInmueble'],
                        request.json["capitalAportado"] , request.json["prestamo"] , request.json["cuota"],
                        request.json["plazo"] , request.json["plazoRestante"] , request.json["tasaInteres"],
                        request.json["tipoInteres"] , request.json["fechaNacimiento"] , request.json["ahorros"],
                        request.json["nomina"],request.json["otrosPrestamos"], request.json["esPrimeraVivienda"] )


    simulacion = Simulacion(None,None,None)
    simulacionServicio.generarHipoteca(hipoteca,simulacion)
    porcentaje = simulacionServicio.calcularProbabilidad(simulacion)

    hipoteca.amortizaciones = list()

    if request.json["tipoInteres"] == "fijo":
        hipotecaFijaServicio.calcularAmortizaciones(hipoteca)
        print("cuota" + str(hipoteca.cuota))
    else:
        hipotecaVariableServicio.calcularAmortizaciones(hipoteca)

    response = HipotecaDTO(hipoteca,porcentaje)

    return response.toJson()