from abc import ABC,abstractmethod
class Evento(ABC):
  def __init__(self,nasistentes,catering,tipo):
    self._nasistentes = nasistentes
    self._catering = catering
    self._tipo = tipo
    self._precio_final = 0
  def get_tipo(self):
    return self._tipo
  def get_nasistentes(self):
    return self._nasistentes
  def get_precio_final(self):
    return self._precio_final
  @abstractmethod
  def calcula_precio(self):
    pass
  def mostrar_info(self):
    pass
class Infantil(Evento):
  def __init__(self,nasistentes,catering,tipo,payaso,tematica):
    super().__init__(nasistentes,catering,tipo)
    self.__payaso=payaso
    self.__tematica=tematica
    self.calcula_precio()
  def calcula_precio(self):
    precio=300
    if self._nasistentes>20:
      precio=precio+19*(self._nasistentes-20)
    self.__precio_final=precio
    return precio
  def mostrar_info(self):
    print(f"Evento : {self._tipo} N° Asistentes : {self._nasistentes} Precio : {self.__precio_final}")
class Integrando(Evento):
  def __init__(self,nasistentes,catering,tipo,empresa):
    super().__init__(nasistentes,catering,tipo)
    self.__empresa=empresa
    self.calcula_precio()
  def calcula_precio(self):
    precio=590
    if self._nasistentes>20:
      precio=precio+35*(self._nasistentes-20)
    self.__precio_final=precio
    return precio
  def mostrar_info(self):
    print(f"Evento : {self._tipo} N° Asistentes : {self._nasistentes} Precio : {self.__precio_final}")
class Cumpleaños(Evento):
  def __init__(self,nasistentes,catering,tipo,torta,bebida):
    super().__init__(nasistentes,catering,tipo)
    self.__torta=torta
    self.__bebida=bebida
    self.calcula_precio()
  def calcula_precio(self):
    precio=480
    if self._nasistentes>20:
      precio=precio+23*(self._nasistentes-20)
    self.__precio_final=precio
    return precio
  def mostrar_info(self):
    print(f"Evento : {self._tipo} N° Asistentes : {self._nasistentes} Precio : {self.__precio_final}")
class Manejador:
  def __init__(self):
    self.__listaeventos=[]
  def agregar_evento(self,objevento):
    self.__listaeventos.append(objevento)
  def listar_evento(self):
    for evento in self.__listaeventos:
      evento.mostrar_info()
  def promedio_precio_infantil(self):
    suma=0
    cont=0
    for evento in self.__listaeventos:
      if evento.get_tipo()=='Infantil':
        suma=suma+evento.calcula_precio()
        cont=cont+1
        prom=suma/cont
    print(f"El promedio de los precios infatil es : {prom}")
  def precio_mayor(self):
    mayor=0
    for precio in self.__listaeventos:
      if precio.calcula_precio()>mayor:
        mayor=precio.calcula_precio()
        mayor.mostrar_info()
  def ordenar_eventos(self):
    dic={}
    for evento in self.__listaeventos:
      dic[evento.calcula_precio()]=[evento.get_tipo(),evento.get_nasistentes()]
    dic_ord=sorted(dic.items())
    print(dic_ord)

#Programa principal
objman=Manejador()
opc=-1
while opc!=6:
  print("1. Agregar evento")
  print("2. Mostrar eventos")
  print("3. Promedio precio infantil")
  print("4. Precio mayor")
  print("5. Eventos Ordenados")
  print("6. Salir")
  opc=int(input("Ingrese una opcion : "))
  match opc:
    case 1:
      tipo=input("Ingrese el tipo de evento : ")
      nasistentes=int(input("Ingrese la cantidad de asistentes : "))
      catering=input("Ingrese si desea catering (s n) : ")
      if tipo=='Infantil':
        payaso=input("Ingrese si desea payaso (s n) : ")
        tematica=input("Ingrese la tematica : ")
        obj=Infantil(nasistentes,catering,tipo,payaso,tematica)
      if tipo=='Integrando':
        empresa=input("Ingrese la empresa : ")
        obj=Integrando(nasistentes,catering,tipo,empresa)
      if tipo=='Cumpleaños':
        torta=input("Ingrese si desea torta (s n) : ")
        bebida=input("Ingrese si desea bebida (s n) : ")
        obj=Cumpleaños(nasistentes,catering,tipo,torta,bebida)
      objman.agregar_evento(obj)
    case 2:
      objman.listar_evento()
    case 3:
      objman.promedio_precio_infantil()
    case 4:
      objman.precio_mayor()
    case 5:
      objman.ordenar_eventos()





class Evento:
  def __init__(self,nas,cat,tem='',pay='',emp='',torta='',bebida=''):
    self.__nasistentes=nas
    self.__catering=cat
    self.__tematica=tem
    self.__payaso=pay
    self.__empresa=emp
    self.__torta=torta
    self.__bebida=bebida
    self.__precio_final=0
    self.calcula_precio()
  def calcula_precio(self):
    if self.__tematica!='':
      precio=300
      if self.__nasistentes>20:
        precio=precio+19*(self.__nasistentes-20)
      if self.__payaso=='s':
        precio=precio+400
    else:
      precio=0
    self.__precio_final=precio
  def get_precio_final(self):
    return self.__precio_final
  def get_tematica(self):
    return self.__tematica
  def mostrar_info(self):
    print(f"Evento : {self.__tematica} Catering : {self.__catering} Precio Final : {self.__precio_final}")
#Programa Principal
lista_eventos=[]
objinfantil1=Evento(50,'s','BabyShark','n')
objinfantil2=Evento(30,'n','goku','s')
objinteg=Evento(18,'s',emp='BCP')
objcum=Evento(100,'s','','','','s','s')
lista_eventos.append(objinfantil1)
lista_eventos.append(objinfantil2)
lista_eventos.append(objinteg)
lista_eventos.append(objcum)
#reporte1
for evento in lista_eventos:
  evento.mostrar_info()
#reporte2
suma=0
cont=0
for evento in lista_eventos:
  if evento.get_tematica()!='':
    suma=suma+evento.get_precio_final()
    cont=cont+1
    prom=suma/cont
print(f"El promedio de los precios es : {prom}")
