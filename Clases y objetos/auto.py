from datetime import date

class auto:
    def __init__(self,marca,modelo,anio,kilometraje = 0):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje

    def mostrarInfo(self):
        print(f"---INFORMACIÓN DE SU AUTO--- \nMarca: {self.marca} \nModelo: {self.modelo} \nAño: {self.anio} \nKilometraje: {self.kilometraje}")
    
    def actualizarKilometraje(self,nuevoKilometraje):
        if nuevoKilometraje >= self.kilometraje:
            self.kilometraje = nuevoKilometraje
            print("\n---Kilometraje actualizado---")
        else:
            print("\n---No se puede reducir el kilometraje---")
        print(f"Su kilometraje: {self.kilometraje}")
    
    def realizarViaje(self,kmRecorridos):
        if kmRecorridos >= 0:
            self.kilometraje += kmRecorridos
            print("\n---Se agregaron los kilometros recorridos---")
        else:
            print("\n---La cantidad de kilómetros debe ser positiva---")
        print(f"Su kilometraje: {self.kilometraje}")
        
    def estadoAuto(self):
        if self.kilometraje < 20000:
            print("\nSu auto dice: Estoy como nuevo!!!")
        elif self.kilometraje >= 20000 and self.kilometraje <= 100000:
            print("\nSu auto dice: Ya estoy usado :)")
        else:
            print("\nSu auto dice: ¡Ya déjame descansar por favor!")

    @classmethod
    def crearAuto(cls,modelo):
        marca = "Toyota"
        anio = date.today().year
        return cls(marca,modelo,anio)
    
    @classmethod
    def crearAutoSinparametros(cls):
        marca = "Chevrolet"
        modelo = "Camaro"
        anio = date.today().year
        kilometraje = 10000
        return cls(marca,modelo,anio,kilometraje)
    
    @staticmethod
    def validarKm(auto1,auto2):
        if auto1.kilometraje == auto2.kilometraje:
            return "Tienen el mismo kilometraje"
        else:
            return "No tienen el mismo kilometraje"
    
    @staticmethod
    def mayorKm(auto1,auto2):
        if auto1.kilometraje > auto2.kilometraje:
            return f"El auto {auto1.marca} tiene mayor kilometraje"
        elif auto1.kilometraje < auto2.kilometraje:
            return f"El auto {auto2.marca} tiene mayor kilometraje"