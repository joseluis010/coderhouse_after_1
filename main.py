from banco.cuenta_bancaria import CuentaBancaria  #importando el módulo
from banco.menu import menu_cuenta_bancaria

opcion = menu_cuenta_bancaria()

cuenta = CuentaBancaria(0)

if opcion == 1:
    monto = float(input("Monto a depositar: "))
    cuenta.depositar(monto)    
elif opcion == 2:
    monto = float(input("Monto a retirar: "))
    cuenta.retirar(monto) 
elif opcion == 3:
    cuenta.consultar_saldo()
else:
    print("Saliendo...")