from app.services.IHipotecaServicio import IHipotecaServicio
from app.services.impl.AmortizacionServicio import AmortizacionServicio
from app.services.impl.PonderacionInteresServicio import PonderacionInteresServicio
from app.models.Hipoteca import Hipoteca

def nums(first_number, last_number, step=1):
    return range (first_number, last_number + 1, step)

class HipotecaFijaServicio(IHipotecaServicio):

    ponderacionInteresServicio = PonderacionInteresServicio()
    amortizacionServicio = AmortizacionServicio()

    def calcularCuota(self,hipoteca):

        cuota = 0.0

        # Calcular el valor del préstamo
        hipoteca.calcularValorDelPrestamo()
        prestamo = hipoteca.prestamo
        nCuotas = hipoteca.calcularNCuotas()
        tasaInteres = self.calcularTasaInteres(hipoteca)

        # Numerador y denominador con la fórmula para el cálculo de la cuota
        numerador = tasaInteres * pow(1 + tasaInteres, nCuotas)
        denominador = pow(1 + tasaInteres, nCuotas) -1

        cuota = prestamo * (numerador/denominador)

        hipoteca.cuota = cuota

    def calcularAmortizaciones(self,hipoteca):

        # Calcular cuota mensual de la hipoteca
        self.calcularCuota(hipoteca)

        # Obtener número de cuotas
        nCuotas = hipoteca.calcularNCuotas()

        # Obtener el porcentaje del interés a pagar en cada cuota
        tasaInteres = self.calcularTasaInteres(hipoteca)

        for i in nums(1,nCuotas):
            # Se crea una nueva amortización para la hipoteca fija
            amortizacion = self.amortizacionServicio.crearAmortizacion(hipoteca,i,tasaInteres)
            hipoteca.anadirAmortizacion(amortizacion)

    def calcularTasaInteres(self, hipoteca):

        # Si la hipoteca no tiene una tasa de interés, se cálcula
        # mediante una ponderación sobre los parámetros que afectan
        # al valor del interés.
        # (SINGLETON)
        tasaInteres = hipoteca.tasaInteres
        if tasaInteres == 0.0:
            tasaInteres = self.ponderacionInteresServicio.calcularInteresTotal(hipoteca)
            hipoteca.tasaInteres = tasaInteres

        tasaInteres = tasaInteres / (100 * Hipoteca.N_MENSUALIDADES)

        # Se devuelve el interes calculado
        return tasaInteres

