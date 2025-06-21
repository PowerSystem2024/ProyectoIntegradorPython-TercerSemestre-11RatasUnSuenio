# from utilidades.menu import menu
# from utilidades.cabecera import cabecera
from modelo.cliente import Cliente
from modelo.tratamiento import Tratamiento
from modelo.turno import Turno

# if __name__ == '__main__':
#     cabecera()
#     menu()
    
cliente = Cliente("Luis", "Gonzalez", "luis@gmail.com", "1234567890")
cliente2 = Cliente("Pepe", "Rigoberto", "pepe@gmail.com", "2442212345")
print(cliente)
print(cliente2)

tratamiento = Tratamiento("Masaje", "Masaje relajante", 50.0, 60)
tratamiento2 = Tratamiento("Facial", "Tratamiento facial rejuvenecedor", 75.0, 45)
tratamiento3 = Tratamiento("Pedicura", "Cuidado de pies y uñas", 30.0, 30)
# print(tratamiento)
# print(tratamiento2)
# print(tratamiento3)

turno = Turno(cliente, tratamiento, "17-06-25", "18:00")

print(turno)