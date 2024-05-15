from paquete.Articulo import Articulo

class Carrito:
    cart={}
    def __init__(self):
        self.cart={}
    
    def calcular_total_carrito(self):
        total=0
        for i in self.cart.values():
            total= total + (i[0].precio *i[1])
        return total
    
    def mostrar_carrito(self):
        print('_________________________________________')
        print("Carrito de compras:")
        if self.cart=={}:
            print('\n ...  Tu carrito está vacío  ...\n')
        else:
            for i in self.cart.values():
                print(f'|- "{i[0].nombre}" - marca "{i[0].marca}" - ${i[0].precio}')
                print(f'|   Cantidad:{i[1]}') 
        print(f'Total a pagar: ${self.calcular_total_carrito()}')
        print('_________________________________________')
            
    def agregar_al_carrito(self,art:Articulo,cant_a_agregar):
        try:
            if art.tiene_stock() ==True:
                if art.stock<cant_a_agregar:
                    print(f'\n *** Para el producto "{art.nombre}"')
                    print(' *** No hay suficientes unidades como usted desea')    
                    respuesta=input(f' --->  Desea agregar al carrito {art.stock} unidades? Y/N: ')
                    while respuesta not in('Y','y','N','n'):
                        print('\n Ingrese nuevamente una opcion correcta')
                        respuesta=input(f' --->  Desea agregar al carrito {art.stock} unidades? Y/N: ')
                    if respuesta == 'Y' or respuesta =='y':
                            self.cart[len(self.cart)+1]=[art,art.stock]
                            print(f'\n  + "{art.nombre}" se agregó al carrito\n')
                    else:
                            print(f'\n - "{art.nombre}" no se agregó al carrito\n')
                else:
                    self.cart[len(self.cart)+1]=[art,cant_a_agregar]
                    print(f'\n  + "{art.nombre}" se agregó al carrito\n')
            else:
                print(f'\n *** El producto "{art.nombre}" no tiene stock disponible\n')
        except:
            print(' *** No se pudo agregar al carrito')

    def vaciar_carrito(self):
        try:
            self.cart.clear()
            print('\n - Se eliminaron todos los productos de su carrito\n')
        except:
            print(' *** No se pudo vaciar el carrito')

        
