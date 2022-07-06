
# Este servicio se encarga de generar un valor para el interés
# de una hipoteca a tipo fijo según unos parámetros
from flaskr.models.Hipoteca import Hipoteca


class PonderacionInteresServicio:

    # Definición de constantes
    INTERES_MAX = 4.0
    INTERES_MIN = 2.0
    PESO_TOTAL = 100

    # Peso máximo que pueden teener cada uno de los parámetros
    PESO_NOMINA =       0.4     *       PESO_TOTAL
    PESO_CUOTA =        0.3     *       PESO_TOTAL
    PESO_AHORRO =       0.05    *       PESO_TOTAL
    PESO_PRESTAMOS =    0.2     *       PESO_TOTAL
    PESO_VIVIENDA =     0.05    *       PESO_TOTAL

    # Variable para acumular el peso de todos los parámetros
    acumuladorPesos = 0.0

    # Método para calcular el interés de la hipoteca a tipo fijo
    def calcularInteresTotal(self,hipoteca:Hipoteca):

        # Obtener el valor de los parámetros
        ahorros = hipoteca.ahorros
        nomina = hipoteca.nomina
        nCuotas = hipoteca.calcularNCuotas()
        otrosPrestamos = hipoteca.otrosPrestamos
        primeraVivienda = hipoteca.esPrimeraVivienda

        # Calcular cada uno de los pesos de los parámetros
        self.calcularPesoAhrorro(ahorros)
        self.calcularPesoCuota(nCuotas)
        self.calcularPesoNomina(nomina)
        self.calcularPesoOtrosPrestamos(otrosPrestamos)
        self.calcularPesoPrimeraVivienda(primeraVivienda)

        # Calcular el valor en porcentaje de un único peso
        valorPeso = self.calcularPeso()

        # Número de pesos totales
        nPesos = self.acumuladorPesos

        # Resetear acumulador a 0
        self.acumuladorPesos = 0.0

        # Calcular interés
        interesTotal = (valorPeso * nPesos) + self.INTERES_MIN

        return interesTotal

    # Métodos auxiliares
    #################################################################

    # Método para calcular el valor de un único peso
    def calcularPeso(self):
        peso = (self.INTERES_MAX - self.INTERES_MIN)/self.PESO_TOTAL
        return peso

    # Método para calcular el peso que tiene la nómina sobre
    def calcularPesoNomina(self, nomina):
        if (nomina <= 1000):
            self.acumuladorPesos += self.PESO_NOMINA
        elif (nomina > 1000 and nomina < 2000):
            self.acumuladorPesos += 20.0
        elif (nomina >= 2000):
            self.acumuladorPesos += 5.0

    # Método para calcular el peso que tienen el número de cuotas
    # sobre el interés
    def calcularPesoCuota(self, nCuotas):
        if (nCuotas <= 24):
            self.acumuladorPesos += 10.0
        elif (nCuotas > 24 and nCuotas < 48):
            self.acumuladorPesos += 20.0
        elif (nCuotas >= 48):
            self.acumuladorPesos += self.PESO_CUOTA

    # Método para calcular el peso que tienen los ahorros del cliente
    # sobre el interés
    def calcularPesoAhrorro(self, ahorros):
        if(ahorros<10000):
            self.acumuladorPesos += self.PESO_AHORRO

    # Método para calcular el peso que tienen las deudas del cliente
    # sobre el interés
    def calcularPesoOtrosPrestamos(self, otrosPrestamos):
        if (otrosPrestamos >= 10000 and otrosPrestamos < 20000):
            self.acumuladorPesos += 10.0
        elif (otrosPrestamos >= 20000):
            self.acumuladorPesos += self.PESO_PRESTAMOS

    # Método para calcular el peso que tiene si es primera vivienda
    # sobre el interés
    def calcularPesoPrimeraVivienda(self, esPrimeraVivienda):
        if (esPrimeraVivienda):
            self.acumuladorPesos += self.PESO_VIVIENDA



