class Cliente:
    def __init__(self,nombre,documento,correo):
        self.nombre=nombre
        self.documento=documento
        self.correo=correo
        
    def __str__(self):
        return f'Cliente {self.nombre} - DNI:{self.documento}'
    