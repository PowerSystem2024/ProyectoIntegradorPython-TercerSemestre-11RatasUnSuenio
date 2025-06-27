from utilidades.utils import Utilidades
from modelo.cliente import Cliente
from dao.cliente_dao import ClienteDAO


class ClienteServicio:
    @staticmethod
    def cargar_cliente():
        while True:
            nombre = input("\nNombre: ").strip()
            if len(nombre) > 2:
                break
            print("\n-- Ingrese un nombre válido (más de 2 caracteres) --")

        while True:
            apellido = input("Apellido: ").strip()
            if len(apellido) > 2:
                break
            print("\n-- Ingrese un apellido válido (más de 2 caracteres) --\n")

        while True:
            correo = input("Correo: ").strip()
            if Utilidades.validar_correo(correo):
                break
            print("\n-- El correo ingresado no es válido --\n")

        while True:
            telefono = input("Teléfono: ").strip()
            if Utilidades.validar_telefono(telefono):
                break
            print("\n-- El número de teléfono es inválido --\n")

        cliente = Cliente(nombre, apellido, correo, telefono)
        ClienteDAO.guardar(cliente)
        return cliente
