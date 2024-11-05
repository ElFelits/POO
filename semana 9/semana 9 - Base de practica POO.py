class Triangulo:
    #Atributo de clase
    __pi = 3.1415
    #constructor
    def __init__(self, base, altura):
        #atributos de instancia
        self.__base = base
        self.__altura = altura
    #Metodo de acceso          instancia
    def get_base(self):
        return self.__base
    def set_base(self,base):
        self.__base = base
    #Metodo de operacion       instancia
    def area(self):
        return Triangulo.__pi*self.__base*self.__altura/2
    def mostrar_info(self):
        print(f"pi: {Triangulo.__pi}, base: {self.__base}, altura: {self.__altura} ")
    #Metodo de acceso       clase
    @classmethod
    def get_pi(cls):
        return cls.__pi
    @classmethod
    def set_pi(cls, pi):
        cls.__pi = pi

#Programa principal
b = -1
h = -1
while b < 0:
    try:
        b = float(input("Ingrese base: "))
    except: ValueError("Ingrese un valor valido")
while h < 0:
    try:
        h = float(input("Ingrese altura"))
    except: ValueError("Ingrese un valor valido")
objT1 = Triangulo(b, h)
objT1.mostrar_info()
print(f"Base: {objT1.get_base()}")
print(f"Pi: {Triangulo.get_pi()}")
print(f"Area: {objT1.area()}")
