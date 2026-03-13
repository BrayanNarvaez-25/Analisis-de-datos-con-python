from abc import ABC,abstractmethod

class Empleado(ABC):
    def __init__(self,nombre,salarioBase):
        self.nombre = nombre
        self.salarioBase = salarioBase

    @abstractmethod
    def calcularSalario(self):
        pass

        

class EmpleadoTiempoCompleto(Empleado):
    def calcularSalario(self):
        bono = self.salarioBase * 0.20
        return f"El salario a tiempo completo es: {self.salarioBase + bono}"
 
class EmpleadoMedioTiempo(Empleado):
    def calcularSalario(self):
        bono = self.salarioBase * 0.10
        return f"El salario a medio tiempo es: {self.salarioBase + bono}"
    pass