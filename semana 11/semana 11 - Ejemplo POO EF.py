from abc import ABC, abstractmethod
class Evento(ABC):
    def __init__(self, nasistententes, catering, tipo):
        self._nasistentes = nasistententes
        self._catering = catering
        self._tipo = tipo
        self._precio_final = 0
    def get_tipo(self):
        return self._tipo
    def get__nasistentes(self):
        return self._nasistentes
    def get_precio_final(self):
        return self._precio_final
    @abstractmethod
    def calcula_precio(self):
        pass
    def mostrar_info(self):
        pass
class Infantil(Evento):
    def __init__(self, nasistentes, catering, tipo, payaso, tematica):
        super().__init__(nasistentes, catering, tipo)
        self.__payaso = payaso
        self.__tematica = tematica
        self.calcula_precio()
    def calcula_precio(self):
        precio = 300
        if self._nasistentes > 20:
            precio = precio+19*(self._nasistentes-20)
        if self.__payaso == "s":
            precio = precio + 400
        if self._catering == "s":
            precio = precio + 20*self._nasistentes
        self.__precio_final = precio
        return precio
    def mostrar_info(self):
        print(f"Evento: {self._tipo} Nasistentes: {self._nasistentes} Precio: {self.__precio_final}")
class Integrando(Evento):
    def __init__(self, nasistentes, catering, tipo, empresa):
        super().__init__(nasistentes, catering, tipo)
        self.__empresa = empresa
        self.calcula_precio()
    def calcula_precio(self):
        precio = 590
        if self._nasistentes > 20:
            precio = precio + 35*(self._nasistentes-20)
        if self._catering == "s":
            precio = precio + 20*self._nasistentes
        self.__precio_final = precio
        return precio
    def mostrar_info(self):
        print(f"Evento: {self._tipo} Nasistentes: {self._nasistentes} Precio: {self.__precio_final}")
class Cumpleaños(Evento):
    def __init__(self, nasistentes, catering, tipo, torta, bebida):
        super().__init__(nasistentes, catering, tipo)
        self.__torta = torta
        self.__bebida = bebida
        self.calcula_precio()
    def calcula_precio(self):
        precio = 400
        if self._nasistentes > 20:
            precio = precio+23*(self._nasistentes-20)
        if self.__torta == "s":
            precio = precio + 150
        if self.__bebida == "s":
            precio = precio + 10*self._nasistentes
        if self._catering == "s":
            precio = precio + 20*self._nasistentes
        self.__precio_final = precio
        return precio
    def mostrar_info(self):
        print(f"Evento: {self._tipo} Nasistentes: {self._nasistentes} Precio: {self.__precio_final}")
class Manejador:
    def __init__(self):
        self.__listaeventos=[]
    def agregar_evento(self, objevento):
        self.__listaeventos.append(objevento)
    def listar_evento(self):
        for evento in self.__listaeventos:
            evento.mostrar_info()
    def promedio_precio_infantil(self):
        suma = 0
        cont = 0
        for evento in self.__listaeventos:
            if evento.get_tipo() == "Infantil":
                suma = suma + evento.calcula_precio()
                cont += 1
                prom = suma/cont
        if cont > 0:
            print(f"El promedio de los precios infantil es: {prom}")
        else:
            print("No hay eventos infantiles para calular el promedio")
    def precio_mayor(self):
        mayor = 0
        for precio in self.__listaeventos:
            if precio.calcula_precio() > mayor:
                mayor = precio.calcula_precio()
                mayor.mostrar_info()
    def ordenar_eventos(self):
        dic = {}
        for evento in self.__listaeventos:
            dic[evento.calcula_precio()] = [evento.get_tipo(), evento.get_nasistentes()]
            dic_ord = sorted(dic.items())
            print(dic_ord)
#Programa principal
objman = Manejador()
opc = -1
while opc!=6:
    print("1. Agregar evento")
    print("2. Mostrar eventos")
    print("3. Promedio precio infantil")
    print("4. Precio mayor")
    print("5. Eventos ordenados")
    print("6. Salir")
    opc = int(input("Ingrese una opcion: "))
    match opc:
        case 1:
            tipo = input("Ingrese el tipo de evento: ")
            nasistentes = int(input("Ingrese la cantidad de asistentes: "))
            catering = input("Ingrese si desea catering (s n): ")
            if tipo == "Infantil":
                payaso = input("Ingrese si desea payaso (s n): ")
                tematica = input("Ingrese la tematica: ")
                obj = Infantil(nasistentes, catering, tipo, payaso, tematica)
            if tipo == "Integrando":
                empresa = input("Ingrese la empresa: ")
                obj = Integrando(nasistentes, catering, tipo, empresa)
            if tipo == "Cumpleaños":
                torta = input("Ingrese si desea torta (s n): ")
                bebida = input("Ingrese si desea bebida (s n): ")
                obj = Cumpleaños(nasistentes, catering, tipo, torta, bebida)
            objman.agregar_evento(obj)
        case 2:
            objman.listar_evento()
        case 3:
            objman.promedio_precio_infantil()
        case 4:
            objman.precio_mayor()
        case 5:
            objman.ordenar_eventos()
