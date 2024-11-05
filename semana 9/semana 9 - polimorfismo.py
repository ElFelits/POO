#POO POLIMORFISMO  cuando hay metodo abstracto y NO se va a instanciar un objeto de la clase padre
#A) imprimir las areas
from abc import ABC, abstractmethod
class Figura(ABC):
    def __init__(self, tipo):
        self._tipo = tipo      #Atributo compartido protected/protegido
    def get_tipo(self):        #Herencia metodo compartido
        return self._tipo
    @abstractmethod
    def area(self):            #Poliformismo hay un metodo abstracto que TODOS los hijos deben tener
        pass

class Triangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Triangulo")
        self.__base = base
        self.__altura = altura
    def area(self):
        return self.__base * self.__altura/2

class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__("Cuadrado")
        self.__lado = lado
    def area(self):
        return self.__lado ** 2

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Circulo")
        self.__radio = radio
    def area(self):
        return 3.1415 * self.__radio**2

#Programa principal
objTri1 = Triangulo(5, 7)
objTri2 = Triangulo(4, 10)
objcua = Cuadrado(4)
objcir = Circulo(3)
#Todos los lenguajes
#B) promedio de las areas de los triángulos
lista = [objTri1, objTri2, objcua, objcir] #solo se puede si hay polimorfismo
suma = 0
cont = 0
for obj in lista:
   if obj.get_tipo() == "Triangulo":
       suma += obj.area()
       cont += 1
print(f"Promedio: {suma/cont}")
