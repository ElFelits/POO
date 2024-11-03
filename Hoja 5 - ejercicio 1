#Hoja 5 - ejercicio 1
class Alumnos:
  def __init__(self, codigo, nombre, notas):
    self.__codigo = codigo
    self.__nombre = nombre
    self.__notas = notas
  def calcular_promedio(self):
    pesos = [0.15, 0.2, 0.15, 0.25, 0.05, 0.2]
    promedio = 0
    for i in range(len(self.__notas)):
      promedio += self.__notas[i] * pesos[i]
    return promedio
  def obtener_info(self):
    return (f"Alumno: {self.__nombre}, codigo: {self.__codigo}, Promedio: {self.calcular_promedio()}")

class Seccion:
  def __init__(self):
    self.__alumnos = []
  def agregar_alumno(self, codigo, nombre, notas):
    alumno = Alumnos(codigo, nombre, notas)
    self.__alumnos.append(alumno)
  def mostrar_alumnos(self):
    print("\nInformacion de los alumnos: ")
    for alumno in self.__alumnos:
      print(alumno.obtener_info())

def leer_n():
  n = -1
  while n < 0:
    try:
      n = int(input("Ingrese el numero de alumnos: "))
    except ValueError:
      print("Ingrese un valor valido")
  return n
def calcular_notas(n, seccion):
  for i in range(n):
    codigo = input(f"Ingrese el codigo del alumno {i+1}: ")
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = []
    for j in range(6):
      nota = float(input(f"Ingrese la nota {j + 1} (Lb1, Ea, Lb2, TF, Pa, Eb respectivamente): "))
      notas.append(nota)
    seccion.agregar_alumno(codigo, nombre, notas)

#Programa principal
objsecc = Seccion()
n = leer_n()
calcular_notas(n, objsecc)
objsecc.mostrar_alumnos()
