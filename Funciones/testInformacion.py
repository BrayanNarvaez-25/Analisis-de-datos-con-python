import llamadaInformacion

cantidadPacientes = int(input("Cuatos pacientes desea ingresar: "))

for i in range(cantidadPacientes):
    info = input(f"Ingrese el nombre, apellido y año de nacimiento del paciente {i+1}: ")
    llamadaInformacion.agregarNombre(info)
    llamadaInformacion.agregarEdad(info)

llamadaInformacion.calcularPersonas()