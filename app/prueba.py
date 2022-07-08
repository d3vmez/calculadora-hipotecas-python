from app.main import hipotecaFijaServicio
from app.models.Hipoteca import Hipoteca
from app.models.Simulacion import Simulacion
from app.services.impl.HipotecaFijaServicio import HipotecaFijaServicio
from app.services.impl.SimulacionServicio import SimulacionServicio

hipoteca = Hipoteca(0.0, 120000.0, 40000.0, 0.0, 0, 2, 0, 0.0, "fijo", "hoy", 0.0, 1000.0, 10000.0, True)

simulacionServicio = SimulacionServicio()
simulacion = Simulacion(None,None,None)
simulacionServicio.generarHipoteca(hipoteca,simulacion)
porcentaje = simulacionServicio.calcularProbabilidad(simulacion)

print(str(porcentaje))

