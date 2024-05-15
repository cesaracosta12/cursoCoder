
class Articulo:
    def __init__(self,id,nombre,marca,precio,stock=10):
        self.id=id
        self.nombre=nombre
        self.marca=marca
        self.precio=precio
        self.stock=stock

        
    def __str__(self):
        if self.tiene_stock == False:
            return f'{self.nombre} - Marca {self.marca} - Sin stock disponible'
        else:
            return f'{self.nombre} - Marca {self.marca} : ${self.precio} - cantidad disponible : {self.stock}'
    
    def tiene_stock(self):
        if self.stock == 0:
            return False
        else:
            return True