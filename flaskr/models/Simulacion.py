# Clase Simulacion
class Simulacion:

    # Constructor
    def __init__(self, hipotecaFija, nSimulaciones, porcentaje):
        self.porcentaje = porcentaje
        self.nSimulaciones = nSimulaciones
        self.hipotecaFija = hipotecaFija
        self.hipotecasVariables = list()


