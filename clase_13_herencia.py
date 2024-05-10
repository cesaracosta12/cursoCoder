# Clase 13 herencia
# Herencia


class Vehiculo:
    def __init__(self,marca,color):
        self.marca = marca
        self.color = color
    def tocar_bocina(self):
        print('SONIDO DE BOCINA')
    def __str__(self):
        return f'{type(self).__name__} {self.marca} - {self.color}'

class Acuatico():
    def avanzar(self,distacia):
        print(f'El {type(self).__name__} avanza {distacia} millas')
    
class Terrestre():       
    def avanzar(self,distacia):
        print(f'El {type(self).__name__} avanza {distacia} metros')

class Auto(Vehiculo,Terrestre):
    def __init__(self,marca,color,cant_ruedas):
        self.cant_ruedas = cant_ruedas
        super().__init__(marca,color)
               
    # version 2
    # def __init__(self,cant_ruedas,**kwargs):
    #     self.cant_ruedas = cant_ruedas
    #     super().__init__(**kwargs)
    def tocar_bocina(self):
        super().tocar_bocina()
        print('El auto tocando BOCINAAAA')
  
class Moto(Vehiculo,Terrestre):
    def __init__(self,marca,color,cant_ruedas):
        self.cant_ruedas = cant_ruedas
        super().__init__(marca,color)
    
class Lancha(Vehiculo,Acuatico):
    ...


v1= Vehiculo('Ford','Verde')
#v1.tocar_bocina()
print(v1)

a1=Auto('Fiat','Azul',4)
#a1.tocar_bocina()
# version 2
#a1=Auto(4,'Fiat','Azul')
print(a1,f' - ruedas {a1.cant_ruedas}')

m1=Moto('Yamaha','Amarilla',2)
#m1.tocar_bocina()
print(m1,f' - ruedas {m1.cant_ruedas}')

l1=Lancha('BMW','Blanca')
#l1.tocar_bocina()
print(l1)

a1.avanzar(30)
l1.avanzar(60)

