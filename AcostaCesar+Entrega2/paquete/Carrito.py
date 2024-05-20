from paquete.Articulo import Articulo
from paquete.Catalogo import Catalogo

class Carrito:
    cart={}
    def __init__(self):
        self.cart={}
    def calcular_total_carrito(self):
        total=0
        for i in self.cart.values():
            total= total + (i[0].precio * i[1])
        return total
    
    def mostrar_carrito(self):
        print('_________________________________________')
        print("Mi carrito:")
        if self.cart=={}:
            print('      Tu carrito está vacío     ')
        else:
            for i in self.cart.values():
                print(f'\t|- "{i[0].nombre}" de {i[0].marca} : ${i[0].precio}')
                print(f'\t|   Cant:{i[1]}')
        print(f'\t Total a pagar: ${self.calcular_total_carrito()}')
        print('_________________________________________')
            
    def agregar_al_carrito(self ,catalog:Catalogo ,art:Articulo , cant_a_agregar):
        try:
            if catalog.tiene_stock(art[0].id):
                if art[1]<cant_a_agregar:  
                    print(f'\n *** Para el producto "{art[0].nombre}"')
                    print(' *** No hay suficientes unidades como usted desea')    
                    respuesta=input(f' --->  Desea agregar al carrito {art[1]} unidades? S/N: ')
                    while respuesta not in('S','s','N','n'):
                        print('\n Ingrese nuevamente una opcion correcta')
                        respuesta=input(f' --->  Desea agregar al carrito {art[1]} unidades? S/N: ')
                    if respuesta == 'S' or respuesta =='s':
                        self.cart[len(self.cart)+1]=art
                        print(f'\n  + "{art[0].nombre}" se agregó al carrito\n')                        
                    else:
                        print(f'\n - "{art[0].nombre}" no se agregó al carrito\n')
                else:
                    self.cart[len(self.cart)+1]=[art[0],cant_a_agregar]
                    print(f'\n  + "{art[0].nombre}" se agregó al carrito\n')            
            else:
                print(f'\n *** El producto "{art[0].nombre}" no tiene stock disponible\n')
        except:
            print(' *** No se pudo agregar al carrito')

    def vaciar_carrito(self):
        try:
            self.cart.clear()
            print('\n - Se eliminaron todos los productos de su carrito\n')
        except:
            print(' *** No se pudo vaciar el carrito')

        
