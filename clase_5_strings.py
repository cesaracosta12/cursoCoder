# #clase 5

# # metodos con strings
# cadena = "RIBER te fuiste a la B por puto y cagon"
# print(cadena)
# # upper
# cadena_upper = cadena.upper()
# print(cadena_upper)
# # lower
# cadena_lower = cadena.lower()
# print(cadena_lower)
# # title
# titulo = cadena.title()
# print(titulo)
# # parrafo 
# # primer caracter el may, el resto en min
# parrafo = cadena.capitalize()
# print(parrafo)

# # strings como listas
# # count
# print('Cantidad de caracteres a :' , cadena.count('a'))
# # find (devuelve el indice donde se ubica la primera que encuentra)
# print('indice donde se encuentra la B [' ,cadena.find('B') , ']')
# # rfind devuelve el mismo indice, pero hace la busqueda al reves )
# print('indice donde se encuentra la B al reves [' ,cadena.rfind('B') , ']')

# # split, recorta strings en partes pequeñas de strings
# lista_split = cadena.split() # separa por espacios
# print(lista_split)
# lista_split_2 = cadena.split('a')
# print(lista_split_2)
# lista_split_3 = cadena.split('a ')
# print(lista_split_3)
# lista_split_4 = cadena.split('aasd ')
# print(lista_split_4)

# # join (une una lista de strings en un unico string)
# lista_strings = ['RIBER', 'te', 'fuiste', 'a', 'la', 'B', 'por', 'puto', 'y', 'cagon']
# cadena_strings = ' '.join(lista_strings)
# cadena_strings2 = ' * ** * '.join(lista_strings)
# print(lista_strings)
# print(cadena_strings2)
# print(cadena_strings)

#strip (saca del inicio y del final )
# password = input('ingrese un password: ')
# print(password)
# print(password.strip())
# print(password.strip('asd'))

# replace (reemplaza palabras ggenrando uno nuevo)
cadena8= 'cadena cadena cadeeeena cadena cadena cadena otra carlos'
print(cadena8)
# el numero del final indica la cant de veces que remmplaza
print(cadena8.replace('cadena','otra', 3))

