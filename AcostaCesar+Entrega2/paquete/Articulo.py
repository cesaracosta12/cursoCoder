
class Articulo:
    def __init__(self,id,nombre,marca,precio):
        self.id=id
        self.nombre=nombre
        self.marca=marca
        self.precio=precio
        
    def __str__(self):
             return f'{self.nombre} - de {self.marca} '
