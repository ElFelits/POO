from abc import ABC, abstractmethod

class Contacto(ABC):
    def __init__(self, nombre, numeros):
        self._nombre = nombre
        self._numeros = numeros
    @property
    def get_nombre(self):
        return self._nombre
    @property
    def get_numeros(self):
        return self._numeros
    @abstractmethod
    def mostrar_info(self):
        pass

class ContactoPersonal(Contacto):
    def __init__(self, nombre, numeros, cumpleaños):
        super().__init__(nombre, numeros)
        self.__cumpleaños = cumpleaños
    def mostrar_info(self):
        print(f"Nombre: {self._nombre}, numeros: {' , ' .join(self._numeros)}, cumpleaños {self.__cumpleaños}")

class ContactoProfesional(Contacto):
    def __init__(self, nombre, numeros, empresa):
        super().__init__(nombre, numeros)
        self.__empresa = empresa
    def mostrar_info(self):
        print(f"Nombre de personal: {self._nombre}, numeros: {' , ' .join(self._numeros)}, empresa: {self.__empresa}")

class Agenda:
    def __init__(self, tamaño = 10):
        self.__tamaño = tamaño
        self.__contactos = []
    def adicionar_contacto(self, contacto):
        if len(self.__contactos) >= self.__tamaño:
            print("La agenda esta llena. No se pueden añadir mas contactos")
        else: 
            for obj in self.__contactos:
                if obj.get_nombre == contacto.get_nombre:
                    print("Ya existe un contacto con este nombre")
                    break
            else:
                self.__contactos.append(contacto)
                print(f"Contacto {contacto.get_nombre} añadido")
    def listar_contactos(self):
        if len(self.__contactos) == 0:
            print("No hay contactos en la agenda")
        else:
            for contacto in self.__contactos:
                contacto.mostrar_info()
    def busca_contacto(self, nombre):
        for contacto in self.__contactos:
            if contacto.get_nombre == nombre:
                contacto.mostrar_info()
                break
        else:
            print("Contacto no encontrado")
    def eliminar_contacto(self, nombre):
        for i, contacto in enumerate(self.__contactos):
            if contacto.get_nombre == nombre:
                self.__contactos.pop(i)
            else:
                print("Contacto no encontrado")
    def agenda_llena(self):
        if len(self.__contactos) >= self.__tamaño:
            print("La agenda esta llena")
        else:
            print("La agenda no esta llena")
    def huecos_libres(self):
        print(f"Huecos libres: {self.__tamaño - len(self.__contactos)}")
#Programa principal
objage = Agenda()
opc = -1
while opc!= 7:
    print("\n--- Menú de Agenda ---")
    print("1. Adicionar contacto")
    print("2. Listar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Verificar si la Agenda esta llena")
    print("6. Ver huecos libres")
    print("7. Salir")
    opc = int(input("Ingrese una opcion: "))
    match opc:
        case 1:
            numeros = []
            Tcontacto = input("Indique si el contacto es Personal o Profesional: ")
            if Tcontacto.lower() == "personal":
                nombre = input("Ingrese el nombre del contacto: ")
                while len(numeros) < 1 or len(numeros) > 3:
                    numeros = input("Ingrese los numeros de telefono (separados por coma): ").split(',')
                cumpleaños = input("Ingrese la fecha de cumpleaños: ")
                contacto = ContactoPersonal(nombre, numeros, cumpleaños)
                objage.adicionar_contacto(contacto) 
            elif Tcontacto.lower() == "profesional":
                nombre = input("Ingrese el nombre del contacto: ")
                while len(numeros) < 1 or len(numeros) > 3:
                    numeros = input("Ingrese los numeros de telefono (separados por coma): ").split(',')
                empresa = input("Ingrese el nombre de la empresa: ")
                contacto = ContactoProfesional(nombre, numeros, empresa)
                objage.adicionar_contacto(contacto)
        case 2:
            objage.listar_contactos()
        case 3:
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            objage.busca_contacto(nombre)
        case 4:
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            objage.eliminar_contacto(nombre)
        case 5:
            objage.agenda_llena()
        case 6:
            objage.huecos_libres()
