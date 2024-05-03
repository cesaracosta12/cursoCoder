# clase 5 

# sets

# isdisjoint ( ningun elemento se repite?)

conjunto = {1, 'valor1', (1,True)}
iterable1 = (1, 'valor1', (1,True))
iterable2 = (1, 'valor2', (1,True))
print(conjunto.isdisjoint(iterable1))
print(conjunto.isdisjoint(iterable2))
#print(iterable1.isdisjoint(iterable2)) al reves no funca
# issubset ( esta dentro de otro conjunto ?)

# issuperset ()

# union (crea un conjunto nuevo, puede agregar tupla)
set2= conjunto.union(iterable1)
print(set2)

# difference (devuelve los elementos que NO se repiten)
print(conjunto.difference(iterable1))
print(conjunto.difference(iterable2))

# intersection (devuelve lo que tienen en comun)
print(conjunto.intersection(iterable2))

# difference_update ( hace lo mismo que difference y modifica el set)
# conjunto.difference_update(iterable2)
# print(conjunto)

# intersection_update ( hace lo mismo que intersectino y modifica el set)
conjunto.difference_update(iterable2)
print(conjunto)

# copy
conjunto1 = {1,'2','valor3',('test',54,67.9)}
conjunto_copy= conjunto1.copy()