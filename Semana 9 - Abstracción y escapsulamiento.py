class Figura:
    def __init__(self, tipo):
        self._tipo = tipo
class Triangulo(Figura):
    def __init__(self, tam, tipo):
        super().__init__(tipo)
        self.__tam = tam
    def dibujar(self):
        for fila in range(self.__tam):
            for columna in range(fila+1):
                print("*", end = " ")
            print()
class Cuadrado(Figura):
    def __init__(self, tam, tipo):
        super().__init__(tipo)
        self.__tam = tam
    def dibujar(self):
        for fila in range(1, self.__tam + 1):
            for columna in range(1, self.__tam + 1):
                print("*", end = " ")
            print()
objT1 = Triangulo(5, "T") #El primer dato pertenece al hijo y el segundo al padre
objT1.dibujar()
print()
objC1 = Cuadrado(7, "C")
objC1.dibujar()
