# Clase Hipoteca
class Hipoteca:
    # Constante para almacenar el número de mensualidades
    # que existirán en un año
    N_MENSUALIDADES=12

    # Constructor
    def __init__(self, totalIntereses, capitalInmueble, capitalAportado, prestamo, cuota, plazo, plazoRestante,
                 tasaInteres, tipoInteres, fechaNacimiento, ahorros, nomina, otrosPrestamos,
                 esPrimeraVivienda):

        self.esPrimeraVivienda = esPrimeraVivienda
        self.otrosPrestamos = otrosPrestamos
        self.nomina = nomina
        self.ahorros = ahorros
        self.fechaNacimiento = fechaNacimiento
        self.amortizaciones = list()
        self.tipoInteres = tipoInteres
        self.tasaInteres = tasaInteres
        self.plazoRestante = plazoRestante
        self.plazo = plazo
        self.cuota = cuota
        self.prestamo = prestamo
        self.capitalAportado = capitalAportado
        self.capitalInmueble = capitalInmueble
        self.totalIntereses = totalIntereses

    # Método para añadir una amortizacion a la hipoteca
    def anadirAmortizacion(self,amortizacion):
        self.amortizaciones.append(amortizacion)

    # Método para comprobar si la hipoteca es de tipo fijo
    def esTipoFijo(self):
        if (self.tipoInteres == "fijo"):
            return True
        return False

    # Método para calcular el importe final del préstamo
    def calcularValorDelPrestamo(self):
        capitalInmueble=self.capitalInmueble
        capitalAportado=self.capitalAportado

        prestamo=capitalInmueble - capitalAportado
        self.prestamo=prestamo

    # Método para transformar el plazo en años en mensualidades
    def calcularNCuotas(self):
        nCuotas=self.plazo * Hipoteca.N_MENSUALIDADES
        return nCuotas

    # Método para recalcular los plazos restantes de la hipoteca
    def recalcularPlazoRestante(self):
        plazoRestante=self.plazoRestante - Hipoteca.N_MENSUALIDADES
        self.plazoRestante=plazoRestante

    def __str__(self):
        return "Hipoteca: " + self.amortizaciones