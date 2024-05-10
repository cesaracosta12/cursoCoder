# Clase 13
class Motor:
    def __init__(self,cilindros=6):
        self.cilindros=cilindros
class Auto:
    cant_ruedas=4 # atributo de la clase
    def __init__(self,marca,modelo,num_serie,color='Blanco'):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.__num_serie = num_serie # privado, solo se accede internamente desde la clase
        self.motor=Motor()
    
    def __str__(self) -> str:
        return f'Auto marca {self.marca} - modelo {self.modelo} - color {self.color}'
        
    # getter
    def mostrar_auto(self):
        if self.color == 'Blanco':
            print(f'El auto {self}tiene nro de serie: {self.__num_serie}') # asi si puedo acceder
        else:
            print('El auto no es blanco, no se puede acceder')
    # setter
    def actualizar_nro_serie(self,nuevo_num_serie):
        if self.color == 'Blanco':
            self.__num_serie= nuevo_num_serie
            print('modificado con exito')
        else:
            print('El auto no se puede modificar porque no es blanco')
    
auto1= Auto('Ford','Fiesta',121,'Rojo')
auto1.mostrar_auto()
auto1.actualizar_nro_serie(12)
auto1.mostrar_auto()

auto2= Auto('Fiat','Palio',312,'Blanco')
auto2.mostrar_auto()
auto2.actualizar_nro_serie(12)
auto2.mostrar_auto()