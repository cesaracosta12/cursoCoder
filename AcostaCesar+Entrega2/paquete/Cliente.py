from paquete.Carrito import Carrito
from paquete.Carrito import Catalogo
from datetime import datetime

class Cliente:
    def __init__(self,nombre,documento,correo,direccion,cart_cliente:Carrito):
        self.nombre=nombre
        self.documento=documento
        self.correo=correo
        self.direccion=direccion
        self.cart_cliente = Carrito()
        
    def __str__(self):
        return f'''
    - Nombre    : {self.nombre} 
    - DNI       : {self.documento}
    - Correo    : {self.correo}
    - Direccion : {self.direccion}
    '''

    def mi_perfil(self):
        flag = True
        while flag:
            print('''
 ---> Tu perfil       
    - 1) Ver mi perfil
    - 2) Editar direccion
    - 3) Regresar''')
            option = input('\nIngresa una opcion: ')
            if option == '1':
                print(self.__str__())
            elif option == '2':
                print(f'Tu direccion actual es: "{self.direccion}"')
                nueva_direccion=input('Ingrese nueva direccion:')
                try: 
                    self.editar_direccion(nueva_direccion)
                    print('Direccion actualizada')
                except:
                    print(' *** No se pudo guardar tu direccion')
            elif option == '3':
                flag = False
            else:
                print('\n *** Intenta ingresar un numero')

    def mostrar_carrito(self):
        print('\n ---> Mostrar Carrito \n')
        self.cart_cliente.mostrar_carrito()
    
    def vaciar_carrito(self):
        print('\n ---> Vaciar Carrito \n')
        confirmar=input(f'Se eliminaran todos los productos de tu carrito \n  Deseas vaciar tu carrito? S/N: ')
        while confirmar not in('S','s','N','n'):
            print('\n Ingrese nuevamente una opcion')
            confirmar=input(f'Se eliminaran todos los productos de tu carrito \n  Deseas vaciar tu carrito? S/N: ')
        if confirmar == 'S' or confirmar =='s':
            self.cart_cliente.vaciar_carrito()
    
    def agregar_por_id(self,catalog:Catalogo):
        self.cart_cliente.agregar_por_id(catalog)
    
    def seleccionar_metodo_entrega(self):
        a_domicilio = input(f'Desea enviar a domicilio? S/N: ')
        while a_domicilio not in('S','s','N','n'):
            print('\n Ingrese nuevamente una opcion correcta')
            a_domicilio = input(f'Desea enviar a domicilio? S/N: ')
        if a_domicilio == 'S' or a_domicilio =='s':
            return f'Envio a domicilio para "{self.direccion}"'                     
        else:
            return 'Retira en el local'
    
    def generar_comprobante(self,texto):
        archivo_abierto = open (f'comprobante.txt','w')
        archivo_abierto.write(texto)
        archivo_abierto.close()
    
    def editar_direccion(self,nueva_direccion):
        self.direccion = nueva_direccion

    def finalizar_comprar(self,catalog:Catalogo):
        print('\n ---> Finalizar Compra\n')
        total = self.cart_cliente.calcular_total_carrito()
        if total ==0:
            print(f'No tienes productos agregados al carrito')
        else:
            print(f'Total a pagar: ${total}')
            confirmar=input(f'Desea confirmar compra? S/N: ')
            while confirmar not in('S','s','N','n'):
                print('\n Ingrese nuevamente una opcion correcta')
                confirmar=input(f'Desea confirmar compra? S/N: ')
            if confirmar == 'S' or confirmar =='s':
                detalle_compra= self.cart_cliente.mostrar_detalle_compra()
                for articulo_carrito in self.cart_cliente.cart.values():
                    catalog.actualizar_stock(articulo_carrito)   
                metodo_entrega= self.seleccionar_metodo_entrega()
                now = datetime.now()
                print('\n \t Finalizaste tu compra exitosamente ! \n')
                texto= f'''
################################################
#### Informacion de tu compra
#### 
#### Fecha y hora        : {now}
#### 
#### Info cliente
####     Nombre          : {self.nombre}
####     DNI             : {self.documento}
####     Correo          : {self.correo}
####     Direccion       : {self.direccion}
####  
#### Metodo de entrega   : {metodo_entrega}
####            
#### Detalle compra
{detalle_compra}
####   
#### Total a pagar       :${total}
################################################'''
                print(texto)
                self.generar_comprobante(texto)
                self.cart_cliente.cart.clear()
                              

        
        
    

    

        