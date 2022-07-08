from flask import json

# DTO para enviar un objeto Hipoteca con su simulación a la vista
class HipotecaDTO:

    def __init__(self, hipoteca, porcentaje):
        self.hipoteca = hipoteca
        self.porcentaje = porcentaje

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)



