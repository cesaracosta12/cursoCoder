from paquete.Carrito import Carrito

class Cliente:
    def __init__(self,nombre,documento,correo,cart_cliente):
        self.nombre=nombre
        self.documento=documento
        self.correo=correo
        self.cart_cliente = Carrito()
        
    def __str__(self):
        return f'Cliente {self.nombre} - DNI:{self.documento}'
    
    def finalizar_comprar(self):
        ...