# Entrega 1
# Acosta Cesar
#===================================================
# DB
#===================================================
datos_usuarios = {}
#===================================================
# FUNCIONES
#===================================================
def existing_user(db,username):
    for i in db.keys():
        if i == username :
           return True

def pass_validation(db,username,password):
    for k,v in db.items():
        if k==username and v==password:
            return True
        else:
            return False

def login(db):
    print('''
===============================
||      Iniciar Sesion       ||
===============================
''')
    strikes=3
    usu = input('\nUsuario: ')
    while usu == '':
            print('''
 ----------------------------------------
|   El nombre de usuario es obligatorio  |
|         Ingresa nuevamente             |
 ----------------------------------------
            ''')
            usu = input('\nUsuario: ')

    if existing_user(datos_usuarios,usu):
        con = input('\nContraseña: ')
        while con == '':
            print('''
 ----------------------------------------
|  La contraseña ingresada no es válida  |
|               Por favor                |
|           Ingrese nuevamente           |
 ----------------------------------------
            ''')
            con = input('\nContraseña: ')

        while pass_validation(datos_usuarios,usu,con) != True:
            print(f'''
 --------------------------------------
|         Contraseña incorrecta        |
 --------------------------------------
                ''')
            strikes = strikes - 1
            if strikes == 0:
                print(f'''
 --------------------------------------
|      Alcanzaste los 3 intentos       |
|      Regresa al menu principal       |
 --------------------------------------
                ''')
                break
            else:
                print(f'Intentos restantes: {strikes}')
                con = input('\nContraseña: ')
            continue
        else:
            print(f'''
 -----------------------------------------
|               Hola {usu}
|       Inicio de sesion exitoso !!
 -----------------------------------------
            ''')
    else:
            print(f'''
 -------------------------------------------------
|           No existe el usuario "{usu}"
|   Prueba con otro nombre o registra tu cuenta   |
 -------------------------------------------------
                  ''')

def register(db):
        print('''
===============================
||     Registra tu cuenta    ||
===============================

''')
        usu = input('ingrese nombre de usuario: ')

        while usu == '':
            print('''
 ---------------------------------------
|  El nombre de usuario es obligatorio  |
|        Ingresa nuevamente             |
 ---------------------------------------
                  ''')
            usu = input('Ingrese su nombre de usuario: ')

        if existing_user(datos_usuarios,usu):
            print(f'''
 ------------------------------------
|  El nombre de usuario "{usu}"
|       ya fue registrado
 -------------------------------------
                  ''')
        else:
            con = input('Ingrese su nueva contraseña: ')
            while con=='':
                print('''
 ----------------------------------------
|  La contraseña ingresada no es válida  |
|               Por favor                |
|           Ingrese nuevamente           |
 ----------------------------------------
                  ''')
                con = input('Intente con otra contraseña: ')

            db[usu]=con
            print(f'''
 ------------------------------------
|     Su usuario {usu}
|     Se registró exitosamente
 ------------------------------------
                  ''')

def show_user(db):
    print('''
==================================
||      Listado de usuarios     ||
==================================
''')
    print(f'Cantidad de usuarios: {len(db)} \n______________________________________')
    c = 0
    for k, v in db.items():
        c = c + 1
        print(f'''
* Usuario {c}
        Nombre de usuario: {k}
               Contraseña: {v}
______________________________________
              ''')
#===================================================
# MENU
#===================================================
print('''
==================================
===                            ===
||                              ||
||          Bienvenido          ||
||                              ||
===                            ===
==================================
''')
flag = True
while flag:
    print('''
==================================
||        Menu Principal        ||
==================================

- 1) Login
- 2) Registra tu cuenta
- 3) Mostrar Usuarios
- 4) Salir
''')
    option = input('Que deseas hacer? \nIngresa una opcion: ')
    if option == '1':
        login(datos_usuarios)
    elif option == '2':
        register(datos_usuarios)
    elif option == '3':
        show_user(datos_usuarios)
    elif option == '4':
        print('''
==================================
||         Hasta luego!         ||
==================================
__________________________________
''')
        flag = False
    else:
        print('''
========================================
|  ¡ Ingresaste un valor incorrecto !  |
|            Por favor                 |
|   seleccione nuevamente una opcion   |
========================================
''')

