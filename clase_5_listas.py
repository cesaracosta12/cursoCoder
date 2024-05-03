# clase 5 
# listas

lista_strings = ['RIBER', 'te', 'fuiste', 'a', 'la', 'B', 'por', 'puto', 'y', 'cagon']

lista_nueva = lista_strings + [1,2,3]
print(lista_nueva)

# extend AGREGA AL ULTIMO
lista_nueva.extend({'item1','item2','item3'})
print(lista_nueva)

#insert (posicion,<valor>) NO REEMPLAZA, SINO QUE AGREGA
lista_nueva.insert(0,'GALLINA')
print(lista_nueva)

# reverse (da vuelta la lista)
lista_nueva.reverse()
print(lista_nueva)

# sort
lista_2 = [4,2,3,45,1,6,2,1,6]
print(lista_2)
lista_2.sort()
print(lista_2)
lista_2.sort(reverse=True)
print(lista_2)
lista_3 = ['4','2','3','45','1','6','2','1','6']
print(lista_3)
lista_3.sort()
print(lista_3)