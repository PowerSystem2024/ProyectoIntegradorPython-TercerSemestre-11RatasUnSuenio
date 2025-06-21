from utilidades.menu import menu
from bd.crearTablas import crear_tablas

if __name__ == '__main__':

    crear_tablas() # Creamos todas las tablas antes de iniciar el programa

    print("=================================================")
    print("********** 11 Sueños **********".center(50))
    print("=================================================")
    print("\n¡Hola! Bienvenido a nuestro menú de servicio\n¿Cómo podemos ayudarte?\n")
    menu()
