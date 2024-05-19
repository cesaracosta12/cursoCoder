from paquete.Cliente import Cliente
from paquete.Articulo import Articulo
from paquete.Carrito import Carrito
import csv

with open('catalogo.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    catalogo={}
    for row in csv_reader:
         catalogo[len(catalogo)+1]= Articulo(row[0],row[1],row[2],row[3],row[4])
carrito=Carrito()
c1= Cliente('Lionel Messi','33016244','messi.goat@yahoo.com', carrito)

def mostrar_catalogo(catalog):
    print("Catalogo:")
    if catalog=={}:
        print('\n ...  Tu catalogo está vacío  ...\n')
    else:
        for id, articulo in catalog.items():
            print(f'{id} - {articulo}')
              
def seleccionar_articulo(catalog,nro_seleccion):
    for id, articulo in catalog.items():
            if nro_seleccion == id:
                return articulo
            # else:
            #     return nro_seleccion

mostrar_catalogo(catalogo)
            
respuesta= input('Desea agregar algun producto al carrito? S /N :')
while respuesta not in('S','s','N','n'):
    print('\n Ingrese nuevamente una opcion correcta')
    respuesta=input('Desea agregar algun producto al carrito? S /N :')
    
if respuesta == 'S' or respuesta =='s':
    # id_seleccionado = int(input('Ingrese el ID del producto que deseas agregar :'))
    id_seleccionado = input('Ingrese el ID del producto que deseas agregar :')
    print(id_seleccionado)
    print(type(int(id_seleccionado)))
    
    while int(id_seleccionado) < 1 or int(id_seleccionado) > len(catalogo):
        print('\n Ingrese nuevamente una opcion correcta')
        id_seleccionado = input('Ingrese el ID del producto que deseas agregar :')

    # articulo_agregar = seleccionar_articulo(catalogo,id_seleccionado)

    # cantidad_agregar = int(input('Cuantas unidades desea agregar?: '))
    # while int(cantidad_agregar) < 1 or type(id_seleccionado) != type(int):
    #     print('\n Ingrese nuevamente una opcion correcta')
    #     cantidad_agregar = int(input('Cuantas unidades desea agregar?: '))
        
    # carrito.agregar_al_carrito(articulo_agregar,cantidad_agregar)
else:
    print(' salir')

# selecionado = int(input('seleccione un producto :'))

# articulo_agregar=''
# for id, articulo in catalogo.items():
#     if selecionado == id:
#         print('Usted seleccionó: ')
#         print(f'{id} - {articulo}')
#         articulo_agregar = articulo
# cantidad_agregar= int(input('Cuantas unidades desea agregar?: '))    
# carrito.agregar_al_carrito(articulo_agregar,cantidad_agregar)


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


# flag = True
# while flag:
#     print('''
# ==================================
# ||        Menu Principal        ||
# ==================================

# - 1) Tu perfil
# - 2) Listado de productos
# - 3) Ver mi carrito
# - 4) Finalizar compra
# - 5) Salir
# ''')
#     option = input('Que deseas hacer? \nIngresa una opcion: ')
#     if option == '1':
#         print(c1.__str__())   
#     elif option == '2':
#         ...
#     elif option == '3':
#         ... 
#     elif option == '4':
#         ...
#     elif option == '5':
#         print('''
# ==================================
# ||          Hasta luego         ||
# ==================================
# ''')
#         flag = False
#     else:
#         print('''
# ========================================
# |  ¡ Ingresaste un valor incorrecto !  |
# |            Por favor                 |
# |   seleccione nuevamente una opcion   |
# ========================================
# ''')