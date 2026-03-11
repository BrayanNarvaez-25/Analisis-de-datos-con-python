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

laptopPepito = laptop("Lenovo","i7",32)

print(laptopPepito.__dict__)
print(laptopPepito.valorFinal())
print(f"El valor de descuento es: {laptopPepito.valorDescuento(10)}")