from Fecha import Fecha

class Empleado:
    #aqui va el codigo
    '''#atributos'''
nombre=''
apellidos=''
'''# 1 = Masculino y 2 = femenino'''
sexo=0
salario=0
'''asociaciones'''
fechaNacimiento= Fecha()
fechaIngreso= Fecha()
'''metodos'''
def cambiarSalrio(self, nsalario):
    '''aqui va el codigo'''
    self.salario=nsalario
    return "su nuevo salario es:"+self.salario 
def consultarSalario(self):
    '''#aqui va el codigo'''
    return self.salario 
def aumentoSalarial(self):
    '''#aqui va codigo'''
    aumento=self.salario*0.05
    nsalario=self.salrio+aumento
    self.salario=nsalario
    return "su nuevo salario es:"+self.salario
def DuplicarSalario(self):
    self.salario*=2
def CalcularSalarioAnual(self):
    salarioAnual= self.salario*12
    return salarioAnual
def ConsultarDiaCumpleanios(self):
    return self.fechaNacimiento.ConsultarDiaCumpleanios()
def CalcularImpuesto(self):
    return self.CalcularSalarioAnual()*0.195