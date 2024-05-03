# clase 5 
# diccionarios

auto = {
    'motor':'v8',
    'anio': '2012',
    'vidrios':(6,'blindadas'),
    'pasajeros':4
}

# get 
# (obtiene el valor de una clave y si no esta devuelve el 2do dato)
# .get('ricardo',False)

# keys (devuelve un listado de los valores de las keys de un dict)
print(auto.keys())

# values (devuelve un listado de los valores de las values de un dict)
print(auto.values())

# items (devuelve un listado de los valores de tuplas de un dict)
print(auto.items())
