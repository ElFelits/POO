import numpy as np
from numpy import random

#imprimir valores explicitos de un vector
array1 = np.array([1, 2, -1, 4, 9])
print(array1)
for i in array1:
    print(i)

#vector con valores decimales entre 0 a 1 aleatorios
array2 = random.rand(5)
print(array2.round(2)) #".round(2) para aproximar a 2 decimales"

#vector con valores aleatorios entre A a B
array3 = random.randint(10, 99, size = 5) #size representa la cantidad de valores
print(array3)

#Ingresar valores al vector manualmente
lista1 = []
n = int(input("tamaño de vector: "))
for i in range(n):
    frase = f"Ingrese valor para posicion {i}:" #ingresa un valor por cada posicion de n
    valor = int(input(frase)) #el valor pasa de string a int
    lista1.append(valor) #se agregan los valores a la lista
array4 = np.array(lista1) #la lista se transforma en vector
print(array4)

#funcionalidades
print(np.max(array4))
print(np.min(array4))
print(np.mean(array4))
print(np.sum(array4))

#recorrer vectores
array5 = random.randint(10, 99, size = 5)
for i in array5:
    print(i, end = "") #imprime los valores del vector sin forma de lista

#imprime los valores del vector de la forma "indice = valor[indice]:"

#Forma 1
for i in range(0, len(array5)):
    print(i, "=", array5[i])
#Forma 2
i = 0
while i < len(array5):
    print(f"{i} = {array5[i]}")
    i += 1 

#Eliminación de valores en vectores
array6 = np.array([2, 4, 6, 8, 10])
print(array6)
array6 = np.delete(array6, 2) #eliminando la posición 2 del vector (6)
print(array6)

#Insertar valores
array7 = np.array([2, 4, 6, 8, 10])
array7 = np.insert(array7, 3, 20) #insertar 20 en la posicion 3
array7 = np.insert(array7, 0, 5) #insertar el valor 5 en posicion 0
array7 = np.insert(array7, len(array7), 100) #agregando 100 al vector

#Eliminar mas de una posicion
array8 = np.array([2, 4, 6, 8, 10])
print(array8)
array8 = np.delete(array8, [1, 3]) #eliminando la posición 1 y 3 del vector (4 y 8)
print(array8)

#Ordenar vector
array9 = random.randint(10, 99, size = 5)
print(array9.sort()) #ordenar ascendentemente
print(array9[::-1]) #ordenar descendentemente

#Con el metodo sort no se altera el valor original
print(np.sort(array9)) 
print(np.sort(array9)[::-1])


#MATRICES


#Crear una matriz explicita
matriz1 = np.array([1,3,4,7], [2, 4, 6, 8])
print(matriz1)

M = 3
#Matriz inicializada con ceros
matriz2 = np.zeros((M,M))
#Matriz identidad
matriz3 = np.eye(M)
#Matriz inicializada con UNOS:
matriz4 = np.ones((M,M))
#Matriz inicializada con un valor especifico
matriz4 = np.full((M, M), 7)
#Matriz aleatoria en decimales
matriz5 = np.random.rand(M,M)
matriz6 = np.random.randn(M,M) #valores centrados en 0 (pueden ser negativos)
#Matriz con valores secuenciales
matriz7 = np.arange(1, 10).reshape((M, M))

#Ingresar valores a la matriz manualmente
filas = 3
columnas = 3
lista2 = []
print(f"Ingrese los valores para una matriz de {filas} x {columnas}")
for i in range(filas):
    for j in range(columnas):
        frase = "Ingrese valor ["+str(i)+", "+str(j)+"]: "
        valor = int(input(frase))
        lista2.append(valor)
#Convertir la lista en matriz
matriz8 = np.array(lista2).reshape((filas, columnas))

#operaiones aritmeticas entre elementos de una matriz
matriz9 = np.array([1, 3, 5, 7], [2, 4, 6, 8])
matriz10 = np.array([10, 12, 14, 16], [20, 22, 24, 26])
print(matriz9 + matriz10) #suma
print(matriz9 * matriz10) #multiplicacion
m = np.dot(matriz9, matriz10) #Forma 1: producto matricial
print(matriz9 @ matriz10) #Forma 2: producto matricial

#transpuesta de una matriz
print(matriz9.T)
#determinante de una matriz
print(np.linalg.det(matriz9))
#inversa de una matriz
print(np.linalg.inv(matriz9))
