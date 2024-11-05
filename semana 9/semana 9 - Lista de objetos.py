#POO Lista de objetos
#A) imprimir las areas
class Triangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura
    def area(self):
        print(f"Area: {self.__base * self.__altura/2}")

class Cuadrado:
    def __init__(self, lado):
        self.__lado = lado
    def area(self):
        print(f"Area: {self.__lado ** 2}")

class Circulo:
    def __init__(self, radio):
        self.__radio = radio
    def area(self):
        print(f"Area: {3.1415 * self.__radio**2}")

#Programa principal
objTri1 = Triangulo(5, 7)
objTri2 = Triangulo(4, 10)
objcua = Cuadrado(4)
objcir = Circulo(3)
#otro lenguaje o python
lista_tri = [objTri1, objTri2]
lista_cua = [objcua]
lista_cir = [objcir]
for obj in lista_tri:
    obj.area()
for obj in lista_cua:
    obj.area()
for obj in lista_cir:
    obj.area()
#truco de python
lista = [objTri1, objTri2, objcua, objcir]
for obj in lista:
    obj.area()
