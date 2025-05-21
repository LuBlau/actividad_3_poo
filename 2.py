class Inmueble:
    def __init__(self, id_inmueble: int, area: int, direccion: str):
        self._id_inmueble = id_inmueble
        self._area = area
        self._direccion = direccion

    def calcular_valor(self, valor_metro_cuadrado: int) -> float:
        return self._area * valor_metro_cuadrado

    def imprimir(self):
        print(f"ID: {self._id_inmueble}")
        print(f"Área: {self._area} m²")
        print(f"Dirección: {self._direccion}")

class Vivienda(Inmueble):
    def __init__(self, id_inmueble: int, area: int, direccion: str, habitaciones: int, banos: int):
        super().__init__(id_inmueble, area, direccion)
        self._habitaciones = habitaciones
        self._banos = banos

    def imprimir(self):
        super().imprimir()
        print(f"Habitaciones: {self._habitaciones}")
        print(f"Baños: {self._banos}")

class Casa(Vivienda):
    def __init__(self, id_inmueble: int, area: int, direccion: str, habitaciones: int, banos: int, pisos: int):
        super().__init__(id_inmueble, area, direccion, habitaciones, banos)
        self._pisos = pisos

    def imprimir(self):
        super().imprimir()
        print(f"Pisos: {self._pisos}")

class CasaRural(Casa):
    def __init__(self, id_inmueble: int, area: int, direccion: str, habitaciones: int, banos: int, pisos: int, distancia: int, altitud: int):
        super().__init__(id_inmueble, area, direccion, habitaciones, banos, pisos)
        self._distancia_cabecera = distancia
        self._altitud = altitud

    def imprimir(self):
        super().imprimir()
        print(f"Distancia a cabecera municipal: {self._distancia_cabecera} km")
        print(f"Altitud sobre el nivel del mar: {self._altitud} m")
        print(f"Valor de compra: ${self.calcular_valor(1500000)}")

class CasaUrbana(Casa):
    def __init__(self, id_inmueble: int, area: int, direccion: str, habitaciones: int, banos: int, pisos: int):
        super().__init__(id_inmueble, area, direccion, habitaciones, banos, pisos)

class CasaConjuntoCerrado(CasaUrbana):
    def __init__(self, id_inmueble: int, area: int, direccion: str, habitaciones: int, banos: int, pisos: int, valor_administracion: float, areas_comunes: bool):
        super().__init__(id_inmueble, area, direccion, habitaciones, banos, pisos)
        self._valor_administracion = valor_administracion
        self._areas_comunes = areas_comunes

    def imprimir(self):
        super().imprimir()
        print(f"Valor administración: ${self._valor_administracion}")
        print(f"Incluye áreas comunes: {'Sí' if self._areas_comunes else 'No'}")
        print(f"Valor de compra: ${self.calcular_valor(2500000)}")

class CasaIndependiente(CasaUrbana):
    def imprimir(self):
        super().imprimir()
        print(f"Valor de compra: ${self.calcular_valor(3000000)}")

class Apartamento(Vivienda):
    def __init__(self, id_inmueble: int, area: int, direccion: str, habitaciones: int, banos: int, valor_administracion: float):
        super().__init__(id_inmueble, area, direccion, habitaciones, banos)
        self._valor_administracion = valor_administracion

    def imprimir(self):
        super().imprimir()
        print(f"Valor administración: ${self._valor_administracion}")
        print(f"Valor de compra: ${self.calcular_valor(2000000)}")

class Apartaestudio(Apartamento):
    def __init__(self, id_inmueble: int, area: int, direccion: str, banos: int, valor_administracion: float):
        super().__init__(id_inmueble, area, direccion, 1, banos, valor_administracion)

    def imprimir(self):
        super().imprimir()
        print(f"Tipo: Apartaestudio")
        print(f"Valor de compra: ${self.calcular_valor(1500000)}")

class Local(Inmueble):
    def __init__(self, id_inmueble: int, area: int, direccion: str, localizacion: str):
        super().__init__(id_inmueble, area, direccion)
        self._localizacion = localizacion

    def imprimir(self):
        super().imprimir()
        print(f"Localización: {self._localizacion}")

class LocalComercial(Local):
    def __init__(self, id_inmueble: int, area: int, direccion: str, localizacion: str, centro_comercial: str):
        super().__init__(id_inmueble, area, direccion, localizacion)
        self._centro_comercial = centro_comercial

    def imprimir(self):
        super().imprimir()
        print(f"Centro Comercial: {self._centro_comercial}")
        print(f"Valor de compra: ${self.calcular_valor(3000000)}")

class Oficina(Local):
    def __init__(self, id_inmueble: int, area: int, direccion: str, localizacion: str, es_gobierno: bool):
        super().__init__(id_inmueble, area, direccion, localizacion)
        self._es_gobierno = es_gobierno

    def imprimir(self):
        super().imprimir()
        print(f"Es oficina de gobierno: {'Sí' if self._es_gobierno else 'No'}")
        print(f"Valor de compra: ${self.calcular_valor(3500000)}")

# Prueba de las clases
def main():
    print("\n--- Casa Rural ---")
    casa_rural = CasaRural(1, 120, "Vereda El Bosque", 3, 2, 1, 5, 1500)
    casa_rural.imprimir()

    print("\n--- Casa en Conjunto Cerrado ---")
    casa_conjunto = CasaConjuntoCerrado(2, 100, "Calle 12 #8-45", 3, 2, 2, 300000, True)
    casa_conjunto.imprimir()

    print("\n--- Casa Independiente ---")
    casa_ind = CasaIndependiente(3, 90, "Carrera 21 #34-56", 3, 2, 2)
    casa_ind.imprimir()

    print("\n--- Apartamento Familiar ---")
    apto = Apartamento(4, 80, "Calle 10 #5-20", 2, 2, 350000)
    apto.imprimir()

    print("\n--- Apartaestudio ---")
    estudio = Apartaestudio(5, 45, "Carrera 7 #23-89", 1, 200000)
    estudio.imprimir()

    print("\n--- Local Comercial ---")
    local = LocalComercial(6, 60, "Centro Comercial Santa Fe", "Calle", "Santa Fe")
    local.imprimir()

    print("\n--- Oficina ---")
    oficina = Oficina(7, 50, "Carrera 15 #45-78", "Interno", True)
    oficina.imprimir()

if __name__ == "__main__":
    main()