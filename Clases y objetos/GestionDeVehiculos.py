class Vehiculo:
    def __init__(self,marca,modelo,anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
    
    def descripcion(self):
        print(f"\nMarca: {self.marca} \nModelo: {self.modelo} \nAño: {self.anio}")
    

class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio,numPuertas):
        super().__init__(marca, modelo, anio)
        self.numPuertas = numPuertas
    
    def descripcion(self):
        print(f"\nMarca: {self.marca} \nModelo: {self.modelo} \nAño: {self.anio} \nN.Puertas: {self.numPuertas}")


class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio,tipo):
        super().__init__(marca, modelo, anio)
        self.tipo = tipo
    
    def descripcion(self):
        print(f"\nMarca: {self.marca} \nModelo: {self.modelo} \nAño: {self.anio} \nTipo: {self.tipo}")
        pass