from ClaseCorriente import cuentacorriente
from ClaseCuentasdeAhorros import cuentaclasedeahorros
class simuladorbancario:
    '''#aqui va codigo'''
    cedula=0
    nombre=''
    mesaapertra=0
'''asocianes'''
CuentaCorriente= cuentacorriente()
CuentaAhorro=cuentaclasedeahorros()

'''#metodos'''
def consignarCuentaCorriente(self,cantidad):
    self.Saldo=CuentaCorriente()+cantidad
    return self.Saldo
def CalcularTotal(self):
    self.SaldoTotal=CuentaCorriente()+CuentaAhorro()
    return self.SaldoTotal
def CambioCuentas(self):
    self.Saldo+=CuentaAhorro()
    return self.Saldo 
def RetirarAhorros(self,cantidad):
    self.SaldoAhorro=CuentaAhorro()-cantidad
    return self.SaldoAhorro
def ConsultarSaldoCorriente(self):
    return self.Saldo
def DuplicarAhorros(self):
    self.SaldoAhorro*=2