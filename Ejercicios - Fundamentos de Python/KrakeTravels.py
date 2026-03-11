print("¡¡¡VIAJA CON KRAKETRAVELS!!!")
print("\nAseguremonos que viajas segur@ :)")

print("\n1.- Ecuador \n2.- Colombia \n3.- Perú")
destino = int(input("Ingrese el número de su destino: "))

print("\n1.- Zona urbana \n2.- Zona rural \n3.- Zona perimetral")
zona = int(input("Ingrese el número de su zona: "))

velocidad = float(input("\nIngrese la velocidad a la que viaja (km/h): "))

if destino == 1:
    if zona == 1:
        if velocidad > 50:
            print("\nMuy rápido!! - Disminuye la velocidad")
        elif velocidad > 0 and velocidad < 10:
            print("\nEsta yendo muy lento - Puede acelerar")
        elif velocidad >= 10 and velocidad <= 50: 
            print("\nEstá en el rango adecuado - Viaje seguro")
        else:
            print("\nSea serio... No se ha movido (velocidad 0)")
    if zona == 2:
        if velocidad > 70:
            print("\nMuy rápido!! - Disminuye la velocidad")
        elif velocidad > 0 and velocidad < 51:
            print("\nEsta yendo muy lento - Puede acelerar")
        elif velocidad >= 51 and velocidad <= 70: 
            print("\nEstá en el rango adecuado - Viaje seguro")
        else:
            print("\nSea serio... No se ha movido (velocidad 0)")
    if zona == 3:
        if velocidad > 90:
            print("\nMuy rápido!! - Disminuye la velocidad")
        elif velocidad > 0 and velocidad < 71:
            print("\nEsta yendo muy lento - Puede acelerar")
        elif velocidad >= 71 and velocidad <= 90: 
            print("\nEstá en el rango adecuado - Viaje seguro")
        else:
            print("\nSea serio... No se ha movido (velocidad 0)")

if destino == 2:
    if zona == 1:
        if velocidad > 30:
            print("\nMuy rápido!! - Disminuye la velocidad")
        elif velocidad > 0 and velocidad < 10:
            print("\nEsta yendo muy lento - Puede acelerar")
        elif velocidad >= 10 and velocidad <= 30: 
            print("\nEstá en el rango adecuado - Viaje seguro")
        else:
            print("\nSea serio... No se ha movido (velocidad 0)")
    if zona == 2:
        if velocidad > 80:
            print("\nMuy rápido!! - Disminuye la velocidad")
        elif velocidad > 0 and velocidad < 31:
            print("\nEsta yendo muy lento - Puede acelerar")
        elif velocidad >= 31 and velocidad <= 80: 
            print("\nEstá en el rango adecuado - Viaje seguro")
        else:
            print("\nSea serio... No se ha movido (velocidad 0)")
    if zona == 3:
        if velocidad > 100:
            print("\nMuy rápido!! - Disminuye la velocidad")
        elif velocidad > 0 and velocidad < 81:
            print("\nEsta yendo muy lento - Puede acelerar")
        elif velocidad >= 81 and velocidad <= 100: 
            print("\nEstá en el rango adecuado - Viaje seguro")
        else:
            print("\nSea serio... No se ha movido (velocidad 0)")

if destino == 3:
    if zona == 1:
        if velocidad > 40:
            print("\nMuy rápido!! - Disminuye la velocidad")
        elif velocidad > 0 and velocidad < 10:
            print("\nEsta yendo muy lento - Puede acelerar")
        elif velocidad >= 10 and velocidad <= 40: 
            print("\nEstá en el rango adecuado - Viaje seguro")
        else:
            print("\nSea serio... No se ha movido (velocidad 0)")
    if zona == 2:
        if velocidad > 60:
            print("\nMuy rápido!! - Disminuye la velocidad")
        elif velocidad > 0 and velocidad < 41:
            print("\nEsta yendo muy lento - Puede acelerar")
        elif velocidad >= 41 and velocidad <= 60: 
            print("\nEstá en el rango adecuado - Viaje seguro")
        else:
            print("\nSea serio... No se ha movido (velocidad 0)")
    if zona == 3:
        if velocidad > 120:
            print("\nMuy rápido!! - Disminuye la velocidad")
        elif velocidad > 0 and velocidad < 61:
            print("\nEsta yendo muy lento - Puede acelerar")
        elif velocidad >= 61 and velocidad <= 120: 
            print("\nEstá en el rango adecuado - Viaje seguro")
        else:
            print("\nSea serio... No se ha movido (velocidad 0)")
