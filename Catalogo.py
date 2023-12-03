# Catalogo.py

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self):
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        self.productos.append({"nombre": nombre, "precio": precio})

    def mostrar_productos(self):
        print("Catálogo de productos:")
        for producto in self.productos:
            print(f"{producto['nombre']}: ${producto['precio']}")

