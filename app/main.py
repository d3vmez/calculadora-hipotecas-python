from flaskr.models.Hipoteca import Hipoteca
from flaskr.services.impl.HipotecaFijaServicio import HipotecaFijaServicio
from flaskr.services.impl.HipotecaVariableServicio import HipotecaVariableServicio
from flaskr.services.impl.PonderacionInteresServicio import PonderacionInteresServicio

hipotecaFijaServicio = HipotecaFijaServicio ()
hipotecaVariableServicio = HipotecaVariableServicio()
hipoteca = Hipoteca(0.0, 120000.0, 40000.0, 0.0, 0.0, 2, 0, 0.0, "fijo", "hoy", 0.0, 1000.0, 10000.0, True)

hipotecaVariableServicio.calcularAmortizaciones(hipoteca)

print(str(hipoteca.tasaInteres))
capitalPorAmortizar = hipoteca.amortizaciones[len(hipoteca.amortizaciones) -1].capitalPorAmortizar


print(str(capitalPorAmortizar))
for a in hipoteca.amortizaciones:
    print(str(a))

