from paquete.Cliente import Cliente
from paquete.Articulo import Articulo
from paquete.Carrito import Carrito

#Tecno
a1 = Articulo(1,'Iphone 12','Apple',1000)
a2 = Articulo(2,'Galaxy S24','Samsung',900)
a3 = Articulo(3,'Auricular BT','JBL',200,1)
a4 = Articulo(4,'Monitor 24 pulgadas','LG',400,2)
a5 = Articulo(5,'Monitor 24 pulgadas','Samsung',350,0)
#Hogar
a6 = Articulo(6,"Juego Mesa + 6 sillas","Messitas",600,2)
a7 = Articulo(7,"Puerta de madera","Pentagono",200,6)
a8 = Articulo(8,"Taladro","Banfield",180,6)
#Moda
a9 = Articulo(9,"Remera Lisa","Nike",40,2)
a10 = Articulo(10,"Pantalon cargo","Mentita",20,2)
a11 = Articulo(11,"Campera jean","Levis",80,6)
a12 = Articulo(12,"Zapatillas urbana","Vans",60,6)

# Carrito
carrito = Carrito()
#Cliente
c1= Cliente('Lionel Messi','10','messi.goat@yahoo.com',carrito)
print(c1.__str__())

# carrito.mostrar_carrito() 
carrito.agregar_al_carrito(a3,6)
# carrito.agregar_al_carrito(a1,1)
# carrito.mostrar_carrito()    
# carrito.vaciar_carrito()
# carrito.mostrar_carrito()   
# carrito.agregar_al_carrito(a6,2)
carrito.mostrar_carrito()   