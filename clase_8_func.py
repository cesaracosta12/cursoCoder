# funciones

frase = 'hola señor kioskero'
print('Usando len() -> ',len(frase))

def contador_caracteres(frase):
    contador = 0
    for letra in frase:
        contador += 1
    return(contador)
print('Usando funcion propia -> ', contador_caracteres(frase))

# ejercicio

def welcome(ciudad):
    print(f'Bienvenido a {ciudad} !!')
    
welcome('Cordobaaaaa')
#
welcome(input('Ingrese nombre de ciudad: '))