from ClaseCorriente import cuentacorriente
from ClaseCuentasdeAhorros import cuentaclasedeahorros
class simuladorbancario:
    '''#aqui va codigo'''
    cedula=0
    nombre=''
    mesaapertra=0
'''asocianes'''
ConsultarValor=cuentacorriente()

'''#metodos'''
def consignarCuentaCorriente(self):
    cantidad=0
    self.Saldo=ConsultarValor()+cantidad
    return self.Saldo
def CalcularTotal():
    SaldoTotal=cuentaclasedeahorros+cuentacorriente()
    return SaldoTotal
def CambioCuentas(self):
    self.Saldo+cuentaclasedeahorros()
    return self.Saldo 
def RetirarAhorros(self):
    self.SaldoAhorro=cuentaclasedeahorros()-0
    return self.SaldoAhorro
def ConsultarSaldoCorriente(self):
    return self.Saldo
def DuplicarAhorros(self):
    self.SaldoAhorro*=2