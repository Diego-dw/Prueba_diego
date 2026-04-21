class Trabajador:
    def __init__(self, nombre, edad, peso, altura, salario):
        self.__nombre = nombre
        self.__edad = edad
        self.__peso = peso
        self.__altura = altura
        self.__salario = salario

#getters
def get_nombre(self):
    return self.__nombre

def get_edad(self):
    return self.__edad

def get_peso(self):
    return self.__peso

def get_altura(self):
    return self.__altura

def get_salario(self):
    return self.__salario

#Setters
def set_nombre(self, nombre):
    self.__nombre = nombre

def set_edad(self, edad):
    self.__edad = edad

def set_peso(self, peso):
    self.__peso = peso

def set_altura(self, altura):
    self.__altura = altura

def set_salario(self, salario):
    self.__salario = salario

#metodos
def calcular_imc(self):
    return self.__peso / (self.__altura ** 2)

def aumento_salario(self, porcentaje):
    aumento = self.__salario * (porcentaje / 100)
    self.__salario += aumento

#Info
    def info(self):
        print(f"Nombre: {self.__nombre}")
        print(f"edad: {self.__edad}")
        print(f"peso: {self.__peso} Kg")
        print(f"altura: {self.__altura} m")
        print("Salario: $", round(self.__salario, 2))


#prueba
t1 = Trabajador("Diego", 20, 82, 1.76, 10000)
t1.info()
