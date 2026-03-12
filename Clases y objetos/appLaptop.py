from laptopGaming import laptopGaming
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

class App:
    def __init__(self, root):
        self.root = root
        self.laptops = []
        self.imagenesG = [
            "C:\\Users\\gaton\\OneDrive\\Documentos\\Programación_Brayann\\Modulo 4\\An-lisis-de-datos-con-python\\Clases y objetos\\imgLaptops\\1.png",
            "C:\\Users\\gaton\\OneDrive\\Documentos\\Programación_Brayann\\Modulo 4\\An-lisis-de-datos-con-python\\Clases y objetos\\imgLaptops\\2.png",
            "C:\\Users\\gaton\\OneDrive\\Documentos\\Programación_Brayann\\Modulo 4\\An-lisis-de-datos-con-python\\Clases y objetos\\imgLaptops\\3.png",
            "C:\\Users\\gaton\\OneDrive\\Documentos\\Programación_Brayann\\Modulo 4\\An-lisis-de-datos-con-python\\Clases y objetos\\imgLaptops\\4.png",
            "C:\\Users\\gaton\\OneDrive\\Documentos\\Programación_Brayann\\Modulo 4\\An-lisis-de-datos-con-python\\Clases y objetos\\imgLaptops\\5.png"                            
        ]
        self.imagenesB = [
            "C:\\Users\\gaton\\OneDrive\\Documentos\\Programación_Brayann\\Modulo 4\\An-lisis-de-datos-con-python\\Clases y objetos\\imgLaptops\\6.png",
            "C:\\Users\\gaton\\OneDrive\\Documentos\\Programación_Brayann\\Modulo 4\\An-lisis-de-datos-con-python\\Clases y objetos\\imgLaptops\\7.png",
            "C:\\Users\\gaton\\OneDrive\\Documentos\\Programación_Brayann\\Modulo 4\\An-lisis-de-datos-con-python\\Clases y objetos\\imgLaptops\\8.png",
            "C:\\Users\\gaton\\OneDrive\\Documentos\\Programación_Brayann\\Modulo 4\\An-lisis-de-datos-con-python\\Clases y objetos\\imgLaptops\\9.png",
            "C:\\Users\\gaton\\OneDrive\\Documentos\\Programación_Brayann\\Modulo 4\\An-lisis-de-datos-con-python\\Clases y objetos\\imgLaptops\\10.png"                            
        ]

        root.title("Gestión de Laptops")

        # --- MENU SUPERIOR ---
        self.menuSuperior = tk.Frame(self.root)
        self.menuSuperior.grid(row=0, column=0, columnspan=2)
        
        tk.Button(self.menuSuperior, text="Gamer", command=self.verGamer).pack(side="left")
        tk.Button(self.menuSuperior, text="Business", command=self.verBusiness).pack(side="left")

        # --- CONTENEDORES ---
        self.frameGamer = tk.Frame(self.root)
        self.frameBusiness = tk.Frame(self.root)

        self.setupGamer()
        self.setupBusiness()

        # Iniciar vista gamer por defecto
        self.verGamer()

    def setupGamer(self):
        ttk.Label(self.frameGamer, text="Marca").grid(row=0, column=0)
        self.marcaG = tk.StringVar()
        ttk.Entry(self.frameGamer, textvariable=self.marcaG).grid(row=0, column=1)

        ttk.Label(self.frameGamer, text="Procesador").grid(row=1, column=0)
        self.procesadorG = tk.StringVar()
        ttk.Entry(self.frameGamer, textvariable=self.procesadorG).grid(row=1, column=1)

        ttk.Label(self.frameGamer, text="Memoria").grid(row=2, column=0)
        self.memoriaG = tk.StringVar()
        ttk.Entry(self.frameGamer, textvariable=self.memoriaG).grid(row=2, column=1)

        ttk.Label(self.frameGamer, text="Tarjeta Gráfica").grid(row=3, column=0)
        self.tarjetaGraficaG = tk.StringVar()
        ttk.Entry(self.frameGamer, textvariable=self.tarjetaGraficaG).grid(row=3, column=1)

        ttk.Label(self.frameGamer, text="Precio").grid(row=4, column=0)
        self.precioG = tk.StringVar()
        ttk.Entry(self.frameGamer, textvariable=self.precioG).grid(row=4, column=1)

        ttk.Button(self.frameGamer, text="Agregar Laptop", command=self.agregarLaptopG).grid(row=5, column=0)

        self.mostrarLaptopsG = tk.Text(self.frameGamer, height=10, width=50)
        self.mostrarLaptopsG.grid(row=6, column=0, columnspan=2)

        self.canvaGamer = tk.Canvas(self.frameGamer, width=200, height=200)
        self.canvaGamer.grid(row=1, column=3, rowspan=6)

    def setupBusiness(self):
        ttk.Label(self.frameBusiness, text="Marca").grid(row=0, column=0)
        self.marcaB = tk.StringVar()
        ttk.Entry(self.frameBusiness, textvariable=self.marcaB).grid(row=0, column=1)

        ttk.Label(self.frameBusiness, text="Procesador").grid(row=1, column=0)
        self.procesadorB = tk.StringVar()
        ttk.Entry(self.frameBusiness, textvariable=self.procesadorB).grid(row=1, column=1)

        ttk.Label(self.frameBusiness, text="Memoria").grid(row=2, column=0)
        self.memoriaB = tk.StringVar()
        ttk.Entry(self.frameBusiness, textvariable=self.memoriaB).grid(row=2, column=1)

        ttk.Label(self.frameBusiness, text="Almacenamiento").grid(row=3, column=0)
        self.almacenamientoB = tk.StringVar()
        ttk.Entry(self.frameBusiness, textvariable=self.almacenamientoB).grid(row=3, column=1)

        ttk.Label(self.frameBusiness, text="Duración de Batería").grid(row=4, column=0)
        self.duracionBateriaB = tk.StringVar()
        ttk.Entry(self.frameBusiness, textvariable=self.duracionBateriaB).grid(row=4, column=1)

        ttk.Label(self.frameBusiness, text="Precio").grid(row=5, column=0)
        self.precioB = tk.StringVar()
        ttk.Entry(self.frameBusiness, textvariable=self.precioB).grid(row=5, column=1)

        ttk.Button(self.frameBusiness, text="Agregar Laptop", command=self.agregarLaptopB).grid(row=6, column=0)

        self.mostrarLaptopsB = tk.Text(self.frameBusiness, height=10, width=50)
        self.mostrarLaptopsB.grid(row=7, column=0, columnspan=2)

        self.canvaBusiness = tk.Canvas(self.frameBusiness, width=200, height=200)
        self.canvaBusiness.grid(row=0, column=3, rowspan=8)

    def verGamer(self):
        self.frameBusiness.grid_forget()
        self.frameGamer.grid(row=1, column=0)

    def verBusiness(self):
        self.frameGamer.grid_forget()
        self.frameBusiness.grid(row=1, column=0)

    def agregarLaptopG(self):
        nuevaLaptop = laptopGaming(
            self.marcaG.get(),
            self.procesadorG.get(),
            self.memoriaG.get(),
            self.tarjetaGraficaG.get(),
            self.precioG.get()
        )
        self.laptops.append(nuevaLaptop)
        self.mostrarLaptopsG.insert(tk.END, f"{nuevaLaptop}\n")
        self.mostrarImagenAleatoriasG()

    def agregarLaptopB(self):
        nuevaLaptop = laptopGaming(
            self.marcaB.get(),
            self.procesadorB.get(),
            self.memoriaB.get(),
            self.duracionBateriaB.get(),
            self.precioB.get()
        )
        self.laptops.append(nuevaLaptop)
        self.mostrarLaptopsB.insert(tk.END, f"{nuevaLaptop}\n")
        self.mostrarImagenAleatoriasB()

    def mostrarImagenAleatoriasG(self):
        imagenPath = random.choice(self.imagenesG)
        imagen = Image.open(imagenPath)
        imagen = imagen.resize((200, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(imagen)

        self.canvaGamer.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvaGamer.image = photo
    
    def mostrarImagenAleatoriasB(self):
        imagenPath = random.choice(self.imagenesB)
        imagen = Image.open(imagenPath)
        imagen = imagen.resize((200, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(imagen)

        self.canvaBusiness.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvaBusiness.image = photo

root = tk.Tk()
app = App(root)
root.mainloop()