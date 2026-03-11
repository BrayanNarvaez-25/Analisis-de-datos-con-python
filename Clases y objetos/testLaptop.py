from laptop import laptop

laptopPepito = laptop("Lenovo","i7",32)
laptopMaria = laptop("Lenovo","i7",32, 600)

for numero in range(1,1001):
    asusLaptop = laptop.asusLaptop(numero)
    print(asusLaptop.__dict__)

# print(laptop.compararCosto(laptopPepito,laptopMaria))