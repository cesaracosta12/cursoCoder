# clase 4

# conjuntos
lista = ['item 1',2,False,'42']
tupla = ('item 1',2,False,'42')
conjunto ={'item 1', 3, True,4.3}

set1=[]
set2=()
set3={}
set4=set()

# print(type(set1))
# print(type(set2))
# print(type(set3))
# print(type(set4))
# 
# lista_prueba = [1,2,3,'test','5',('otra','lista')]
# # lista_prueba = [1,2,3,'test','5',['otra','lista']]
# set_pro = set(lista_prueba)
# print(set_pro)
# el set no maneja indice, y no respeta un orden
# el set no puede mostrar listas, pero si tuplas

list_test={'sfd','as','sad'}
set_test = set(list_test)
# funciones integradas
lista1 =['as','ds','lp']
tupla1=('sda','22d','s2s')

# ADD
# es mutable, no usa el append para agregar
#set_test.add(lista1)
print(set_test)
set_test.add(tupla1)
print(set_test)
# UPDATE
set_test.update(lista1)
print(set_test)
# len

# discard
# tenes que pasarle el elemento que queres retirar del set

# remove
# si no encuentra elemento rompe

# operador IN
# in
print(1 in set_test)
print('lp' in set_test)

# not
print(1 not in set_test)
print('lp' not in set_test)

# clear() elimina toda
set_test.clear()
print(set_test)

# pop() elimina el primer que encuentre
set_test.add(tupla1)
set_test.update(lista1)
print(set_test)
set_test.pop()
print(set_test)

# diferencia entre update y add
colores={'rojo','azul'',amarillo'}
# colores.add('dorado')
# colores.add('plateado')
print(colores)
colores.update('dorado','plateado')
print(colores)
#colores.remove('dorado')
print(colores)
colores.discard('plateado')
print(colores)
colores.remove('negro')
print(colores)