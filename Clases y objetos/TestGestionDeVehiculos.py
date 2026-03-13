from GestionDeVehiculos import Vehiculo,Auto,Moto

auto = Auto("Chevrolet","Camaro",2025,4)
auto.descripcion()

moto = Moto("Kawazaki","Ninja",2025,"deportiva")
moto.descripcion()

auto1 = Auto("Toyota", "Corolla", 2024, 4)
auto2 = Auto("Honda", "Civic", 2023, 4)
moto1 = Moto("Yamaha", "MT-07", 2022, "deportiva")
moto2 = Moto("Vespa", "Primavera", 2024, "scooter")

vehiculos = [auto,auto1,auto,moto,moto1,moto2]

for v in vehiculos:
    v.descripcion()