from laptop import laptop

class laptopGaming(laptop):
    def __init__(self, marca, procesador, memoria, tarjetaGrafica ,costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria,costo, impuesto)
        self.tarjetaGrafica = tarjetaGrafica
    
    def __str__(self):
        return f"\nMarca: {self.marca} \nProcesador: {self.procesador} \nMemoria: {self.memoria} \nTargeta Gráfica: {self.tarjetaGrafica} \nCosto: {self.costo} \nImpuesto: {self.impuesto}"

    def ralizarDiagnosticoSistema(self):
        resultadoDiagnostico = super().ralizarDiagnosticoSistema()
        resultadoJuegos = self.ralizarDiagnosticoJuegos()
        resultadoDiagnostico["Resultado juegos"] = resultadoJuegos
        return resultadoDiagnostico
    
    def realizarInformeUso(self):
        informe = super().realizarInformeUso()
        informe.update({
            "Tipo": "Gaming",
            "Uso Recomendado" : "Juegos de video",
            "Horas de uso" : 10,
            "Recomendaciones de software" : ["Antivirus","VPN"]
        })
        return informe
    
    def ralizarDiagnosticoJuegos(self):
        juegos = ["FORNITE","COD","GTA"]
        resultados = {}
        for juego in juegos:
            fpsBase = 30
            if "RTX" in self.tarjetaGrafica:
                fps = fpsBase * 3
            elif "GTX" in self.tarjetaGrafica:
                fps = fpsBase * 2
            else:
                fps = fpsBase
            
            resultados [juego] = f"{fps} FPS"
        return resultados

    pass