

# Clase Simulacion
from flask import json


class Simulacion:

    # Constructor
    def __init__(self, hipotecaFija, nSimulaciones, porcentaje):
        self.porcentaje = porcentaje
        self.nSimulaciones = nSimulaciones
        self.hipotecaFija = hipotecaFija
        self.hipotecasVariables = list()

    def anadirHipotecaVariables(self,hipotecaVariable):
        self.hipotecasVariables.append(hipotecaVariable)

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)


