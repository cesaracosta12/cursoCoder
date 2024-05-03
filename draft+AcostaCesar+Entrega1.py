# entrega 1

#===================================================    
# DB
#===================================================    

datos_usuarios = {}

#===================================================    
# FUNCIONES
#===================================================    

def existe_usuario(db,username):
    for i in db.keys():
        if i == username :
           return True

def login(db):
    usu = input('ingrese nombre de usuario: ')
    con = input('ingrese contraseña: ') 
    print(f'usuario: <{usu}>  -- contraseña: <{con}> ')
    # buscar si existe el usuario
    
    # su contraseña es válida?
    # es nula?
    
    
def register(db):
        
        usu = input('ingrese nombre de usuario: ')
        
        while usu == '':
            print('Ingresaste vacio, ingresa nuevamente')
            usu = input('ingrese nombre de usuario: ')

        if existe_usuario(datos_usuarios,usu):
            print(f'El nombre de usuario "{usu}" ya fue registrado')  
        else:
            
            con = input('ingrese contraseña: ')
            
            while con=='':
                print('Ingresaste vacio, ingresa nuevamente')
                con = input('ingrese contraseña: ')
                 
            db[usu]=con
            print('Se registró exitosamente')

    
#=================================================== 
# MENU
#===================================================    

flag = True
while flag:
    print('''
*******************************
**********   MENU   ***********
*******************************

- 1) Login
- 2) Registrarse
- 3) Buscar usuarios
- 4) Salir

''')
    option = input('Ingrese una opcion: ')
    print('========================================')
    if option == '1':
        print('''
*******************************
**********   LOGIN   **********
*******************************

''')
        login(datos_usuarios)

    elif option == '2':
        print('''
*******************************
*******   REGISTRARSE   *******
*******************************

''')
        register(datos_usuarios) 
        
    elif option == '3':
        print('''
*******************************
*****   BUSCAR USUARIO   *****
*******************************

''')
        #usu = input('ingrese nombre de usuario: ')
        #search(usu)
        
    elif option == '4':
        print('''
******************************              
*****    Hasta Pronto    *****
****************************** 
''')
        flag = False
    else:
        print('''

*****-_ Ingresaste un valor incorrecto _-*****')
    Por favor ingresa nuevamente 
    
''')
    
