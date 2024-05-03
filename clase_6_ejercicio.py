# clase 7
# ejercicio practico

def generacion(anio):
    if anio >= 1900 and anio <= 1909:
        print('generacion 00')
    elif anio >= 1910 and anio <= 1919:
        print('generacion 10')
    elif anio >= 1920 and anio <= 1929:
        print('generacion 20')
    elif anio >= 1930 and anio <= 1939:
        print('generacion 30')
    elif anio >= 1940 and anio <= 1949:
        print('generacion 40')
    elif anio >= 1950 and anio <= 1959:
        print('generacion 50')
    elif anio >= 1960 and anio <= 1969:
        print('generacion 60')
    elif anio >= 1970 and anio <= 1979:
        print('generacion 70')
    elif anio >= 1980 and anio <= 1989:
        print('generacion 80')
    elif anio >= 1990 and anio <= 1999:
        print('generacion 90')
    else:
        print('NO SE ENCONTRO GENERACION')

print('-----------------------')
anio = int(input('ingrese el anio de nacimiento:'))
print('RESULTADO : ')
generacion(anio)

