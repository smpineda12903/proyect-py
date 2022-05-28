class Usuario:
    def _init_(self, name):
        self.name = name

    def role(self):
        return "Soy una persona"

    def fact(self):
        return self.Persona

    def _str_(self):
        return self.name


class DueñoEmpresa(Usuario):
    def _init_(self, Empresa):
        super()._init_("DueñoEmpresa")
        self.Empresa = Empresa

    def fact(self):
        return self.Empresa

    def role(self):
        return "Soy dueño de empresa"


class Conductor(Usuario):
    def _init_(self, Placa):
        super()._init_("Conductor")
        self.Placa = Placa
    
    def fact(self):
        return self.Placa

    def role(self):
        return "soy conductor"

class Persona(Usuario):
    def _init_(self, Persona):
        super()._init_("Persona")
        self.Persona = Persona


a = DueñoEmpresa("Nombre empresa")
b = Conductor("ACH-123")
c = Persona("Juan")
print('el rol es: ',a)
print('el nombre de la empresa es: ',a.fact())
print(a.role())
print()
print('el rol es: ',b)
print('las placas del vehiculo asignado son: ',b.fact())
print(b.role())
print()
print('su rol es: ',c)
print('el nombre es: ',c.fact())
print(c.role())