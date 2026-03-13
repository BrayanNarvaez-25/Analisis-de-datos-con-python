class Libro:

    contadorLibros = 0

    def __init__(self,titulo,autor,paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        Libro.contadorLibros += 1
    
    def mostrarInfo(self):
        print(f"\nLibro: {self.titulo} \nAutor: {self.autor} \nN.páginas: {self.paginas}")
    
    @staticmethod
    def esGrande(pagLibro):
        if  pagLibro > 300:
            return f"El libro es grande: {True}"
        else: 
            return f"El libro es grande: {False}"
    
    @classmethod
    def totalLibros(cls):
        return f"Total de libros: {cls.contadorLibros}"
        pass