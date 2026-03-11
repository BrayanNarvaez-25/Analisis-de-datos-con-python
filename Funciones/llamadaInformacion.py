nombrePaciente = []
edad = []

#split separa cadenas y join une cadenas
#partes[:-1] toma todos los valores menos el ultimo

def agregarNombre(nombre):
    partes = nombre.split()
    nombreCompleto = " ".join(partes[:-1])
    nombrePaciente.append(nombreCompleto)

def agregarEdad(anio):
    anioN = int(anio.split()[-1])
    anioA = 2026
    edadA = anioA - anioN
    edad.append(edadA)

def calcularPersonas():
    edadMayor = max(edad)
    personaMayor = nombrePaciente[edad.index(edadMayor)]

    edadMenor = min(edad)
    personaMenor = nombrePaciente[edad.index(edadMenor)]

    print(f"{personaMayor} con la edad de {edadMayor} es mayor a los demás pacientes")
    print(f"{personaMenor} con la edad de {edadMenor} es menor a los demás pacientes")