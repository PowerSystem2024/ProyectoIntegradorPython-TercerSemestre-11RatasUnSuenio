from utilidades.utils import Utilidades
from servicio.turno_servicio import TurnoServicio
from dao.tratamiento_dao import TratamientoDAO

class TratamientoServicio:
    @staticmethod
    def mostrar_tratamientos():
        Utilidades.encabezado("Tratamientos")

        for tratamiento in TratamientoDAO.obtener_todos():
            print(tratamiento)

        print("¿Cómo desea continuar? ")
        print("1. Hacer una reserva \n2. Volver al menú principal")

        while True:
            opcion = int(input("> "))
            if opcion == 1 or opcion == 2:
                break
            else:
                print("Opción no válida, por favor intente de nuevo.")

        if opcion == 1:
            TurnoServicio.reservar_turno()
        elif opcion == 2:
            print("Volviendo al menú principal...\n")
