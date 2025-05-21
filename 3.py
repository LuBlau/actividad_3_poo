class Mascota:
    def __init__(self, nombre: str, edad: int, color: str):
        self._nombre = nombre
        self._edad = edad
        self._color = color

    def imprimir_info(self):
        print(f"Nombre: {self._nombre}")
        print(f"Edad: {self._edad} años")
        print(f"Color: {self._color}")

class Perro(Mascota):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color)
        self._peso = peso
        self._muerde = muerde

    @staticmethod
    def sonido():
        print("Los perros ladran")

    def imprimir_info(self):
        super().imprimir_info()
        print(f"Peso: {self._peso} kg")
        print(f"Muerde: {'Sí' if self._muerde else 'No'}")

class PerroPequeno(Perro):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool, raza: str):
        super().__init__(nombre, edad, color, peso, muerde)
        self._raza = raza

    def imprimir_info(self):
        super().imprimir_info()
        print(f"Raza: {self._raza}")

class PerroMediano(Perro):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool, raza: str):
        super().__init__(nombre, edad, color, peso, muerde)
        self._raza = raza

    def imprimir_info(self):
        super().imprimir_info()
        print(f"Raza: {self._raza}")


class PerroGrande(Perro):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool, raza: str):
        super().__init__(nombre, edad, color, peso, muerde)
        self._raza = raza

    def imprimir_info(self):
        super().imprimir_info()
        print(f"Raza: {self._raza}")

class Gato(Mascota):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color)
        self._altura_salto = altura_salto
        self._longitud_salto = longitud_salto

    @staticmethod
    def sonido():
        print("Los gatos maúllan y ronronean")

    def imprimir_info(self):
        super().imprimir_info()
        print(f"Altura de salto: {self._altura_salto} cm")
        print(f"Longitud de salto: {self._longitud_salto} cm")

class GatoSinPelo(Gato):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float, raza: str):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)
        self._raza = raza

    def imprimir_info(self):
        super().imprimir_info()
        print(f"Raza: {self._raza}")

class GatoPeloLargo(Gato):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float, raza: str):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)
        self._raza = raza

    def imprimir_info(self):
        super().imprimir_info()
        print(f"Raza: {self._raza}")

class GatoPeloCorto(Gato):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float, raza: str):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)
        self._raza = raza

    def imprimir_info(self):
        super().imprimir_info()
        print(f"Raza: {self._raza}")

# Prueba de las clases
def main():
    perro1 = PerroPequeno("Max", 3, "Marrón", 7.5, True, "Yorkshire Terrier")
    perro1.imprimir_info()
    perro1.sonido()
    print("")

    perro2 = PerroMediano("Toby", 5, "Negro", 15.0, False, "Bulldog")
    perro2.imprimir_info()
    perro2.sonido()
    print("")

    perro3 = PerroGrande("Rex", 6, "Negro y fuego", 30.0, True, "Doberman")
    perro3.imprimir_info()
    perro3.sonido()
    print("")

    gato1 = GatoSinPelo("Sombra", 4, "Gris", 45, 120, "Esfinge")
    gato1.imprimir_info()
    gato1.sonido()
    print("")

    gato2 = GatoPeloLargo("Luna", 2, "Blanco", 50, 150, "Himalayo")
    gato2.imprimir_info()
    gato2.sonido()
    print("")

    gato3 = GatoPeloCorto("Michi", 1, "Azul grisáceo", 40, 130, "Azul Ruso")
    gato3.imprimir_info()
    gato3.sonido()

if __name__ == "__main__":
    main()