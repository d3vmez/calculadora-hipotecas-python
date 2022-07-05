from flaskr.services.IHipotecaServicio import IHipotecaServicio
from flaskr.models.Hipoteca import Hipoteca


class HipotecaFijaServicio(IHipotecaServicio):

    def calcularCuota(hipoteca:Hipoteca):

        cuota = 0.0

        # Calcular el valor del préstamo
        hipoteca.calcularValorDelPrestamo()
        prestamo = hipoteca.prestamo
        nCuotas = hipoteca.calcularNCuotas()
        tasaInteres = HipotecaFijaServicio.calcularTasaInteres(hipoteca)

        # Numerador y denominador con la fórmula para el cálculo de la cuota


    def calcularAmortizaciones(hipoteca):
        pass

    def calcularTasaInteres(hipoteca):
        print()