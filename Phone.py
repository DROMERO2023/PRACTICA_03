# Phone.py

class Phone:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.estado = 'Apagado'

    def encender_apagar(self):
        if self.estado == 'Apagado':
            self.estado = 'Encendido'
            print("Teléfono encendido.")
        else:
            self.estado = 'Apagado'
            print("Teléfono apagado.")

    def perfil(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nEstado: {self.estado}")

    def llamar(self, numero):
        if self.estado == 'Encendido':
            print(f"Llamando al número {numero}.")
        else:
            print("El teléfono está apagado. Enciéndelo para realizar una llamada.")

    def acceder(self):
        if self.estado == 'Encendido':
            print("Accediendo al menú principal.")
        else:
            print("El teléfono está apagado. Enciéndelo para acceder al menú.")
