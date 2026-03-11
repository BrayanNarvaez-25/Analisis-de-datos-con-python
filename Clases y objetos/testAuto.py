from auto import auto

for num in range(1,11):
    autoNuevo = auto.crearAuto("Supra")
    print(autoNuevo.__dict__)

auto1 = auto("Chevrolet","Camaro",2026,100)
auto2 = auto("Chevrolet","Camaro",2026,100)
print(f"\n----{auto.validarKm(auto1,auto2)}")

auto3 = auto("Toyota","Supra",2026,100)
auto4 = auto("Chevrolet","Camaro",2026,200)
print(f"\n----{auto.validarKm(auto3,auto4)}")

auto5 = auto.crearAutoSinparametros()
print(f"\nAuto nuevo: {auto5.__dict__}")

auto6 = auto("Toyota","Supra",2026,600)
auto7 = auto("Chevrolet","Camaro",2026,200)

print(f"\n{auto.mayorKm(auto3,auto4)}")
print(f"\n{auto.mayorKm(auto6,auto7)}")