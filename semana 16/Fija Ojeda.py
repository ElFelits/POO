import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Sistema:
    def _init_(self):
        self.__dfCalif = pd.read_excel("NotasAlumnos.xlsx", sheet_name="Notas")

    def datosAlumno(self):
        print("\n\nDatos de calificación")
        print("-----------------------")

        codigo = self.ingCodigo()
        if codigo in self.__dfCalif.Codigo.values:
            print("Código ya registrado")
        else:
            nombre = self.ingNombre()
            parcial = self.ingresarNota("Examen parcial: ")
            final = self.ingresarNota("Examen final: ")
            alumno = Alumno(codigo, nombre, parcial, final)
            self.regAlumno(alumno)

    def ingCodigo(self):
        while True:
            codigo = input("Código del alumno ")
            if codigo.strip() != "":
                if codigo[0] == "A" and len(codigo) == 7 and codigo[1:].isdigit():
                    return codigo
                else:
                    print("Código debe tener la estructura Annnnnn")
            else:
                print("Código no puede estar vacío")

    def ingNombre(self):
        while True:
            nombre = input("Nombre del alumno ")
            if nombre.strip() != "" and not any(map(str.isdigit, nombre)):
                return nombre
            else:
                print("Nombre vacio o con números")

    def ingresarNota(self, etiqueta):
        while True:
            try:
                nota = float(input(etiqueta))
                if 0 <= nota <= 20:
                    return nota
                else:
                    print("Nota fuera de rango")
            except ValueError:
                print("No ingresó un número, inténtelo nuevamente")

    def regAlumno(self, alumno):
        self._dfCalif.loc[self._dfCalif.shape[0]] = alumno.dataRow()

    def listaCalif(self):
        print(self.__dfCalif)

    def estadisticas(self):
        print("Estadísticas del examen parcial")
        print(self.__dfCalif["Parcial"].describe())
        print("Estadísticas del examen final")
        print(self.__dfCalif["Final"].describe())
        print("Estadísticas del nota final")
        print(self.__dfCalif["NotaFinal"].describe())
        print(self.__dfCalif.groupby(["Condicion"])["NotaFinal"].count())

        valores = np.array(
            self.__dfCalif.groupby(["Condicion"])["NotaFinal"].count().tolist()
        )
        etiquetas = np.array(
            self.__dfCalif.groupby(["Condicion"])["NotaFinal"].count().keys().tolist()
        )
        plt.pie(valores, labels=etiquetas)
        plt.legend(title="Nota Final")
        plt.show()


class Alumno:
    def _init_(self, codigo, nombre, parcial, final):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__parcial = parcial
        self.__final = final
        self._notaFinal = (self.parcial + self._final) / 2
        self._condicion = "Aprobado" if self._notaFinal >= 12.5 else "Desaprobado"

    def dataRow(self):
        return [
            self.__codigo,
            self.__nombre,
            self.__parcial,
            self.__final,
            self.__notaFinal,
            self.__condicion,
        ]


# main
def main():
    sistema = Sistema()
    while True:
        op = menu()
        if op == 1:
            sistema.datosAlumno()
        elif op == 2:
            sistema.listaCalif()
        elif op == 3:
            sistema.estadisticas()
        elif op == 4:
            # sistema.grabarDatos()
            break


def menu():
    print("\nSistema de Calificaciones")
    print("--------------------------")
    print("[1] Registrar calificación")
    print("[2] Listar Calificaciones")
    print("[3] Mostrar Estadísticas")
    print("[4] Salir")
    op = ingresa_opcion("Ingresa tu opción: ", 1, 4)
    return op


def ingresa_opcion(etiqueta, inferior, superior):
    while True:
        try:
            numint = int(input(etiqueta))
            if inferior <= numint <= superior:
                return numint
            else:
                print("Opción no existe, inténtelo nuevamente")
        except ValueError:
            print("El valor ingresado debe ser un número")


# Programa principal
main()
