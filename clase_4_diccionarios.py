#diccionario
auto = {
    'motor':'v8',
    'anio': '2012',
    'vidrios':(6,'blindadas'),
    'pasajeros':4
}

#se usa .get(valor) para acceder
# si en .get('elemento')
print(auto.get('motor'))
print(auto)
# no encuentra muetra error
# podemos insetar que queremos que muestre si no encuentra .get('elemento','mensaje de error')
auto['motor']='ssda'
print(auto)
auto['modelo'] = 2021
print(auto)
#update
auto.update({'color':'rojo','ruedas':5,'motor':'v21'})
print(auto)
#len
print(len(auto))
#del elimina
del auto['vidrios']
print(auto)
print(auto.get('vidrios','no encontro vidrios'))
print(auto)
# in
print('motor' in auto)
print('v8' in auto)
print('v21' in auto)
#clear

# pop
mentita = auto.pop('color')
print(auto)
print(mentita)
mentita = auto.pop('kaka','mensaje de error NO ENCONTRO')
print(mentita)
