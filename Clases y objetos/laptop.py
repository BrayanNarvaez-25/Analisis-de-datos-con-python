import random

class laptop:
    def __init__(self,marca,procesador,memoria,costo = 500, impuesto = 10):
        self.marca = marca
        self.procesador = procesador
        self.memoria = memoria
        self.costo = costo
        self.impuesto = impuesto

    def valorFinal(self):
        return self.costo + self.impuesto
    
    def valorDescuento(self,descuento):
        return (self.costo * descuento)/100
    
    def ralizarDiagnosticoSistema(self):
        resultado = {
            "MARCA" : f"{self.marca}",
            "PROCESADOR" : f"{self.procesador}",
            "MEMORIA RAM" : "OK" if self.memoria >= 8 else "Aumentar memoria Ram",
            "BATERIA" : "OK" if random.choice([True,False]) else "Cambiar de bateria"
        }
        return resultado
    
    def realizarInformeUso(self):
        resultadoInforme = {
            "Tipo": "Generica",
            "Uso Recomendado" : "Tareas cotidianas",
            "Horas de uso" : 5,
            "Diagnostico actual" : self.ralizarDiagnosticoSistema()
        }
        return resultadoInforme

    @staticmethod
    def compararCosto(laptop1,laptop2):
        if laptop1.costo == laptop2.costo:
            return "Los costos son iguales"
        else:
            return "Los costos son diferentes"
        
    @classmethod
    def asusLaptop(cls,costo):
        marca = "asus"
        procesador = "i5"
        memoria = 16
        return cls(marca,procesador,memoria,costo)