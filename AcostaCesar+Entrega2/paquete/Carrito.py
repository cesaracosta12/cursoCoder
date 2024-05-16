from paquete.Articulo import Articulo

class Carrito:
    
    # Mi carrito será un dict{} que tiene 
    #   key = id (que auto incrementa a partir  de 1 )
    #   value = [ <una instancia de objeto Articulo> , <cantidad agregada> ]
    
    cart={}
    
    def __init__(self):
        self.cart={}
    
    def calcular_total_carrito(self):
        # inicializo el total en 0
        total=0
        # recorro el diccionario cart con un for
        for i in self.cart.values():
            # sumo al total el precio del articulo y lo multiplico por su respectiva cantidad
            # el articulo está en la posicion[0]
            # la cantidad de articulos a agregar esta en la posicio [1]
            total= total + (i[0].precio * i[1])
        #devuelvo el total
        return total
    
    def mostrar_carrito(self):
        print('_________________________________________')
        print("Carrito de compras:")
        # valido si está vacío
        if self.cart=={}:
            print('\n ...  Tu carrito está vacío  ...\n')
        else:
            # recorro el carrito
            for i in self.cart.values():
                # muestro el nombre, marca y precio de cada articulo
                print(f'|- "{i[0].nombre}" - marca "{i[0].marca}" - ${i[0].precio}')
                # y tambien muestro la cantidad agregada al carrito
                print(f'|   Cantidad:{i[1]}')
        # por ultimo muestro el total a pagar llamando al metodo anterior 
        print(f'Total a pagar: ${self.calcular_total_carrito()}')
        print('_________________________________________')
            
    # para agregar un articulo al carrito le paso por parametros el articulo y la cantidad que desea agregar
    def agregar_al_carrito(self , art:Articulo , cant_a_agregar):
        try:
            # verifico si el articulo tiene stock
            if art.tiene_stock() ==True:
                # luego valido si la cantidad que desea agregar está disponible
                if art.stock<cant_a_agregar:
                    # si la cantidad que desea agregar es mayor a la disponible entonces
                    # le consulto al usuario si desea agregar la cantidad que sí está disponible mediante un input()
                    print(f'\n *** Para el producto "{art.nombre}"')
                    print(' *** No hay suficientes unidades como usted desea')    
                    respuesta=input(f' --->  Desea agregar al carrito {art.stock} unidades? S/N: ')
                    while respuesta not in('S','s','N','n'):
                        print('\n Ingrese nuevamente una opcion correcta')
                        respuesta=input(f' --->  Desea agregar al carrito {art.stock} unidades? S/N: ')
                    # si el usuario responde SI entonces agrego la cantidad disponible 
                    if respuesta == 'Y' or respuesta =='y':
                        self.cart[len(self.cart)+1]=[art,art.stock]
                        print(f'\n  + "{art.nombre}" se agregó al carrito\n')                        
                    else:
                        # si responde NO entonces muestro un mensaje  
                        print(f'\n - "{art.nombre}" no se agregó al carrito\n')
                else:
                    self.cart[len(self.cart)+1]=[art,cant_a_agregar]
                    print(f'\n  + "{art.nombre}" se agregó al carrito\n')            
            else:
                # si el articulo no tiene stock entonces muestro un mensaje
                print(f'\n *** El producto "{art.nombre}" no tiene stock disponible\n')
        except:
            print(' *** No se pudo agregar al carrito')

    # el metodo para vaciar elimina todos los elementos del diccionario
    def vaciar_carrito(self):
        try:
            self.cart.clear()
            print('\n - Se eliminaron todos los productos de su carrito\n')
        except:
            print(' *** No se pudo vaciar el carrito')

        
