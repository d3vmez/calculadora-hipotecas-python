# Clase Amortizacion
class Amortizacion:

    # Constructor
    def __init__(self, numeroCuota, cuota, interes, cuotaAmortizacion, totalAmortizacion, capitalPorAmortizar):
        self.capitalPorAmortizar = capitalPorAmortizar
        self.totalAmortizacion = totalAmortizacion
        self.cuotaAmortizacion = cuotaAmortizacion
        self.interes = interes
        # Cuota total
        self.cuota = cuota
        self.numeroCuota = numeroCuota

    def __str__(self):
        return "Amortizacion[" + str(self.numeroCuota) + "]" + " Cuota total: " + str(
            self.cuota) + "Intereses: " + str(self.interes) + " Cuota amortizacion" + "Total amortizado: " + str(
            self.totalAmortizacion) + " Capital por amortizar: " + str(self.capitalPorAmortizar)
