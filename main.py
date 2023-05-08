from banco.cuenta_bancaria import CuentaBancaria  #importando el módulo

cuenta_1 = CuentaBancaria(1000)
cuenta_1.depositar(2000)

cuenta_1.consultar_saldo()


cuenta_2 = CuentaBancaria(0)
cuenta_2.consultar_saldo()