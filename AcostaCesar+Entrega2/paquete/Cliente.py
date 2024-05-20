from paquete.Carrito import Carrito

class Cliente:
    def __init__(self,nombre,documento,correo,cart_cliente:Carrito):
        self.nombre=nombre
        self.documento=documento
        self.correo=correo
        self.cart_cliente = Carrito()
        
    def __str__(self):
        return f'''
_________________________________________
    Informacion de Cliente
    - Nombre : {self.nombre} 
    - DNI    : {self.documento}
    - correo : {self.correo}
_________________________________________
    '''
    
    def finalizar_comprar(self):
        ...