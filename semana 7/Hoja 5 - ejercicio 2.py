#Hoja 5 - ejercicio 2
class Candidato:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__votos = 0
    def agregar_voto(self):
        self.__votos += 1
    def obtener_nombre(self):
        return self.__nombre
    def obtener_votos(self):
        return self.__votos
    def porcentaje_votos(self, total_votos):
        porcentaje = (self.__votos / total_votos) * 100
        return porcentaje  
class Eleccion:
    def __init__(self):
        self.__candidatos = []
        self.__total_votos = 0
    def agregar_candidato(self, nombre):
        candidato = Candidato(nombre)
        self.__candidatos.append(candidato)
    def registrar_voto(self, candidato_nombre):
        for candidato in self.__candidatos:
            if candidato.obtener_nombre() == candidato_nombre:
                candidato.agregar_voto()
                self.__total_votos += 1
                break 
        else:
            return False
        return True
    def mostrar_resultados(self):
        print("\nResultados de la eleccion: ")
        for candidato in self.__candidatos:
            votos = candidato.obtener_votos()
            porcentaje = candidato.porcentaje_votos(self.__total_votos)
            print(f"{candidato.obtener_nombre()}: {votos}: votos, {porcentaje}%")
    def obtener_candidato_ganador(self):
        ganador = self.__candidatos[0]
        for candidato in self.__candidatos:
            if candidato.obtener_votos() > ganador.obtener_votos():
                ganador = candidato
        return ganador
def registrar_votaciones(objelecc):
    Nvotantes = -1
    for i in range(5):
        nombre = input(f"Ingrese el nombre del candidato {i + 1}: ")
        objelecc.agregar_candidato(nombre)
    while Nvotantes < 0:
        try:
            Nvotantes = int(input("Ingrese el numero de votantes: "))
        except ValueError:
            print("Ingrese un valor valido")
    for i in range(Nvotantes):
        while True:
            voto = input(f"Ingrese el nombre del candidato del votante {i + 1} ")
            if objelecc.registrar_voto(voto) == True:
                break
            elif objelecc.registrar_voto(voto) == False:  
                print("Nombre de candidato no valido")
    objelecc.mostrar_resultados()
    ganador = objelecc.obtener_candidato_ganador()
    print(f"\nEl candidato ganador es: {ganador.obtener_nombre()} con {ganador.obtener_votos()} votos")

#Programa Principal
objelecc = Eleccion()
registrar_votaciones(objelecc)
