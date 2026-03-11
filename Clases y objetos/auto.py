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

auto1 = auto("Chevrolet","Camaro",2025)

auto1.mostrarInfo()
auto1.actualizarKilometraje(100)
auto1.actualizarKilometraje(-100)
auto1.realizarViaje(100)
auto1.realizarViaje(-100)
auto1.estadoAuto()