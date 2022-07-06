
# Implementación de la interfaz IHipotecaServicio
# Este servicio se encarga de calcular la cuota y amortizaciones
# de una hipoteca de interés variable
import random
from app.models.Hipoteca import Hipoteca
from app.services.IHipotecaServicio import IHipotecaServicio
from app.services.impl.AmortizacionServicio import AmortizacionServicio

def nums(first_number, last_number, step=1):
    return range (first_number, last_number + 1, step)

class HipotecaVariableServicio(IHipotecaServicio):

    EURIBOR = 0.2/(100 * Hipoteca.N_MENSUALIDADES)
    DIFERENCIAL = 2.5

    amortizacionServicio = AmortizacionServicio()

    def calcularCuota(self, hipoteca:Hipoteca):

        cuota = 0.0
        # Si el plazo restante es igual a 0, quiere decir que nos encontramos en el
        # primer cálculo de la cuota por ello se debe establecer
        # el plazo restante = número de cuotas totales,
        # el plazo restante = número de cuotas totales,
        if hipoteca.plazoRestante == 0:
            hipoteca.plazoRestante = hipoteca.calcularNCuotas()
            hipoteca.calcularValorDelPrestamo()

        # Como es una hipoteca variable se juega con el plazo restante, ya que la cuota
        # necesita ser recalculada
        nCuotas = hipoteca.plazoRestante
        tasaInteres = self.calcularTasaInteres(hipoteca)

        # Numerador y denominador con la fórmula para el cálculo de la cuota
        numerador = tasaInteres * pow(1 + tasaInteres, nCuotas)
        denominador = pow(1 + tasaInteres, nCuotas) -1

        # Si la hipoteca no tiene amortizaciones, el capital por amortizar
        # es igual al préstamo,
        # ya que nos encontramos en el cáclulo de la cuota para el primer año.
        # En caso contrario, se tomará el capital por amortizar que tiene
        # la última amortizacion  de la hipoteca
        capitalPorAmortizar= 0.0
        if len(hipoteca.amortizaciones) != 0:
            capitalPorAmortizar = hipoteca.amortizaciones[len(hipoteca.amortizaciones) -1].capitalPorAmortizar
        else:
            capitalPorAmortizar = hipoteca.prestamo

        cuota = capitalPorAmortizar * (numerador/denominador)

        hipoteca.cuota = cuota

    def calcularAmortizaciones(self, hipoteca):
        # Calcular cuota de la hipoteca
        self.calcularCuota(hipoteca)

        # Obtener número de cuotas
        nCuotas = hipoteca.plazoRestante

        # Obtener el interés calcula que se pagará en cada cuota
        tasaInteres = self.calcularTasaInteres(hipoteca)

        acumuladorPlazos = 1
        for i in nums(1,nCuotas):
            # Si el acumulador de plazos llega a 13, es decir, se ha cumplido un año con la hipoteca
            # se tiene que recalcular la hipoteca

            if acumuladorPlazos == 13:
                self.recalcularHipoteca(hipoteca)
                # Se actualizan la nueva tasa de interés
                tasaInteres = self.calcularTasaInteres(hipoteca)
                acumuladorPlazos = 1

            acumuladorPlazos = acumuladorPlazos + 1

            # Se crea la nueva amortización para hipoteca variable
            amortizacion = self.amortizacionServicio.crearAmortizacion(hipoteca, i , tasaInteres)
            hipoteca.anadirAmortizacion(amortizacion)

    def calcularTasaInteres(self, hipoteca):
        # Si la hipoteca no tiene una tasa de interés, se le aplica
        # el diferencial (interés fijo en una hipoteca variable)
        # (SINGLETON)
        tasaInteres = hipoteca.tasaInteres
        if tasaInteres == 0.0:
            tasaInteres = self.DIFERENCIAL
            hipoteca.tasaInteres = tasaInteres

        # Se devuelve el interes calculado más el EURIBOR
        return (tasaInteres/(100 * Hipoteca.N_MENSUALIDADES)) + self.EURIBOR

    # Métodos auxiliares
    #################################################################

    # Método para cambiar el valor del EURIBOR
    def variarEURIBOR(self):
        EURIBOR = 0.2/(100 * Hipoteca.N_MENSUALIDADES)
        variacionEURIBOR = random.uniform(-1.0, 1.0)
        self.EURIBOR += variacionEURIBOR/(100 * Hipoteca.N_MENSUALIDADES)

    # Método para recalcular la cuota, con un nuevo valor para el euribor
    # y un número diferente de cuotas restantes (plazo)
    def recalcularHipoteca(self, hipoteca:Hipoteca):
        # Simular una variación en el EURIBOR
        self.variarEURIBOR()

        # Actualizar el número de plazos restantes para finalizar la hipoteca
        hipoteca.recalcularPlazoRestante()

        # Calcular la nueva cuota para el siguiente año
        self.calcularCuota(hipoteca)


