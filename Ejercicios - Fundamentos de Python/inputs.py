notaTarea = float(input("Ingresar la nota de la tarea: "))
notaLeccion = float(input("Ingresar la nota de la leccion: "))
notaExamen = float(input("Ingresar la nota de la examen: "))

totalProm = (notaTarea + notaLeccion + notaExamen) / 3

print(f"El promeedio es: {totalProm}")