class Persona:
    def __init__(self, nombre: str, direccion: str):
        self._nombre = nombre
        self._direccion = direccion

    def get_nombre(self) -> str:
        return self._nombre

    def get_direccion(self) -> str:
        return self._direccion

    def set_nombre(self, nombre: str):
        self._nombre = nombre

    def set_direccion(self, direccion: str):
        self._direccion = direccion

    def imprimir_info(self):
        print(f"Nombre: {self._nombre}")
        print(f"Dirección: {self._direccion}")

class Estudiante(Persona):
    def __init__(self, nombre: str, direccion: str, carrera: str, semestre: int):
        super().__init__(nombre, direccion)
        self._carrera = carrera
        self._semestre = semestre

    def get_carrera(self) -> str:
        return self._carrera

    def get_semestre(self) -> int:
        return self._semestre

    def set_carrera(self, carrera: str):
        self._carrera = carrera

    def set_semestre(self, semestre: int):
        self._semestre = semestre

    def imprimir_info(self):
        super().imprimir_info()
        print(f"Carrera: {self._carrera}")
        print(f"Semestre: {self._semestre}")

class Profesor(Persona):
    def __init__(self, nombre: str, direccion: str, departamento: str, categoria: str):
        super().__init__(nombre, direccion)
        self._departamento = departamento
        self._categoria = categoria

    def get_departamento(self) -> str:
        return self._departamento

    def get_categoria(self) -> str:
        return self._categoria

    def set_departamento(self, departamento: str):
        self._departamento = departamento

    def set_categoria(self, categoria: str):
        self._categoria = categoria

    def imprimir_info(self):
        super().imprimir_info()
        print(f"Departamento: {self._departamento}")
        print(f"Categoría: {self._categoria}")

# Ejemplo de uso
def main():
    estudiante = Estudiante("Juan Pérez", "Calle 123", "Ingeniería", 5)
    profesor = Profesor("María Gómez", "Avenida Principal", "Matemáticas", "Titular")

    print("Información del Estudiante:")
    estudiante.imprimir_info()

    print("\nInformación del Profesor:")
    profesor.imprimir_info()

if __name__ == "__main__":
    main()