# clase_8 

# for (por cada elemento de una coleccion)
# list, tuple, set, dict, string

lista = [0,1,2,'sd',4,5,True,('abc',2),'mentita']

#print('La lista contiene el valor: ', lista[0])
#print('La lista contiene el valor: ', lista[1])

indice = 0
cant_items = len(lista)

# se puede recorrer con while
#
# while indice < cant_items:
    # print('- while - La lista contiene el valor: ', lista[indice])
    # indice += 1
    
    
for elemento in lista:
# X --->   print('- for - La lista contiene el valor: ', lista[elemento]) 
    print('- for - La lista contiene el valor: ', elemento)

# lista_vacia= []
# for i in lista_vacia:
#     print('- for - La lista contiene el valor: ', i)

# con un SET (NO TIENE INDICE EL SET)
#
settt = {0,1,2,'sd',4,5,True,('abc',2),'mentita'}
for item in settt:
    print('- for - El set contiene el valor: ', item)
    
    
# para un dict
#
diccc = {
    'marca':'Ford',
    'ruedas': 5,
    'modelo': ('Ka','Focus','Fiesta'),
    'color':('negro','blanco','azul','amarillo')
}

for elem in diccc:
    print('- for - El diccionario contiene el valor: ', elem)

# es lo mismo que
for elem in diccc.keys():
    print('- for - El diccionario contiene la llave: ', elem)
# por defecto el for pasa por las keys

# si queremos recorrer sus valores debemos usar el .values()
for elem in diccc.values():
    print('- for - El diccionario contiene el valor: ', elem)

# tambien podemos pedirle por cada items
for elem in diccc.items():
    print('- for - El diccionario contiene el item: ', elem)
    
for variable1, variable2 in diccc.items():
    print(f'Llave {variable1}: Valor {variable2}')
    
# range
lista = [1,2,3,4,5,6,7,8,9]
#rango = range(11)
rango = range(1,12)

lista_rango = list(rango)
# lista_rango = list(range(11))
print(rango)
print(lista_rango)

# for valor in lista:
#     print(valor*2)
# for valor in rango:
#     print(valor*2)
for valor in range(1,12):
    print(valor*2)
# tambien permite hacer el salto con el 3er parametro
for valor in range(1,30,3):
    print('RANGO',valor*2)

# enumerate
cadena = 'aguante boca carajo'
indice = 0
for letra in cadena:
    print(f'la letra {letra} esta en el indice {indice}')
    indice +=1
# la funcion enumerate sirve para hacer esto de arriba

indice2 = 0
for indice2 , letra in enumerate(cadena):
    print(f'la letra {letra} esta en el indice {indice2}')
    
listeee= [1,2,3,4,5,33,55,3,21,12,2,2]
for indice, numero in enumerate(listeee):
    print(f'el nro {numero} se encuentra en el indice [{indice}]')