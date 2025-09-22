import math

class Calculadora:
    def __init__(self, numero):
        self.numero = numero

    def raiz_cuadrada(self):
        if self.numero < 0:
            return "Error: No se puede calcular la raíz de un número negativo."
        return math.sqrt(self.numero)

    def potencia(self, exponente):
        try:
            return self.numero ** float(exponente)
        except ValueError:
            return "Error: El exponente debe ser un número válido."
