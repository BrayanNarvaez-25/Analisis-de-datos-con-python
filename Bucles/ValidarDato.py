print("PROGRAMA PARA VALIDAR DATOS")

datos = []

numDatos = int(input("¿Cuantos datos quiere ingresar?: "))

for i in range(numDatos):
    dato = input(f"Ingrese el dato {i+1}: ")
    if dato.isdigit():
        valor = int(dato)
    elif "." in dato and dato.replace(".","",1).isdigit():
        valor = float(dato)
    else:
        valor = str(dato)
    
    datos.append(valor)

print(f"Su lista es: {datos}")