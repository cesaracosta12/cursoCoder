# clase 12

# clases

class Motor:
    def __init__(self,cilindros=6):
        self.cilindros=cilindros
    
class Auto:
    cant_ruedas=4 # atributo de la clase
    def __init__(self,marca,modelo,num_serie,color='Blanco'):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.__num_serie = num_serie # privado
        self.motor=Motor()
    
    def __str__(self) -> str:
        return f'Auto marca {self.marca} - modelo {self.modelo} - color {self.color}'
        
    def tocar_bocina():
        print('SONIDO DE BOCINAAAAAAAA')
    
auto1= Auto('Ford','Fiesta',121,'Rojo')
auto2= Auto('Renault','12',121)
auto3= Auto('Fiat','Palio',235,'Rojo')

print(auto1.cant_ruedas)
print(auto2.cant_ruedas)
print(auto3.cant_ruedas)
# Seteo el atributo de la clase
Auto.cant_ruedas=5
print(auto1.cant_ruedas)
print(auto2.cant_ruedas)
print(auto3.cant_ruedas)

class Concesionaria:
    def __init__(self,concesionaria):
        self.concesionaria=concesionaria
        self.autos = []
    def __str__(self) -> str:
        return f'Listado de autos "{self.concesionaria}"'
    def __len__(self):
        #return f'Cantidad de autos: {len(self.autos)}'
        return len(self.autos)
    def agregar_auto(self,auto):
        if auto and auto.color.capitalize()=='negro':
            self.autos.append(auto)
        else:
            print('No hay auto negro'
        )
    def __getitem__(self,posicion):
        try:
            return self.autos[posicion]
        except:
            print(f'No se encontro auto en posicion{posicion}')
    def __setitem__(self,posicion,nuevo_auto):
        try:
            if nuevo_auto.color=='Negro':
                self.autos[posicion]=nuevo_auto
            else:
                print('El auto no es negro')
        except:
            print(f'No se pudo modificar el auto de la posicion{posicion}')
    
            
concesionaria = Concesionaria('automentita')
auto1.color='Negro'
concesionaria[0]=auto1
print(concesionaria[0])
print(concesionaria.autos)

# print(auto1.__num_serie) # no se puede acceder porque el dato es privado