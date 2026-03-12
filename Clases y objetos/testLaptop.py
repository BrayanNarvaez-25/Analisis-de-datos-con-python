from laptop import laptop
from laptopGaming import laptopGaming
from laptopBusiness import laptopBusiness

def imprimirInforme(laptop):
    informe = laptop.realizarInformeUso()
    for clave, valor in informe.items():
        print(f"{clave} : {valor}")
    print("\n")

laptopPepito = laptop("Lenovo","i7",32)
laptopMaria = laptop("Lenovo","i7",32, 600)
laptopJuanito = laptopGaming("MSI","i7",4,"RTX 8GB")
laptopPedrito = laptopBusiness("Dell", "i7", 16, 512, 12)

print("PEPITO: ")
imprimirInforme(laptopPepito)
print("JUANITO: ")
imprimirInforme(laptopJuanito)
print("PEDRITO: ")
imprimirInforme(laptopPedrito)