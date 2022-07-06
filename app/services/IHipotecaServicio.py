from abc import abstractmethod
from abc import ABCMeta

# Interfaz para el servicio Hipoteca
from flaskr.models import Hipoteca


class IHipotecaServicio(metaclass=ABCMeta):

    # Método para calcular la cuota que se deberá pagar al mes, incluyendo los intereses
    @abstractmethod
    def calcularCuota(self,hipoteca:Hipoteca):
        pass

    # Método para calcular cada una de las amortizaciones que conforman una hipoteca
    @abstractmethod
    def calcularAmortizaciones(self,hipoteca:Hipoteca):
        pass

    # Método calcular la tasa de interes en base a las mensualidades
    @abstractmethod
    def calcularTasaInteres(self,hipoteca:Hipoteca):
        pass

