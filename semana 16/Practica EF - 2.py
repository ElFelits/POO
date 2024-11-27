def cantidad_impares(n):
    contador = 0
    for digito in str(abs(n)):  
        if int(digito) % 2 == 1:
            contador += 1
    print(f"La cantidad de impares es: {contador}")

def calcular_suma(n, x):
    suma = 0
    for k in range(n + 1):
        termino = ((-1) ** k) * k * ((x - 1) ** (k + 1)) / (k + 1)
        suma += termino
    print(f"La suma de los términos de la serie es: {round(suma, 2)}")

#Programa principal
n = int(input("Ingrese un número entero: "))
cantidad_impares(n)
n = int(input("Ingrese n: "))
x = int(input("Ingrese x: "))
calcular_suma(n, x)
