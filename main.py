# main.py

from Circulo import Circulo
from Catalogo import Catalogo
from Operaciones import dividir_numeros
from Producto import Producto
from Phone import Phone
import os

if __name__ == '__main__':
    # Problema 01:
    print("=================================================================")
    print("EJERCICIO 01: CALCULAR EL ÁREA DE UN CIRCULO A TRAVÉS DE SU RADIO")

    circulo = Circulo()
    print(f"Área del círculo: {circulo.calcular_area()}")

    # Problema 02:
    print("=================================================================")
    print("EJERCICIO 02: CATÁLOGO Y LISTA DE PRODUCTOS")

    catalogo = Catalogo()
    catalogo.agregar_producto()
    catalogo.mostrar_productos()

    # Problema 03:
    print("=================================================================")
    print("EJERCICIO 03: MENÚ INTERACTIVO - DIVISIÓN DE DOS NÚMEROS")
    dividir_numeros()

    # Problema 04:
    print("=================================================================")
    print("EJERCICIO 04: PAÍS, LOTE Y AÑO DE UN PRODUCTO")
    producto = Producto()
    print(producto)

    # Problema 05:
    print("=================================================================")
    print("EJERCICIO 05: NUEVO MÉTODO PARA LA CLASE PHONE")
    phone = Phone("Samsung", "Galaxy S21")
    phone.encender_apagar()
    phone.perfil()
    phone.llamar("123456789")
    phone.acceder()

    # Problema 06:
    print("=================================================================")
    print("EJERCICIO 05: INSTANCIAR DATOS DESDE EL TECLADO")
    class Persona:
        def __init__(self):
            self.nombre = input("Ingrese el nombre: ")
            self.edad = input("Ingrese la edad: ")

    persona = Persona()
    print(f"Persona creada: {persona.nombre}, {persona.edad} años.")
