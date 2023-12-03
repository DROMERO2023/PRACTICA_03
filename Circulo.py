# Circulo.py

import math

class Circulo:
    def __init__(self):
        self.radio = float(input("Ingrese el radio del círculo: "))

    def calcular_area(self):
        return math.pi * self.radio**2
