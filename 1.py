class Cuenta:
    def __init__(self, saldo: float, tasa_anual: float):
        self._saldo = saldo
        self._num_consignaciones = 0
        self._num_retiros = 0
        self._tasa_anual = tasa_anual
        self._comision_mensual = 0.0

    def consignar(self, monto: float):
        if monto > 0:
            self._saldo += monto
            self._num_consignaciones += 1

    def retirar(self, monto: float):
        if monto > 0 and monto <= self._saldo:
            self._saldo -= monto
            self._num_retiros += 1
        else:
            print("Fondos insuficientes")

    def calcular_interes_mensual(self):
        interes_mensual = (self._tasa_anual / 12) * self._saldo
        self._saldo += interes_mensual

    def extracto_mensual(self):
        self._saldo -= self._comision_mensual
        self.calcular_interes_mensual()

    def imprimir(self):
        print(f"Saldo: {self._saldo}")
        print(f"Consignaciones: {self._num_consignaciones}")
        print(f"Retiros: {self._num_retiros}")
        print(f"Tasa anual: {self._tasa_anual}%")
        print(f"Comisión mensual: {self._comision_mensual}")

class CuentaAhorros(Cuenta):
    def __init__(self, saldo: float, tasa_anual: float):
        super().__init__(saldo, tasa_anual)
        self._activa = saldo >= 10000

    def consignar(self, monto: float):
        if self._activa:
            super().consignar(monto)

    def retirar(self, monto: float):
        if self._activa:
            super().retirar(monto)
            self._activa = self._saldo >= 10000

    def extracto_mensual(self):
        if self._num_retiros > 4:
            self._comision_mensual += (self._num_retiros - 4) * 1000
        super().extracto_mensual()
        self._activa = self._saldo >= 10000

    def imprimir(self):
        super().imprimir()
        print(f"Cuenta activa: {self._activa}")
        print(f"Total transacciones: {self._num_consignaciones + self._num_retiros}")

class CuentaCorriente(Cuenta):
    def __init__(self, saldo: float, tasa_anual: float):
        super().__init__(saldo, tasa_anual)
        self._sobregiro = 0.0

    def retirar(self, monto: float):
        if monto > 0:
            if monto <= self._saldo:
                super().retirar(monto)
            else:
                self._sobregiro += monto - self._saldo
                self._saldo = 0
                self._num_retiros += 1

    def consignar(self, monto: float):
        if monto > 0:
            if self._sobregiro > 0:
                if monto >= self._sobregiro:
                    monto -= self._sobregiro
                    self._sobregiro = 0
                else:
                    self._sobregiro -= monto
                    monto = 0
            super().consignar(monto)

    def extracto_mensual(self):
        super().extracto_mensual()

    def imprimir(self):
        super().imprimir()
        print(f"Total transacciones: {self._num_consignaciones + self._num_retiros}")
        print(f"Valor de sobregiro: {self._sobregiro}")

def main():
    print("Cuenta de Ahorros:")
    cuenta_ahorros = CuentaAhorros(12000, 5)
    cuenta_ahorros.consignar(3000)
    cuenta_ahorros.retirar(5000)
    cuenta_ahorros.extracto_mensual()
    cuenta_ahorros.imprimir()

    print("\nCuenta Corriente:")
    cuenta_corriente = CuentaCorriente(5000, 5)
    cuenta_corriente.retirar(7000)  # genera sobregiro
    cuenta_corriente.consignar(3000)  # reduce sobregiro
    cuenta_corriente.extracto_mensual()
    cuenta_corriente.imprimir()

if __name__ == "__main__":
    main()