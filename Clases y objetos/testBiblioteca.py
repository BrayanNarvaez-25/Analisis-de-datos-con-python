from biblioteca import Libro

libro1 = Libro("Cien años de soledad","Gabriel García Márquez",500)
libro1.mostrarInfo()

libro2 = Libro("1984","George Orwell",400)
libro3 = Libro("El código Da Vinci","Dan Brown",200)
print(f"\n{Libro.esGrande(libro2.paginas)}")
print(f"\nEl libro es grande: {Libro.esGrande(libro3.paginas)}")

print(f"\n{Libro.totalLibros()}")