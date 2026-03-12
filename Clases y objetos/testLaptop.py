from laptop import laptop
from laptopGaming import laptopGaming
from laptopBusiness import laptopBusiness

laptopPepito = laptop("Lenovo","i7",32)
laptopMaria = laptop("Lenovo","i7",32, 600)

laptopJuanito = laptopGaming("MSI","i7",4,"RTX 8GB")

print(laptopJuanito.ralizarDiagnosticoSistema())

laptopPedrito = laptopBusiness("Dell", "i7", 16, 512, 12)
print(f"\n{laptopPedrito.ralizarDiagnosticoSistema()}")