class Persona:
    def __init__(self, nombre, edad, direccion):
        self._nombre = nombre
        self._edad = edad
        self._direccion = direccion

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion

class Empleado:
    def __init__(self, puesto, salario):
        self._puesto = puesto
        self._salario = salario

    @property
    def puesto(self):
        return self._puesto

    @puesto.setter
    def puesto(self, puesto):
        self._puesto = puesto

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario

class Responsable(Persona, Empleado):
    def __init__(self, nombre, edad, direccion, puesto, salario):
        Persona.__init__(self, nombre, edad, direccion)
        Empleado.__init__(self, puesto, salario)

class Departamento:
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

class Area:
    def __init__(self, nombre, departamento):
        self._nombre = nombre
        self._departamento = departamento

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def departamento(self):
        return self._departamento

    @departamento.setter
    def departamento(self, departamento):
        self._departamento = departamento

class Director(Responsable):
    pass

class Gerente(Responsable):
    pass

class JefeArea(Responsable):
    pass
