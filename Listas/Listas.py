#Listas

planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]

# print(planetas[-3])
# print(planetas[2:])
# print(len(planetas))

#TRABAJAR CON UNA LISTA DE NÚMEROS
gravedadPlanetas = [3.7, 8.87, 9.81, 3.71, 24.79, 10.44, 8.69, 11.15]
pesoBus = 124054 #Newtons

print(f"En la Tierra, un autobús de dos pisos pesa {pesoBus} N")
print(f"En Mercurio, un autobús de dos pisos pesa {pesoBus*gravedadPlanetas[0]} N")

print(f"Lo más liviano que seria un autobus en el sistema solar es {pesoBus*min(gravedadPlanetas)} N")
print(f"Lo más pesado que seria un autobus en el sistema solar es {pesoBus*max(gravedadPlanetas)} N")