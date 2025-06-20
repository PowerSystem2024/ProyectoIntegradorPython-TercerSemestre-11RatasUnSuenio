from utilidades.menu import menu
# from modelo.cliente import Cliente
# from modelo.tratamiento import Tratamiento
# from modelo.turno import Turno

if __name__ == '__main__':
    print("=================================================")
    print("********** 11 Sueños **********".center(50))
    print("=================================================")
    print("\n¡Hola! Bienvenido a nuestro menú de servicio\n¿Cómo podemos ayudarte?\n")
    menu()
    
# cliente = Cliente("Luis", "Gonzalez", "luis@gmail.com", "1234567890")
# cliente2 = Cliente("Pepe", "Rigoberto", "pepe@gmail.com", "2442212345")
# print(cliente)
# print(cliente2)
#
# tratamiento = Tratamiento("Masaje", "Masaje relajante", 50.0, 60)
# tratamiento2 = Tratamiento("Facial", "Tratamiento facial rejuvenecedor", 75.0, 45)
# tratamiento3 = Tratamiento("Pedicura", "Cuidado de pies y uñas", 30.0, 30)
# # print(tratamiento)
# # print(tratamiento2)
# # print(tratamiento3)
#
# turno = Turno(cliente, tratamiento, "17-06-25", "18:00")
#
# print(turno)