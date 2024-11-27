import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
class Manejador:
    def __init__(self):
        self.__migraciongeneral=pd.read_excel('Emig_Inmg.xlsx',sheet_name='Pob_Inm_Emig')
        self.__migracion2017=pd.read_excel('Emig_Inmg.xlsx',sheet_name='Pob_2017')
    def mostrar_info(self):
        print(self.__migraciongeneral)
    def reporte_1(self, año1, año2):
        df=pd.DataFrame(self.__migraciongeneral)
        df_año1Lima = df.loc[(df['Año'] == año1) & (df['Departamento'] == "Lima y Callao")]
        df_año2Lima = df.loc[(df['Año'] == año2) & (df['Departamento'] == "Lima y Callao")]
        df_año1 = df.loc[(df['Año'] == año1) & (df['Departamento'] != "Lima y Callao")]
        df_año2 = df.loc[(df['Año'] == año2) & (df['Departamento'] != "Lima y Callao")]
        plt.figure(figsize=(9,4),facecolor="skyblue")
        plt.subplot(131)
        plt.plot(list(df_año1["Inmigrantes1"]),list(df_año1["Departamento"]),'r^-',label=año1)
        plt.plot(list(df_año2["Inmigrantes1"]),list(df_año2["Departamento"]),'g^-',label=año2)
        plt.legend()
        plt.ylabel('Departamentos')
        plt.xlabel('Inmigrantes cada 100000 personas')
        plt.title("Inmigrantes por departamentos en el Perú")
        plt.subplot(133)
        plt.plot(list(df_año1Lima["Inmigrantes1"]),list(df_año1Lima["Departamento"]),'r^',label=año1)
        plt.plot(list(df_año2Lima["Inmigrantes1"]),list(df_año2Lima["Departamento"]),'g^',label=año2)
        plt.legend()
        plt.ylabel('Departamentos')
        plt.xlabel('Inmigrantes cada 100000 personas')
        plt.title("Inmigrantes en Lima")
        plt.show()
    def reporte_2(self, año1, año2):
        df=pd.DataFrame(self.__migraciongeneral)
        df_año1Lima = df.loc[(df['Año'] == año1) & (df['Departamento'] == "Lima y Callao")]
        df_año2Lima = df.loc[(df['Año'] == año2) & (df['Departamento'] == "Lima y Callao")]
        df_año1 = df.loc[(df['Año'] == año1) & (df['Departamento'] != "Lima y Callao")]
        df_año2 = df.loc[(df['Año'] == año2) & (df['Departamento'] != "Lima y Callao")]
        plt.figure(figsize=(9,4),facecolor="skyblue")
        plt.subplot(131)
        plt.plot(list(df_año1["Emigrantes1"]),list(df_año1["Departamento"]),'r^-',label=año1)
        plt.plot(list(df_año2["Emigrantes1"]),list(df_año2["Departamento"]),'g^-',label=año2)
        plt.legend()
        plt.ylabel('Departamentos')
        plt.xlabel('Emigrantes cada 100000 personas')
        plt.title("Emigrantes por departamentos en el Perú")
        plt.subplot(133)
        plt.plot(list(df_año1Lima["Emigrantes1"]),list(df_año1Lima["Departamento"]),'r^',label=año1)
        plt.plot(list(df_año2Lima["Emigrantes1"]),list(df_año2Lima["Departamento"]),'g^',label=año2)
        plt.legend()
        plt.ylabel('Departamentos')
        plt.xlabel('Emigrantes cada 100000 personas')
        plt.title("Emigrantes en Lima")
        plt.show()
    def reporte_3(self):
        df_inmigrantes_x_region= self.__migraciongeneral.groupby('Region')['Inmigrantes1'].sum()
        df_emigrantes_x_region= self.__migraciongeneral.groupby('Region')['Emigrantes1'].sum()
        plt.figure(figsize=(9, 4),facecolor='skyblue')
        plt.subplot(131)
        plt.bar(list(df_inmigrantes_x_region.keys()),list(df_inmigrantes_x_region),label= 'Inmigrantes')
        plt.legend()
        plt.ylim([1,200])
        plt.ylabel('Inmigrantes cada 100000 personas')
        plt.subplot(133)
        plt.bar(list(df_emigrantes_x_region.keys()),list(df_emigrantes_x_region),label= 'Emigrantes',color="green")
        plt.legend()
        plt.ylim([1,200])
        plt.ylabel('Emigrantes cada 100000 personas')
        plt.show()
    def reporte_4(self,departamento):
        df=pd.DataFrame(self.__migracion2017)
        datos_filtrado = df.loc[df["Departamento"]==departamento]
        plt.barh("Inmigrantes",datos_filtrado["Inmigrantes1"],label="Inmigrantes")
        plt.barh("Emigrantes",datos_filtrado["Emigrantes1"],label="Emigrantes")
        plt.barh("PoblacionTotal",datos_filtrado["PoblacionTotal1"],label="PoblacionTotal")
        plt.legend()
        plt.xlabel('Emigrantes e inmigrantes cada 100000 personas')
        plt.ylabel('Tipo de población')
        plt.title(f"Barras comparando Inmigrantes y Emigrantes en el año 2017 en {departamento}")
        plt.show()
    def reporte_4_1(self):
        df=pd.DataFrame(self.__migracion2017)
        plt.figure(figsize=(9,4),facecolor="skyblue")
        plt.subplot(131)
        plt.barh(list(df.Departamento),df["Inmigrantes1"],label="Inmigrantes")
        plt.legend()
        plt.subplot(132)
        plt.barh(list(df.Departamento),df["Emigrantes1"],label="Emigrantes",color="green")
        plt.legend()
        plt.subplot(133)
        plt.barh(list(df.Departamento),df["PoblacionTotal1"],label="PoblacioTotal",color="black")
        plt.legend()
        plt.xlabel('Emigrantes e inmigrantes cada 100000 personas')
        plt.ylabel('Tipo de población')
        plt.title(f"Barras comparando Inmigrantes y Emigrantes en el año 2017 en Amazonas")
        plt.show()
    def reporte_extra_1(self,departamento):
        df=pd.DataFrame(self.__migraciongeneral)
        df_departamento=df.loc[df["Departamento"]==departamento]
        datos_por_añoInm=df_departamento.groupby("Año")["Inmigrantes1"].sum()
        ejex=sorted(list(set(df["Año"])))
        ejey=[]
        for i in datos_por_añoInm:
            ejey.append(i)
        df1=pd.DataFrame({"Año":ejex ,"Cantidad":ejey})
        X = df1[['Año']]
        y = df1['Cantidad'] 
        modelo = LinearRegression()
        modelo.fit(X, y)
        año_2024 = np.array([[2024]])
        prediccion = modelo.predict(año_2024)
        print(f'Predicción para el año 2024 en el departamento de {departamento}: {round(prediccion[0]*100000,0)} inmigrantes aproximadamente')
    def reporte_extra_2(self, departamento):
        df = pd.DataFrame(self.__migraciongeneral)
        dftotalin = df.groupby('Año')['Inmigrantes1'].sum()
        dftotalem = df.groupby('Año')['Emigrantes1'].sum()
        df1 = df.loc[df["Departamento"] == departamento]
        dftotalin_dep = df1.groupby('Año')['Inmigrantes1'].sum()
        dftotalem_dep = df1.groupby('Año')['Emigrantes1'].sum()
        total_inmigrantes = dftotalin.sum()
        total_emigrantes = dftotalem.sum()
        porcentajes_inmigrantes = (dftotalin_dep / total_inmigrantes) * 100
        porcentajes_emigrantes = (dftotalem_dep / total_emigrantes) * 100
        print(f'Porcentajes de Inmigrantes en {departamento}:')
        for año, porcentaje in porcentajes_inmigrantes.items():
            print(f'Año {año}: {porcentaje:.2f}%')
        print(f'Porcentajes de Emigrantes en {departamento}:')
        for año, porcentaje in porcentajes_emigrantes.items():
            print(f'Año {año}: {porcentaje:.2f}%')
        
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.hist(porcentajes_inmigrantes, bins=5, color='purple', edgecolor='black', alpha=0.7)
        plt.title(f'Histograma de Inmigrantes por año en {departamento}')
        plt.xlabel('Porcentaje de Inmigrantes')
        plt.ylabel('Frecuencia')

        plt.subplot(1, 2, 2)
        plt.hist(porcentajes_emigrantes, bins=5, color='orange', edgecolor='black', alpha=0.7)
        plt.title(f'Histograma de Emigrantes por año en {departamento}')
        plt.xlabel('Porcentaje de Emigrantes')
        plt.ylabel('Frecuencia')
        plt.tight_layout()
        plt.show()
