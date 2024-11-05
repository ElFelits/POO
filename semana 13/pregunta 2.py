from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, tipo, marca, material, transmision, cilindrada, precio_base):
        self._tipo = tipo
        self._marca = marca
        self._material = material
        self._transmision = transmision
        self._cilindrada = cilindrada
        self._precio_base = precio_base
    @abstractmethod
    def calcular_precio_final(self):
        pass
    @abstractmethod
    def imprimir_info(self):
        pass

class Sedan(Auto):
    def __init__(self, marca, material, transmision, cilindrada, suspension):
        super().__init__("Sedan", marca, material, transmision, cilindrada, 40000)
        self.__suspension = suspension
    def calcular_precio_final(self):
        costos_suspension = {"posterior": 1400, "delantera": 1500, "doble": 1800}
        precio_final = self._precio_base + costos_suspension.get(self.__suspension, 0)
        return precio_final
    def imprimir_info(self):
        print(f"Tipo: {self._tipo}, Marca: {self._marca}, Material: {self._material}, "
              f"Transmisión: {self._transmision}, Cilindrada: {self._cilindrada} cc, Precio Final: S/ {self.calcular_precio_final()}")

class Hatchback(Auto):
    def __init__(self, marca, material, transmision, cilindrada, tiempo_encender):
        super().__init__("Hatchback", marca, material, transmision, cilindrada, 44000)
        self.__tiempo_encender = tiempo_encender
    def calcular_precio_final(self):
        if self.__tiempo_encender == 2:
            return self._precio_base * 1.2
        elif self.__tiempo_encender == 4:
            return self._precio_base * 1.1
        else:
            return self._precio_base
    def imprimir_info(self):
        print(f"Tipo: {self._tipo}, Marca: {self._marca}, Material: {self._material}, "
              f"Transmisión: {self._transmision}, Cilindrada: {self._cilindrada} cc, Precio Final: S/ {self.calcular_precio_final()}")

class Convertible(Auto):
    def __init__(self, marca, material, transmision, cilindrada, tiene_maletera):
        super().__init__("Convertible", marca, material, transmision, cilindrada, 50000)
        self.__tiene_maletera = tiene_maletera
    def calcular_precio_final(self):
        costo_maletera = 0
        if self.__tiene_maletera == True:
            costo_maletera = 5000 
        precio_final = self._precio_base + costo_maletera
        return precio_final
    def imprimir_info(self):
        print(f"Tipo: {self._tipo}, Marca: {self._marca}, Material: {self._material}, "
              f"Transmisión: {self._transmision}, Cilindrada: {self._cilindrada} cc, Precio Final: S/ {self.calcular_precio_final()}")

class GestorAutos:
    def __init__(self):
        self.__autos_registrados = []
    def registrar_auto(self, auto):
        self.__autos_registrados.append(auto)
    def listar_autor_por_precio(self):
        autos_ordenados = sorted(self.__autos_registrados, key = lambda auto: auto.calcular_precio_final(), reverse = True)
        for auto in autos_ordenados:
            auto.imprimir_info()
    def mostrar_auto_menor_mayor_precio(self):
        auto_menor_precio = min(self.__autos_registrados, key = lambda auto: auto.calcular_precio_final())
        auto_mayor_precio = max(self.__autos_registrados, key = lambda auto: auto.calcular_precio_final())
        print("Auto con menor precio final: ")
        auto_menor_precio.imprimir_info()
        print("\nAuto con mayor precio final: ")
        auto_mayor_precio.imprimir_info()
    def mostrar_autos_por_tipo(self, tipo):
        autos_tipo = [auto for auto in self.__autos_registrados if auto._tipo == tipo]
        autos_ordenados = sorted(autos_tipo, key = lambda auto: auto.calcular_precio_final(), reverse = True)
        for auto in autos_ordenados:
            auto.imprimir_info()

#Programa principal
objgest = GestorAutos()
auto1 = Sedan("Toyota", "Aluminio", "Automática", 2000, "posterior")
auto2 = Sedan("Honda", "Hierro", "Mecánica", 2500, "doble")
auto3 = Hatchback("Ford", "Aluminio", "Eléctrico", 1500, 2)
auto4 = Hatchback("Nissan", "Hierro", "Automática", 1800, 4)
auto5 = Convertible("BMW", "Hierro", "Automática", 3000, True)
auto6 = Convertible("Audi", "Aluminio", "Mecánica", 3500, False)

objgest.registrar_auto(auto1)
objgest.registrar_auto(auto2)
objgest.registrar_auto(auto3)
objgest.registrar_auto(auto4)
objgest.registrar_auto(auto5)
objgest.registrar_auto(auto6)

opc = -1
while opc!= 4:
    print("\nReportes")
    print("1. Lista de autos ordenados por precio final")
    print("2. Auto con menor y mayor precio final")
    print("3. Autos de x tipo ordenados por precio")
    print("4. Salir")
    opc = int(input("Ingrese una opcion: "))
    match opc:
        case 1:
            objgest.listar_autor_por_precio()
        case 2:
            objgest.mostrar_auto_menor_mayor_precio()
        case 3:
            tipo = input("Ingrese el tipo de auto (Sedan, Hatchback, Convertible): ")
            objgest.mostrar_autos_por_tipo(tipo)
