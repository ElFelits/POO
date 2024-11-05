#Hoja 5 - ejercicio 5
from datetime import datetime

class Producto:
    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio

    def imprimir_datos(self):
        print(f"Nombre: {self.__nombre}, codigo: {self.__codigo}, precio: S/{self.__precio}")

    def obtener_codigo(self):
        return self.__codigo

    def obtener_precio(self):
        return self.__precio

    def obtener_nombre(self):
        return self.__nombre

class Boleta:
    def __init__(self, nombre_cliente):
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.nombre_cliente = nombre_cliente
        self.productos = []
        self.total = 0

    def agregar_producto(self, producto, cantidad):
        self.productos.append((producto, cantidad))
        self.total += producto.obtener_precio() * cantidad

    def mostrar_boleta(self):
        print(f"\n--- Boleta de Venta ---")
        print(f"Fecha: {self.fecha}")
        print(f"Cliente: {self.nombre_cliente}")
        print("Productos:")
        for producto, cantidad in self.productos:
            print(f"{producto.obtener_codigo()} - {producto.obtener_nombre()} x {cantidad} = S/{producto.obtener_precio() * cantidad}")
        print(f"Total a Pagar: S/{self.total}")

class Tienda:
    def __init__(self):
        self.__productos = []
        self.__boletas = []
    
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
            if not codigo_existe:
                break
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        nuevo_producto = Producto(codigo, nombre, precio)
        self.__productos.append(nuevo_producto)
        print("Producto agregado exitosamente")
    
    def realizar_venta(self):
        if len(self.__productos) == 0:
            print("No hay productos disponibles para la venta")
        else:
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            boleta = Boleta(nombre_cliente)
            while True:
                codigo_producto = input("Ingrese el codigo del producto a vender (o 'fin' para terminar): ")
                if codigo_producto.lower() == "fin":
                    break

                producto_encontrado = None
                for producto in self.__productos:
                    if producto.obtener_codigo() == codigo_producto:
                        producto_encontrado = producto
                        break

                if producto_encontrado is None:
                    print("Producto no encontrado. Intente nuevamente")
                    continue

                cantidad = -1
                while cantidad < 0:
                    try:
                        cantidad = int(input("Ingrese la cantidad: "))
                        if cantidad < 0:
                            print("La cantidad debe ser un número positivo. Intente nuevamente.")
                    except ValueError:
                        print("Ingrese un valor numérico válido.")

                boleta.agregar_producto(producto_encontrado, cantidad)
                print("Producto agregado a la boleta")

            self.__boletas.append(boleta)
            boleta.mostrar_boleta()

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
        print("3. Realizar venta")
        print("4. Salir")
        try:
            opc = int(input("\nIngrese una opción: "))
        except ValueError:
            print("Ingrese un valor válido.")
            continue

        if opc in [1, 2, 3, 4]:
            return opc
        else:
            print("Opción no válida. Intente de nuevo.")

# Programa principal
objtie = Tienda()
while True:
    opc = Menu()
    match opc:
        case 1:
            objtie.agregar_producto()
        case 2:
            objtie.mostrar_productos()
        case 3:
            objtie.realizar_venta()
        case 4:
            break