#Programa principal
Obj=Manejador()
opc=-1
Obj.mostrar_info()
while not(opc==7):
    print("1) Reporte 1")
    print("2) Reporte 2")
    print("3) Reporte 3")
    print("4) Reporte 4")
    print("5) Reporte adicional 1")
    print("6) Reporte adicional 2")
    print("7) Salir")
    opc=int(input("Ingrese una opcion : "))
    match opc:
        case 1:
            año1=int(input("Ingrese el primer año a comparar : "))
            año2=int(input("Ingrese el segundo año a comparar : "))
            Obj.reporte_1(año1,año2)
        case 2:
            año1=int(input("Ingrese el primer año a comparar : "))
            año2=int(input("Ingrese el segundo año a comparar : "))
            Obj.reporte_2(año1,año2)
        case 3:
            Obj.reporte_3()
        case 4:
            confirmacion=input("¿Desea ver la comparacion de todos los departamentos? (si-no): ")
            if confirmacion=="si":
                Obj.reporte_4_1()
            if confirmacion=="no":
                departamento=input("Ingrese el departamento que desee comparar : ")
                Obj.reporte_4(departamento)
        case 5:
            departamento=input("Ingrese el departamento que desea predecir la inmigración : ")
            Obj.reporte_extra_1(departamento)
        case 6:
            departamento=input("Ingrese el departamento que desea ver el histograma : ")
            Obj.reporte_extra_2(departamento)
