# clase 14
import sys

print(sys.argv)
# el primer valor de sys.argv es el nombre del archivo

valores = sys.argv[1:]

suma = 0
for valor in valores:
    suma = suma + int(valor)
    
print(f'La suma de{valores} es {suma}')
