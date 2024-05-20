from paquete.Cliente import Cliente
from paquete.Carrito import Carrito
from paquete.Carrito import Catalogo
#################################################################################
#  Incializo variables
#################################################################################
catalogo=Catalogo()
carrito=Carrito()
c1= Cliente('Lionel Messi','33016244','messi.goat@yahoo.com','Av Patria 1587, Cordoba, Argentina', carrito)
#################################################################################
#  Cargo el catalogo de productos
#################################################################################
url='catalogo.csv'
try:
    catalogo.cargar_catalogo(url)
except:
    print('No se pudo cargar el catalogo')
#################################################################################
#  menu principal
#################################################################################
flag = True
while flag:
    print('''
Menu Principal        
    - 1 ) Ver catalogo de productos
    - 2 ) Agregar producto por ID
    - 3 ) Ver mi carrito
    - 4 ) Finalizar compra
    - 5 ) Vaciar mi carrito
    - 6 ) Tu perfil
    - 7 ) Salir''')
    option = input('Que deseas hacer? \nIngresa una opcion: ')
    if option == '1':
        catalogo.mostrar_catalogo()
        desea_agregar= ''
        while desea_agregar not in('S','s','N','n'):
             desea_agregar = input("Desea agregar algun producto al carrito? S/N :")
        if desea_agregar == 'S' or desea_agregar =='s':
            c1.agregar_por_id(catalogo)
    elif option == '2':
        c1.agregar_por_id(catalogo)
    elif option == '3':
        c1.mostrar_carrito()
    elif option == '4':
        c1.finalizar_comprar(catalogo)
    elif option == '5':
        c1.vaciar_carrito()
    elif option == '6':
        c1.mi_perfil()
    elif option == '7':
        print(' ---> Salir')
        print('''\n \t  Hasta luego''')
        flag = False
    else:
        print('\n *** Intenta ingresar un numero')