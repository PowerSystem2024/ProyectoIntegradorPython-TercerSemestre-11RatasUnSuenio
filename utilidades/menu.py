from utilidades.contacto import Contacto
from servicio.tratamiento_servicio import TratamientoServicio
from servicio.turno_servicio import TurnoServicio
def menu():
    opcion = 0
    while opcion != 4:
        print("-------------------------------------------------")
        print(">> MENÚ <<".center(50))
        print("-------------------------------------------------")
        print("1. Nuestros servicios")
        print("2. Reserva Online")
        print("3. Contacto\n")
        print("4. Salir\n")

        opcion = int(input("Elija una opción para continuar: "))
        if opcion == 1:
            TratamientoServicio.mostrar_tratamientos()
        elif opcion == 2:
            print("Reserva Online...")
            TurnoServicio.reservar_turno()
        elif opcion == 3:
            Contacto.contacto()
        elif opcion == 4:
            print("¡Gracias por usar nuestros servicios!")
        else:
            print("Opción no válida, por favor intenta de nuevo.")