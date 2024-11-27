def agregar_figura(figGeome, id_figura, tipo, dimensiones, area):
    figGeome[id_figura] = [tipo, dimensiones, area]

def calcular_area_triangulo():
    base = -1
    altura = -1
    while base <= 0:
        try:
            base = float(input("Ingrese base: "))
        except ValueError:
            print("Ingrese un valor valido")
    while altura <= 0:
        try:
            altura = float(input("Ingrese altura: "))
        except ValueError:
            print("Ingrese un valor valido")
    area = base*altura/2
    agregar_figura(figGeome, id_figura, "Triángulo", f"Base = {base}, Altura = {altura}", area)

def calcular_area_cuadrado():
    lado = -1
    while lado <= 0:
        try:
            lado = float(input("Ingrese lado: "))
        except ValueError:
            print("Ingrese un valor valido")
    area = lado**2
    agregar_figura(figGeome, id_figura, "Cuadrado", f"Lado = {lado}", area)

def listar_diccionario():
    if len(figGeome) == 0:
        print("\nEl diccionario está vacío. No hay figuras registradas.")
    figuras_ordenadas = sorted(figGeome.items(), key=lambda x: x[1][2], reverse=True)
    for id_figura, datos in figuras_ordenadas:
        tipo, dimensiones, area = datos
        print(f"ID: {id_figura}, Tipo: {tipo}, Dimensiones: {dimensiones}, Área: {area:.2f}")
        
#Menú principal
figGeome = {}
id_figura = 1
opc = -1
while opc != 4:
    print("\nMenu de opciones")
    print("1. Calcular el área de un triangulo")
    print("2. Calcular el área de un cuadrado")
    print("3. Lista diccionario ordenado descendentemente")
    print("4. Salir")
    try:
        opc = int(input("Seleccione una opcion: "))
    except ValueError:
        print("Ingrese un valor valido")
    match opc:
        case 1:
            calcular_area_triangulo()
            id_figura += 1
        case 2:
            calcular_area_cuadrado()
            id_figura += 1
        case 3:
            listar_diccionario()
