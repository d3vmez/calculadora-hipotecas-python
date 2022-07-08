from app.models.Hipoteca import Hipoteca
from app.models.Simulacion import Simulacion

import copy

from app.services.impl.HipotecaFijaServicio import HipotecaFijaServicio
from app.services.impl.HipotecaVariableServicio import HipotecaVariableServicio


class SimulacionServicio:

    N_SIMULACIONES = 100

    hipotecaFijaServicio = HipotecaFijaServicio()
    hipotecaVariableServicio = HipotecaVariableServicio()

    # Método para generar una hipoteca fija y una lista de hipotecas variables
    def generarHipoteca(self, hipoteca:Hipoteca, simulacion:Simulacion):

        # Generar hipoteca fija
        # Se clona un objeto de hipoteca para no interferir en los datos
        # de la hipoteca que se muestran por pantalla

        hipotecaFija = copy.copy(hipoteca)
        print(str(len(hipoteca.amortizaciones)))
        # Generar amortizaciones
        self.hipotecaFijaServicio.calcularAmortizaciones(hipotecaFija)
        simulacion.hipotecaFija = hipotecaFija

        #Generar hipotecas variables, tantas como se especifican en N_SIMULACIONES
        for i in range(0,self.N_SIMULACIONES,1):
            hipotecaVariable = Hipoteca(0.0, hipoteca.capitalInmueble, hipoteca.capitalAportado, 0.0, 0, hipoteca.plazo, 0, 0.0, "fijo", "hoy", None, None, None, None)
            self.hipotecaVariableServicio.calcularAmortizaciones(hipotecaVariable)
            simulacion.anadirHipotecaVariables(hipotecaVariable)



    # Método para calcular la probabilidad de que una hipoteca a tipo variable
    # sea más barata que una de tipo fijo
    def calcularProbabilidad(self, simulacion:Simulacion):

        # Variable para acumular las veces que el interés total de una
        # hipoteca variable es menor que una de tipo fijo
        acumulador = 0

        # Obtener los intereses totales de la hipoteca a tipo fijo
        interesFijo = simulacion.hipotecaFija.totalIntereses

        # Por cada hipoteca variable, se comprueba los intereses totales de cada
        # una de ellas con el interes total de la hipoteca fija
        for i in range(0,len(simulacion.hipotecasVariables),1):
            interesVariable = simulacion.hipotecasVariables[i].totalIntereses
            if interesFijo > interesVariable:
                acumulador = acumulador + 1

        # Porcentaje de que el interés fijo sea más caro que el variable
        porcentaje = (acumulador/self.N_SIMULACIONES) * 100

        return porcentaje

