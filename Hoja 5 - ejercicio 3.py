#Hoja 5 - ejercicio 3
class Cancion:
    def __init__(self, nombre, genero, cantante):
        self.__nombre = nombre
        self.__genero = genero
        self.__cantante = cantante
    
    def imprimir_datos(self):
        return f"{self.__nombre} - {self.__genero} - {self.__cantante}"
    
class Playlist:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__canciones = []
    
    def agregar_cancion(self, cancion):
        self.__canciones.append(cancion)
    
    def mostrar_canciones(self):
        print(f"Canciones en la playlist '{self.__nombre}': ")
        for cancion in self.__canciones:
            print(cancion.imprimir_datos())
    
    def obtener_nombre(self):
        return self.__nombre
    
    def imprimir(self):
        return self.__nombre

class GestorPlaylists:
    def __init__(self):
        self.__playlists = []
    
    def crear_playlist(self):
        nombre_playlist = input("Ingrese el nombre de la playlist: ")
        objplay = Playlist(nombre_playlist)
        self.__playlists.append(objplay)
        print(f"Playlist '{nombre_playlist}' creada.")
    
    def agregar_cancion_a_playlist(self):
        nombre_playlist = input("Ingrese el nombre de la playlist: ")
        nombre_cancion = input("Ingrese el nombre de la cancion: ")
        genero = input("Ingrese el genero de la cancion: ")
        cantante = input("Ingrese el nombre del cantante: ")
        cancion = Cancion(nombre_cancion, genero, cantante)
        encontrada = False
        for playlist in self.__playlists:
            if playlist.obtener_nombre() == nombre_playlist:
                playlist.agregar_cancion(cancion)
                print(f"Canción '{nombre_cancion}' agregada a la playlist.")
                encontrada = True
                break
        if not encontrada:
            print(f"No se encontró la playlist '{nombre_playlist}'")
    
    def mostrar_canciones_en_playlist(self):
        nombre_playlist = input("Ingrese el nombre de la playlist: ")
        encontrada = False
        for playlist in self.__playlists:
            if playlist.obtener_nombre() == nombre_playlist:
                playlist.mostrar_canciones()
                encontrada = True
                break
        if not encontrada:
            print(f"No se encontró la playlist '{nombre_playlist}'.")
    
    def mostrar_playlists(self):
        if not self.__playlists:
            print("No hay playlists registradas.")
        else:
            print("Playlists registradas: ")
            for playlist in self.__playlists:
                print(playlist.imprimir())

def Menu():
    while True:
        print("1. Crear una nueva playlist")
        print("2. Agregar canción a una playlist")
        print("3. Mostrar canciones en una playlist")
        print("4. Mostrar todas las playlists")
        print("5. Salir")
        try:
            opc = int(input("\nIngrese una opción: "))
        except ValueError:
            print("Ingrese un valor válido.")
            continue

        if opc in [1, 2, 3, 4, 5]:
            return opc
        else:
            print("Opción no válida. Intente de nuevo.")

# Programa Principal
objgest = GestorPlaylists()

while True:
    opc = Menu()
    match opc:
        case 1:
            objgest.crear_playlist()
        case 2:
            objgest.agregar_cancion_a_playlist()
        case 3:
            objgest.mostrar_canciones_en_playlist()
        case 4:
            objgest.mostrar_playlists()
        case 5:
            break
