class Vendedor:
    def __init__(self, codigo, nombre, ruta):
        #atributos de instancia
        self.__codigo = codigo
        self.__nombre = nombre
        self.__ruta = ruta
    def mostrar_info(self):
        print(f"codigo: {self.__codigo}, nombre: {self.__nombre}, ruta: {self.__ruta}")
class Cliente:
    def __init__(self, nombre:str, razon_social:str, rubro:str):
        #Atributos de instancia
        self.__nombre = nombre
        self.__razon_social = razon_social
        self.__rubro = rubro
        self.__asesor = None
#metodos de acceso
def get_asesor(self):
    return self.__asesor
def set_asesor(self, asesor):
    if isinstance(asesor, Vendedor):
        self.__asesor = asesor
    else:
        raise ValueError("El elemento debe ser de tipo vendedor")
