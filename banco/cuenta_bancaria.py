class CuentaBancaria:
    def __init__(self, saldo_inicial) -> None:
        self.saldo = saldo_inicial

    def depositar(self, monto):
        self.saldo += monto
        print (f"Se depósito ${monto}. Saldo actual: ${self.saldo}")

    def retirar(self, monto):
        self.saldo -= monto
        print (f"Se retiró ${monto}. Saldo actual: ${self.saldo}")

    def consultar_saldo(self):
        print(f"Saldo actual: ${self.saldo}")


