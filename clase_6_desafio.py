# clase 7 
# if

# estado_lluvia = input('esta lloviendo?')
# if estado_lluvia == 'si': 
#     print('uso parawa')
# elif estado_lluvia == 'no':
#     print('no uso parawa')
    
# ------------------
# ejercicio 2

# marvel vs capcom

nombre = input('nombre de usuario: ').capitalize()
preferencia = input('preferencia(Marvel/Capcom): ').upper()

# grupo a marvel
# grupo b capcom

if preferencia == 'MARVEL' and nombre< 'M' or preferencia=='CAPCOM' and nombre >'N' :
    print('Tu grupo es A')
else :
    print('Tu grupo es B')
