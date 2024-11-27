import random

class CEncuesta:
    def __init__(self, sexo, edad, servicio, nivel_satisfaccion):
        self._sexo = sexo  
        self._edad = edad  
        self._servicio = servicio  
        self._nivel_satisfaccion = nivel_satisfaccion  

    def set_sexo(self, sexo):
        self._sexo = sexo

    def get_sexo(self):
        return self._sexo

    def set_edad(self, edad):
        self._edad = edad

    def get_edad(self):
        return self._edad

    def set_servicio(self, servicio):
        self._servicio = servicio

    def get_servicio(self):
        return self._servicio

    def set_nivel_satisfaccion(self, nivel_satisfaccion):
        self._nivel_satisfaccion = nivel_satisfaccion

    def get_nivel_satisfaccion(self):
        return self._nivel_satisfaccion

    def consultarEncuesta(self):
        print(f"Sexo: {self._sexo}")
        print(f"Edad: {self._edad}")
        print(f"Servicio de video llamadas: {self._servicio}")
        print(f"Nivel de satisfacción: {self._nivel_satisfaccion}")



def generar_encuestas(n):
    servicios = ["Skype", "Discord", "Zoom"]
    niveles_satisfaccion = ["Bueno", "Regular", "Malo"]
    encuestas = []

    for _ in range(n):
        sexo = random.choice(["f", "m"])
        edad = random.randint(15, 75)
        servicio = random.choice(servicios)
        nivel_satisfaccion = random.choice(niveles_satisfaccion)
        encuesta = CEncuesta(sexo, edad, servicio, nivel_satisfaccion)
        encuestas.append(encuesta)

    return encuestas



def analizar_encuestas(encuestas):

    mas_joven = min(encuestas, key=lambda x: x.get_edad())
    mas_viejo = max(encuestas, key=lambda x: x.get_edad())


    mujeres_mayores = sum(1 for e in encuestas if e.get_sexo() == "f" and e.get_edad() > 18)


    zoom_usuarios = [e for e in encuestas if e.get_servicio() == "Zoom"]
    satisfaccion_zoom = {
        "Bueno": sum(1 for e in zoom_usuarios if e.get_nivel_satisfaccion() == "Bueno"),
        "Regular": sum(1 for e in zoom_usuarios if e.get_nivel_satisfaccion() == "Regular"),
        "Malo": sum(1 for e in zoom_usuarios if e.get_nivel_satisfaccion() == "Malo"),
    }


    skype_usuarios = [e for e in encuestas if e.get_servicio() == "Skype"]
    if skype_usuarios:
        mas_viejo_skype = max(skype_usuarios, key=lambda x: x.get_edad())
    else:
        mas_viejo_skype = None


    print("Persona más joven:")
    mas_joven.consultarEncuesta()
    print("\nPersona más vieja:")
    mas_viejo.consultarEncuesta()
    print(f"\nNúmero de mujeres mayores de 18 años: {mujeres_mayores}")
    print("\nSatisfacción en Zoom:")
    for nivel, cantidad in satisfaccion_zoom.items():
        print(f"{nivel}: {cantidad} usuarios")
    if mas_viejo_skype:
        print("\nPersona más vieja que usó Skype:")
        mas_viejo_skype.consultarEncuesta()
    else:
        print("\nNo hay encuestas de usuarios que usaron Skype.")


# Programa principal
if __name__ == "__main__":
    n = int(input("Ingrese la cantidad de encuestas realizadas: "))
    if n <= 0:
        print("Debe ingresar un valor mayor a 0.")
    else:
        encuestas = generar_encuestas(n)
        analizar_encuestas(encuestas)
