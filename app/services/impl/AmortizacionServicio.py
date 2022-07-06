from app.models import Hipoteca


# Este servicio se encarga de crear las amortizaciones para la hipoteca
from app.models.Amortizacion import Amortizacion


class AmortizacionServicio:

    capitalPorAmortizar = 0.0
    totalPorAmortizar = 0.0

    # Si es la primera cuota se inicalizan los valores para
    # el capital por amortizar, que se corresponde con el préstamo inicial,
    # y total amortizado, que será 0
    def crearAmortizacion(self, hipoteca:Hipoteca, nCuotas, tasaInteres):

        # Si es la primera cuota se inicalizan los valores para
        # el capital por amortizar, que se corresponde con el préstamo inicial,
        # y total amortizado, que será 0

        if nCuotas == 1:
            self.capitalPorAmortizar = hipoteca.prestamo
            self.totalPorAmortizar = 0.0

        # Calcular intereses
        intereses = self.calcularIntereses(tasaInteres,self.capitalPorAmortizar)
        self.actualizarInteresTotal(intereses,hipoteca)

        # Calcular cuota de amortizacion
        cuotaAmortizacion = self.calcularCuotaAmortizacion(hipoteca.cuota, intereses)

        # Calcular el total amortizado
        self.actualizarTotalAmortizado(cuotaAmortizacion)

        # Calcular capital por amortizar
        self.actualizarCapitalPorAmortizar(cuotaAmortizacion)

        return Amortizacion(nCuotas, hipoteca.cuota, intereses, cuotaAmortizacion,self.totalPorAmortizar, self.capitalPorAmortizar)

    # Métodos auxiliares
    #################################################################

    # Método para calcular los intereses que se pagan en cada cuota
    def calcularIntereses(self, tasaInteres, capitalPorAmortizar):
        return capitalPorAmortizar * tasaInteres

    # Método para calcular el importe de la cuota, sin contar con los intereses
    def calcularCuotaAmortizacion(self, cuota, interes):
        return cuota - interes

    # Método para actualizar el total amortizado
    def actualizarTotalAmortizado(self, cuota):
        self.totalPorAmortizar += cuota

    # Método para actualizar el capital por amortizar
    def actualizarCapitalPorAmortizar(self, cuota):
        self.capitalPorAmortizar -= cuota

    # Método para acumular los intereses de cada una de las amortizaciones de la hipoteca
    def actualizarInteresTotal(self, interes, hipoteca:Hipoteca):
        hipoteca.totalIntereses += interes

