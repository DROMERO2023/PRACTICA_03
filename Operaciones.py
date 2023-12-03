# Operaciones.py

def dividir_numeros():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 / num2
        print(f"Resultado de la división: {resultado}")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except ValueError:
        print("Error: Ingrese números válidos.")
