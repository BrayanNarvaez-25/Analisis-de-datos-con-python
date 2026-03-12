from laptop import laptop
import random

class laptopBusiness(laptop):
    def __init__(self, marca, procesador, memoria,almacenamiento, duracionBat, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.almacenamiento = almacenamiento
        self.duracionBat = duracionBat

    def ralizarDiagnosticoSistema(self):
        resultado = super().ralizarDiagnosticoSistema()
        resultado["Almacenamiento:"] = f"{self.almacenamiento} GB"
        resultado["Duracion estimada"] = f"{self.duracionBat} horas"
        resultado["Conectividad"] = self.verificarConectividadRed()
        
        return resultado

    def verificarConectividadRed(self):
        disponibilidadWifi = random.choice([True, False])
        accesoServidores = random.choice([True, False])
        latencia = f"{random.randint(5, 150)} ms"
        diagnosticoRed = {
            "Wi-Fi Disponible": "OK" if disponibilidadWifi else "Sin conexión",
            "Servidores Empresariales": "Acceso concedido" if accesoServidores else "Error de autenticación",
            "Latencia de Red": latencia
        }
        
        return diagnosticoRed