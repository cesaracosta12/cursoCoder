from paquete.Articulo import Articulo


import csv
class Catalogo:
    catalogo={}
    def __init__(self):
        self.catalogo={}

    def cargar_catalogo(self,nombre_archivo_csv):    
        with open(nombre_archivo_csv) as file:   
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                 self.catalogo[len(self.catalogo)+1]= [Articulo(int(row[0]),row[1],row[2],int(row[3])),int(row[4])]
        
    def tiene_stock(self,id):            
        for articulo in self.catalogo.values():
            if articulo[0].id == id:
                if articulo[1] > 0:
                    return True
                else:
                    return False

    def mostrar_catalogo(self):
        print('_________________________________________')
        print("Catalogo:")
        if self.catalogo=={}:
            print('       no hay productos       ')
        else:
            for id, articulo in self.catalogo.items():
                if self.tiene_stock(id):
                    print(f'{id} - "{articulo[0].nombre}" de {articulo[0].marca}: ${articulo[0].precio} - unidades:{articulo[1]}')
                else:
                    print(f'{id} - "{articulo[0].nombre}" de {articulo[0].marca} - sin unidades disponibles')
        print('_________________________________________')    
         
    def seleccionar_articulo(self,id_seleccionado):
        for id, articulo in self.catalogo.items():
                if id_seleccionado == id:
                    return articulo
                
