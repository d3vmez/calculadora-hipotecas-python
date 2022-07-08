from flask import Flask , jsonify , request
from flask_cors import CORS, cross_origin

from app.models.Hipoteca import Hipoteca
from app.models.HipotecaDTO import HipotecaDTO
from app.models.Simulacion import Simulacion
from app.services.impl.HipotecaFijaServicio import HipotecaFijaServicio
from app.services.impl.HipotecaVariableServicio import HipotecaVariableServicio
from app.services.impl.SimulacionServicio import SimulacionServicio

app = Flask(__name__)
cors = CORS(app)
app.config["CORS-HEADERS"] = "Content-Type"

hipotecaFijaServicio = HipotecaFijaServicio()
hipotecaVariableServicio = HipotecaVariableServicio()
simulacionServicio = SimulacionServicio()

@app.route("/api/calculadora" , methods=["POST"])
@cross_origin()
def calculadoraSubmit():
    # Almacenar el JSON recibido en un objeto Hipoteca
    hipoteca = Hipoteca(request.json['totalIntereses'] , request.json['capitalInmueble'],
                        request.json["capitalAportado"] , request.json["prestamo"] , request.json["cuota"] ,
                        request.json["plazo"] , request.json["plazoRestante"] , request.json["tasaInteres"] ,
                        request.json["tipoInteres"] , request.json["fechaNacimiento"] , request.json["ahorros"] ,
                        request.json["nomina"] , request.json["otrosPrestamos"] , request.json["esPrimeraVivienda"])

    simulacion = Simulacion(None,None,None)
    simulacionServicio.generarHipoteca(hipoteca,simulacion)
    porcentaje = simulacionServicio.calcularProbabilidad(simulacion)

    hipoteca.amortizaciones = list()

    if request.json["tipoInteres"] == "fija":
        hipotecaFijaServicio.calcularAmortizaciones(hipoteca)

    else:
        hipotecaVariableServicio.calcularAmortizaciones(hipoteca)

    response = HipotecaDTO(hipoteca,porcentaje)

    print(str(porcentaje))

    return response.toJson()

if __name__ == "__main__":
    app.run(None , 8859 , True)
