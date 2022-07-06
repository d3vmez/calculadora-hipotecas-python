from app.models.Hipoteca import Hipoteca
from app.models.Simulacion import Simulacion

import copy

from app.services.impl.HipotecaFijaServicio import HipotecaFijaServicio
from app.services.impl.HipotecaVariableServicio import HipotecaVariableServicio


class SimulacionServicio:

    N_SIMULACIONES = 100

    hipotecaFijaServicio = HipotecaFijaServicio()
    hipotecaVariableServicio = HipotecaVariableServicio()

    def generarHipoteca(self, hipoteca:Hipoteca, simulacion:Simulacion):

        # Generar hipoteca fija
        # Se clona un objeto de hipoteca para no interferir en los datos
        # de la hipoteca que se muestran por pantalla

        hipotecaFija = copy.copy(hipoteca)

        # Generar amortizaciones
        self.hipotecaFijaServicio.calcularAmortizaciones(hipotecaFija)
        simulacion.hipotecaFija = hipotecaFija

        #Generar hipotecas variables, tantas como se especifican en N_SIMULACIONES
        for i in range(0,self.N_SIMULACIONES,1):
            hipotecaVariable = copy.copy(hipoteca)
            self.hipotecaVariableServicio.calcularAmortizaciones(hipotecaVariable)
            simulacion.anadirHipotecaVariables(hipotecaVariable)

    def calcularProbabilidad(self):
        pass


