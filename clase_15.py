# clase 15 paaaaaaaaaaa

# Archivos

# open() y write()
# open('ubicacion de archivo .txt','formato de open' )
# i =1
# nombre=input('Ingrese nombre: ')
# print(nombre)
# archivo_abierto = open (f'comprobante{i}.txt','w')
# # al write le tengo que pasar un string
# archivo_abierto.write(nombre)
# archivo_abierto.close()

# # v2
# datos_persona = {
#     'nombre':input('Ingrese nombre: '),
#     'apellido' : input('ingrese apellido: '),
#     'edad': input('ingrese edad: ')
# }

# archivo_abierto = open (f'test_file.txt','w')
# archivo_abierto.write(f'Datos de {datos_persona["nombre"]} {datos_persona["apellido"]} edad: {datos_persona["edad"]} \n')
# archivo_abierto.write(f'''
#         Datos de{datos_persona["nombre"]} {datos_persona["apellido"]} edad: {datos_persona["edad"]}
#         ''')
# archivo_abierto.close()

# # append
# # agrega al archivo
# nombre=input('Ingrese nombre: ')
# print(nombre)
# archivo_abierto = open (f'mentita_file.txt','a')
# archivo_abierto.write(nombre)
# archivo_abierto.close()


# # read()
# nombre=input('Ingrese nombre: ')
# archivo_abierto = open(f'test_file.txt','w')
# archivo_abierto.write(nombre)
# archivo_abierto.close()

# podemos ponerlo pero por defecto toma como 'r'
# archivo_abierto = open(f'test_file.txt','r')
# valor_archivo = ''
# # read() devuelve un string con todo lo que tiene
# valor_archivo= archivo_abierto.read() 
# print(valor_archivo)
# print([valor_archivo])
# archivo_abierto.close()

# v2
# archivo_abierto = open(f'test_file.txt','r')
# valor_archivo = ''
# # read() devuelve un string con todo lo que tiene
# valor_archivo= archivo_abierto.read() 
# print(valor_archivo)
# print([valor_archivo])
# valor_archivo_2da_vuelta= archivo_abierto.read() 
# print(valor_archivo_2da_vuelta)# el puntero de lectura quedo al final
# archivo_abierto.close()

# # readline()
# archivo_abierto = open(f'test_file.txt','r')
# # readline() devuelve un string con una linea
# linea1= archivo_abierto.readline() 
# linea2= archivo_abierto.readline() 
# print(linea1)
# print(linea2)
# archivo_abierto.close()

# # generamos una lista con todas las lineas de un archivo
# archivo_abierto = open(f'test_file.txt','r')
# lineas = archivo_abierto.readlines()
# print(lineas)
# archivo_abierto.close()

# # seek() se puede usar para cualquier tipo de operacion
# mueve el puntero
# archivo_abierto = open(f'test_file.txt','r')
# valor_archivo = archivo_abierto.read()
# print(valor_archivo)
# print('#############')
# print(valor_archivo) # me muestra todo porque lo tengo capturado en una variable
# print('#############')
# print(archivo_abierto.read()) # no muestra nada porque el puntero quedo en la ultima linea y posicion
# print('#############')
# archivo_abierto.seek(4) # mueve el puntero a la posicion que le indico por param
# print(archivo_abierto.read())
# archivo_abierto.close()

# JSON 

# debemos importar json
import json

# ejemplo de dicciontario
dicc = {
    'key1':'value1',
    'key2':False,
    'key3':None,
    'key4':['asd',123]
}

# usamos el contextmananger (with)
# dump()
with open('archivo_de_no_json.json','w') as archivo_abierto:
    json.dump(dicc, archivo_abierto, indent=4)
    # no es necesario close()

# read json
# load()
with open('archivo_de_no_json.json','r') as archivo_abierto:
    datos = json.load(archivo_abierto)
    print(datos)
print('********')
print(datos)