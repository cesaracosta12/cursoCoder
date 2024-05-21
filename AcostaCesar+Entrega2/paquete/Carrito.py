from paquete.Articulo import Articulo
from paquete.Catalogo import Catalogo

#################################################################################
#  Mi carrito es un diccionario que cuenta con
#  key = id 
#       (es un entero que autoincrementa a medida que crece el dicc)
#  value = [Articulo,cantidad_de_unidades_agregadas] 
#       (un array con 2 indices, el primero un objeto Articulo 
#          y el segundo un int con la cantidad de unidades agregadas)
# 
#################################################################################

class Carrito:
    
    cart={}
    
    def __init__(self):
        self.cart={}
        
    def calcular_total_carrito(self):
        total=0
        for i in self.cart.values():
            total= total + (i[0].precio * i[1])
        return total
    
    def mostrar_detalle_compra(self):
        detalle= ''
        for i in self.cart.values():
                detalle = detalle + f'#### \t\t\t|- "{i[0].nombre}" de {i[0].marca} : ${i[0].precio}\n'
                detalle = detalle + f'#### \t\t\t|   Cantidad : {i[1]}\n'
        return detalle
    
    def mostrar_carrito(self):
        print("Mi carrito:")
        if self.cart=={}:
            print('      Tu carrito está vacío     ')
        else:
            for i in self.cart.values():
                print(f'\t\t |- "{i[0].nombre}" de {i[0].marca} : ${i[0].precio}')
                print(f'\t\t |   Cantidad : {i[1]}')
        print(f'\t Total a pagar: ${self.calcular_total_carrito()}')

    def agregar_al_carrito(self , art:Articulo , cant_a_agregar):
        try:
            if art[1]<cant_a_agregar:  
                print(f'\n *** Para el producto "{art[0].nombre}"')
                print(' *** No hay suficientes unidades como usted desea')    
                respuesta=input(f' --->  Desea agregar al carrito {art[1]} unidades? S/N: ')
                while respuesta not in('S','s','N','n'):
                    print('\n Ingrese nuevamente una opcion correcta')
                    respuesta=input(f' --->  Desea agregar al carrito {art[1]} unidades? S/N: ')
                if respuesta == 'S' or respuesta =='s':
                    self.cart[len(self.cart)+1]=art
                    print(f'\n  + Agregaste {art[1]} "{art[0].nombre}" a tu carrito\n')                        
                else:
                    print(f'\n - "{art[0].nombre}" no se agregó a tu carrito\n')
            else:
                self.cart[len(self.cart)+1]=[art[0],cant_a_agregar]
                print(f'\n  + Agregaste {cant_a_agregar} "{art[0].nombre}" a tu carrito\n')            
        except:
            print(' *** No se pudo agregar al carrito')

    def vaciar_carrito(self):
        try:
            self.cart.clear()
            print('\n - Se eliminaron todos los productos de su carrito\n')
        except:
            print(' *** No se pudo vaciar el carrito')

    def agregar_por_id(self,catalog:Catalogo):
        id_seleccionado = 0
        while id_seleccionado < 1 or id_seleccionado > len(catalog.catalogo):
             while True:
                 try:
                     id_seleccionado = int(input('ID del producto:'))
                     break
                 except:
                     print(' *** Intenta ingresar un numero')
        articulo_agregar = catalog.seleccionar_articulo(id_seleccionado)
        if catalog.tiene_stock(articulo_agregar[0].id):
            cantidad_agregar =0        
            while cantidad_agregar < 1:
                while True:   
                    try:
                        cantidad_agregar = int(input('Cuantas unidades?: '))
                        break
                    except:
                        print(' *** Intenta ingresar un numero mayor a cero')
            self.agregar_al_carrito(articulo_agregar,cantidad_agregar)
        else:
            print(f'\n *** "{articulo_agregar[0].nombre}" no hay unidades disponibles\n')
        
