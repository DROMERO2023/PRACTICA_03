# Producto.py

class Producto:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del producto: ")
        self.codigo = input("Ingrese el código del producto (en formato PAIS-LOTE-AÑO): ")

    def __str__(self):
        pais, lote, anio = self.codigo.split('-')
        return f"Producto: {self.nombre}\nPaís: {pais}\nNúmero de lote: {lote}\nAño: {anio}"
