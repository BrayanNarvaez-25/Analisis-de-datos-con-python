import emoji

cantidadFrase = int(input("Cuatas frases desea ingresar: "))

for i in range(cantidadFrase):
    frase = input("Ingrese la frase: ")
    emoji.encontrarPalabra(frase)
    emoji.angregarFrase(frase)