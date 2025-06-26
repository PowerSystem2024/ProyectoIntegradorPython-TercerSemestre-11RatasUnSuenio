from servicio.cliente_servicio import ClienteServicio
from utilidades.utils import Utilidades
from modelo.turno import Turno
from dao.tratamiento_dao import TratamientoDAO  # USAMOS DAO
import random
import time

class TurnoServicio:
    @staticmethod
    def reservar_turno():
        continua_reservando = True

        while continua_reservando:
            print("\n+ Es momento de poner tus datos personales")
            nuevo_cliente = ClienteServicio.cargar_cliente()

            tratamientos_disponibles = TratamientoDAO.obtener_todos()

            while True:
                Utilidades.encabezado("Reserva Online")
                print("+ Ingresa uno de los siguientes tratamientos\n")
                for i, tratamiento in enumerate(tratamientos_disponibles, start=1):
                    print(f"{i}. {tratamiento}")

                try:
                    tratamiento_indice = int(input("> "))
                    if tratamiento_indice < 1 or tratamiento_indice > len(tratamientos_disponibles):
                        raise ValueError()
                    break
                except ValueError:
                    print("\n--- ¡¡Ingrese bien la opción!! ---\n")
                    time.sleep(0.5)

            tratamiento_elegido = tratamientos_disponibles[tratamiento_indice - 1]
            print("\n+ Ingresa la fecha\n¡A continuación se le mostrarán los turnos disponibles!")

            cronograma = llenar_matrices()
            turnos = cargar_turnos()

            while True:
                mostrar_turnos(turnos, cronograma)
                try:
                    dia = int(input("\nIngresa el día de tu reserva: "))
                    if validar_dia_cerrado(dia - 1, cronograma):
                        print(f"\n--- El día '{dia}' el establecimiento está cerrado. Por favor ingrese otro día ---")
                        time.sleep(1.5)
                        continue
                    break
                except ValueError:
                    print("Día inválido")

            print()
            for i, turno in enumerate(turnos, start=1):
                print(f"{i}. {turno.strip()}")

            while True:
                try:
                    turno_hora = int(input("\nElija el turno de tu reserva (1-7): "))
                    if comprobar_fecha_turno(dia - 1, turno_hora - 1, cronograma):
                        print("Turno ya ocupado. Elegí otro.")
                        continue
                    break
                except ValueError:
                    print("Hora inválida")

            nuevo_turno = Turno(nuevo_cliente, dia, turnos[turno_hora - 1], tratamiento_elegido)
            print("\n+ Reserva registrada\n")
            time.sleep(0.5)
            print(nuevo_turno)
            time.sleep(2)

            seguir = input("¿Desea reservar otro turno o servicio? (S/N): ").strip().lower()
            if seguir != 's':
                continua_reservando = False

        print("\n¡Gracias por elegirnos!")
        time.sleep(2)
        print("Volviendo al menú principal...")

def mostrar_turnos(turnos, cronograma):
    num_dias = 30
    num_turnos = 7
    cont1 = 0
    dias = ["Sab ", "Dom ", "Lun ", "Mar ", "Mie ", "Jue ", "Vie "]

    print()
    print("                                                  ___________________")
    print("                                                 | Septiembre / 2024 |")
    print("       ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    print(f"Día\\Hs | {turnos[0]} || {turnos[1]} || {turnos[2]} || {turnos[3]} || {turnos[4]} || {turnos[5]} || {turnos[6]} |")

    for i in range(num_dias):
        print("       " + "¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯" * num_turnos)

        dia_nombre = dias[cont1]
        dia_num = f"{i + 1}: " if i < 9 else f"{i + 1}:"
        print(f"{dia_nombre}{dia_num}", end='')

        for j in range(num_turnos):
            turno = cronograma[i][j]
            if turno != "":
                print(f"|{turno}|", end='')
            else:
                print("|             |", end='')

        print()

        if i == 29:
            print("       " + "¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯" * num_turnos)

        cont1 = (cont1 + 1) % 7

def cargar_turnos():
    return [
        "   09:00   ",
        "   10:30   ",
        "   12:00   ",
        "   13:30   ",
        "   15:00   ",
        "   16:30   ",
        "   18:00   "
    ]

def llenar_matrices():
    cronograma = [['' for _ in range(7)] for _ in range(30)]
    cont = 0
    cont1 = 1

    for i in range(len(cronograma)):
        for j in range(len(cronograma[0])):
            num_azar = random.randint(0, 1)
            if i != cont and i != cont1:
                cronograma[i][j] = "             " if num_azar == 0 else "  Reservado  "
            else:
                cronograma[i][j] = "   Cerrado   "

        if i == cont:
            cont += 7
        if i == cont1:
            cont1 += 7

    return cronograma

def validar_dia_cerrado(dia, cronograma):
    return all(cronograma[dia][i] == "   Cerrado   " for i in range(7))

def comprobar_fecha_turno(dia, turno, cronograma):
    if cronograma[dia][turno] == "  Reservado  ":
        print("\n--- El día y turno seleccionado están reservados. Por favor ingrese otro día o turno ---")
        time.sleep(1.5)
        return True
    else:
        cronograma[dia][turno] = "  Reservado  "
        return False
