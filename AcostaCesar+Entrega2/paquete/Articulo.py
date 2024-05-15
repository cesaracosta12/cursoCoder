
class Articulo:
    def __init__(self,nombre,marca,precio,stock=10):
        self.nombre=nombre
        self.marca=marca
        self.precio=precio
        self.stock=stock

        
    def __str__(self):
        if self.stock == 0:
            return f'{self.nombre} - Marca {self.marca} - Sin stock disponible'
        else:
            return f'{self.nombre} - Marca {self.marca} : ${self.precio} - cantidad disponible : {self.stock}'
    
        