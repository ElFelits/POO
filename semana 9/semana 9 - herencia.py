#POO HERENCIA  cuando hay un atributo o metodo comun que puede ser heredado y así eliminar la redundancia
#A) imprimir las areas
class Figura:
    def __init__(self, tipo):
        self._tipo = tipo      #Atributo compartido protected/protegido
    def get_tipo(self):        #Herencia metodo compartido
        return self._tipo

class Triangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Triangulo")
        self.__base = base
        self.__altura = altura
    def area(self):
        return f"Area: {self.__base * self.__altura/2}"

class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__("Cuadrado")
        self.__lado = lado
    def area(self):
        return f"Area: {self.__lado ** 2}"

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Circulo")
        self.__radio = radio
    def area(self):
        return f"Area: {3.1415 * self.__radio**2}"

#Programa principal
objTri1 = Triangulo(5, 7)
objTri2 = Triangulo(4, 10)
objcua = Cuadrado(4)
objcir = Circulo(3)
#Otro lenguaje o python
lista_tri = [objTri1, objTri2]
lista_cua = [objcua]
lista_cir = [objcir]
#B) promedio de las areas de los triángulos
suma = 0
for obj in lista_tri:
    suma += obj.area()
print(f"Promedio: {suma/len(lista_tri)}")

#truco de python
#B) promedio de las areas de los triángulos
lista = [objTri1, objTri2, objcua, objcir]
suma = 0, cont = 0
for obj in lista:
   if obj.get_tipo() == "Triangulo":
       suma += obj.area()
       cont += 1
print(f"Promedio: {suma/cont}")
