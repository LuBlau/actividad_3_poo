class Profesor:
    """
    Esta clase denominada Profesor es una superclase que representa un
    profesor genérico.
    """

    def imprimir(self):
        print("Es un profesor.")


class ProfesorTitular(Profesor):
    """
    Esta clase denominada ProfesorTitular es una subclase de Profesor.
    """

    def imprimir(self):
        print("Es un profesor titular.")


# Clase de prueba que demuestra el polimorfismo
def main():
    profesor1 = ProfesorTitular()  # Se usa la clase hija pero se trata como clase padre
    profesor1.imprimir()


if __name__ == "__main__":
    main()