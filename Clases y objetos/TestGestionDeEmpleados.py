from GestionDeEmpleados import Empleado,EmpleadoMedioTiempo,EmpleadoTiempoCompleto

empleado1 = EmpleadoTiempoCompleto("Carlos Ruiz", 1200.0)
empleado2 = EmpleadoMedioTiempo("Elena Gómez", 800.0)

print(empleado1.calcularSalario())
print(empleado2.calcularSalario())

empleado3 = EmpleadoTiempoCompleto("Beatriz Viteri", 1500.0)
empleado4 = EmpleadoTiempoCompleto("Roberto Solís", 1800.0)
empleado5 = EmpleadoMedioTiempo("Marta Roldán", 950.0)
empleado6 = EmpleadoMedioTiempo("Jorge Icaza", 1100.0)

empleados = [empleado1,empleado2,empleado3,empleado4,empleado5,empleado6]

print("\n")

for e in empleados:
    print(f"\nEmpleado: {e.nombre}")
    print(e.calcularSalario())