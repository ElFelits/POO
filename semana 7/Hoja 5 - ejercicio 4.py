#Hoja 5 - ejercicio 4
class Producto:
    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
    def imprimir_datos(self):
        print(f"Nombre: {self.__nombre}, codigo: {self.__codigo}, precio: S/{self.__precio}")
    def obtener_codigo(self):
        return self.__codigo

class Tienda:
    def __init__(self):
        self.__productos = []
    
    def agregar_producto(self):
        codigo = input("Ingrese el código numérico del producto (único): ")
        while True:
            codigo_existe = False
            for producto in self.__productos:
                if producto.obtener_codigo() == codigo:
                    codigo_existe = True
                    print("El código ya existe. Ingrese un código único.")
                    codigo = input("Ingrese el código numérico del producto (único): ")
                    break
            if codigo_existe == False:
                break
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        nuevo_producto = Producto(codigo, nombre, precio)
        self.__productos.append(nuevo_producto)
        print("Producto agregado exitosamente")
    def mostrar_productos(self):
        if len(self.__productos) == 0:
           print("No hay productos registrados")
        else:
            print("\nLista de productos: ")
            for producto in self.__productos:
                producto.imprimir_datos()
def Menu():
    while True:
        print("\n--- Tienda Don Tito ---")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Salir")
        try:
            opc = int(input("\nIngrese una opción: "))
        except ValueError:
            print("Ingrese un valor válido.")
            continue

        if opc in [1, 2, 3]:
            return opc
        else:
            print("Opción no válida. Intente de nuevo.")

#Programa principal
objtie = Tienda()
while True:
    opc = Menu()
    match opc:
        case 1:
            objtie.agregar_producto()
        case 2:
            objtie.mostrar_productos()
        case 3:
            break
