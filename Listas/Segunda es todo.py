print("BIENVENID@ A SEGUNDA ES TODO ")

menu = ["Encebollado", "Locro de papa", "Fritada", "Ceviche de camarón", "Llapingachos"]

print("\n¿QUE DESEA REALIZAR HOY?")

print("\nMENÚ DE OPCIONES \n1.- Añadir plato al menú  \n2.- Buscar en el menú  \n3.- Eliminar plato del menú  \n4.- Mostrar platos del menú")

accion = int(input("\nIngrese el número de lo que quiere hacer: "))


if accion == 1:
    añadir = input("\nIngrese el nombre del plato para añadir: ")
    menu.append(añadir)
    print(f"Se ha añadido con éxito \n{menu}")
elif accion == 2:
    buscar = input("\nIngrese el nombre del plato a buscar: ")
    if buscar in menu:
        print("Si existe ese plato en el menú")
    else:
        print("No existe es plato en el menú")
elif accion == 3:
    eliminar = input("\nIngrese el nombre del plato para eliminar: ")
    menu.remove(eliminar)
    print(f"Se ha eliminado correctamente \n{menu}")
elif accion == 4:
    print(f"\nNuestro menú: \n{menu}")