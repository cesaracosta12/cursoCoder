# clase 9

# asignacion de argumentos por nombre

def resta(num1,num2):
    return num1-num2
print(resta(1,2))
print(resta(2,1))
print(resta(1,num2=2))
print(resta(num2=2,num1=1))

# este caso da error
# print(resta(num2=2,1)) 
# print(resta(1,num2=2)) 
# una vez definido el argumento por nombre, python espera que uses siempre los nombres

# funciones con valores por defecto
# puedo definir los valores de todas las variables por defecto
def funcion(var0,var1=10,var2=20,var3=30):
    return var0,var1,var2,var3
#print(funcion())
print(funcion(1,2))
print(funcion(9999))
print(funcion('primera variable',var3='kirikocho'))

# cuando no tenemos todos los argumentos para pasar usamos
# parametros indefinidos

# *args
# es una tupla
def suma(*args): # def suma(*variable):
    #print(type(args))
    #print(args)
    suma =0
    for valor in args:
        suma += valor
    return suma
    
print(suma())
print(suma(1))
print(suma(1,2,4))
print(suma(53,31))

# otro ejemplo

def concatenado(*listas):
    conca =[]
    for valor in listas:
        conca += valor
    return conca

print(concatenado([1,2,3,5],[55,8,77,323,0],[23,45,0]))

# **kwargs
# es un diccionario que le tengo que pasar argumentos por nombre

def mostrar(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for llave, valor in kwargs.items():
        print(f'llave: {llave} - valor: {valor}')

mostrar(nombre='Edinson',apellido='Cavani',posicion='Delantero',nro=10,pais='UY')

def prueba_multi_params(numero,*args,**kwargs):
    print(numero)
    print(args)
    print(kwargs)
    
prueba_multi_params(15,16,True,-12,'Merentiel',marca='Ford',modelo='ka')