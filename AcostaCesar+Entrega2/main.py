from paquete.Cliente import Cliente
from paquete.Articulo import Articulo
from paquete.Carrito import Carrito
from paquete.Carrito import Catalogo


catalogo=Catalogo()
carrito=Carrito()

c1= Cliente('Lionel Messi','33016244','messi.goat@yahoo.com', carrito)
url='catalogo.csv'

try:
    catalogo.cargar_catalogo(url)
except:
    print('No se pudo cargar el catalogo')
                
# COMPRAR()
# a la hora de finalizar la compra
# imprimir comprobante con
## info de cliente
## info carrito
## monto total
## medio de pago
## direccion y metodo de envio
## se descuente el articulo de su stock
## se imprime el ticket con la hora de la compra en un .txt

def agregar_por_id(catalog:Catalogo,cart:Carrito):
    id_seleccionado = 0
    while id_seleccionado < 1 or id_seleccionado > len(catalog.catalogo):
         while True:
             try:
                 id_seleccionado = int(input('ID del producto:'))
                 break
             except:
                 print(' *** Intenta ingresar un numero')
    articulo_agregar = catalog.seleccionar_articulo(id_seleccionado)
    cantidad_agregar =0        
    while cantidad_agregar < 1:
        while True:   
            try:
                cantidad_agregar = int(input('Cuantas unidades?: '))
                break
            except:
                print(' *** Intenta ingresar un numero mayor a cero')
    cart.agregar_al_carrito(catalog,articulo_agregar,cantidad_agregar)


flag = True
while flag:
    print('''
_________________________________________
        Menu Principal        

    - 2) Listado de productos
    - 6) Agregar al carrito por ID
    - 3) Ver mi carrito
    - 4) Finalizar compra
    - 5) Vaciar mi carrito
    - 1) Tu perfil
    - 7) Salir
_________________________________________
''')
    option = input('Que deseas hacer? \nIngresa una opcion: ')
    if option == '1':
        print(c1.__str__())
    elif option == '2':
        catalogo.mostrar_catalogo()
        desea_agregar= ''
        while desea_agregar not in('S','s','N','n'):
             desea_agregar = input("Desea agregar algun producto al carrito? S/N :")
        if desea_agregar == 'S' or desea_agregar =='s':
            agregar_por_id(catalogo,c1.cart_cliente)
        
    elif option == '3':
        c1.cart_cliente.mostrar_carrito()
    elif option == '4':
        ...
    elif option == '5':
        c1.cart_cliente.vaciar_carrito()
    elif option == '6':
        agregar_por_id(catalogo,c1.cart_cliente)
    elif option == '7':
        print('''

            Hasta luego
_________________________________________
''')
        flag = False
    else:
        print('\n *** Intenta ingresar un numero')