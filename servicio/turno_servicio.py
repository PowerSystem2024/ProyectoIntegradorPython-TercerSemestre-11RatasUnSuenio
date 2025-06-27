from servicio.cliente_servicio import ClienteServicio
from utilidades.utils import Utilidades
from modelo.turno import Turno
from dao.tratamiento_dao import TratamientoDAO  # USAMOS DAO
from dao.turno_dao import TurnoDAO
from datetime import date, datetime, timedelta
from dao.cliente_dao import ClienteDAO
import calendar
import random
import time

class TurnoServicio:
    @staticmethod
    def reservar_turno():
        hoy = date.today()
        anio = hoy.year
        mes = hoy.month
        continua_reservando = True

        while continua_reservando:
            print("\n+ Es momento de poner tus datos personales")
            nuevo_cliente = ClienteServicio.cargar_cliente()

            tratamientos_disponibles = TratamientoDAO.obtener_todos()
            clientes_disponibles = ClienteDAO.obtener_todos()

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

            turnos = cargar_turnos()
            dias_del_mes = calendar.monthrange(anio, mes)[1]
            cronograma = llenar_matrices(
                dias_del_mes,
                turnos,
                anio,
                mes,
                clientes_disponibles,
                tratamientos_disponibles
            )

            while True:
                mostrar_turnos(turnos, cronograma, anio, mes)
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
            fecha_turno = date(anio, mes, dia)
            nuevo_turno = Turno(nuevo_cliente, fecha_turno, turnos[turno_hora - 1].strip(), tratamiento_elegido)
            TurnoDAO.guardar(nuevo_turno)
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

def mostrar_turnos(turnos, cronograma, anio, mes):
    dias_semana = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]
    nombre_mes = calendar.month_name[mes]

    ROJO = '\033[91m'
    VERDE = '\033[92m'
    RESET = '\033[0m'

    print()
    print(f"                                                  ___________________")
    print(f"                                                 | {nombre_mes} / {anio} |")
    print("       ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    print(f"Día\\Hs | {' || '.join([f'{hora:^11}' for hora in turnos])} |")

    for i, fila in enumerate(cronograma):
        dia_actual = date(anio, mes, i + 1)
        dia_nombre = dias_semana[dia_actual.weekday()]
        dia_num = f"{i + 1:2d}:"

        print("       " + "¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯" * len(turnos))
        print(f"{dia_nombre} {dia_num}", end='')

        for estado in fila:
            if estado.strip() == "":
                texto = f"{VERDE} Disponible {RESET}"
            elif estado.strip() == "Reservado":
                texto = f"{ROJO}Reservado{RESET}  "
            else:
                texto = estado  # "Cerrado" u otro valor

            print(f"| {texto:^11} |", end='')

        print()

    print("       " + "¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯" * len(turnos))

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

def llenar_matrices(dias_mes, turnos, anio, mes, clientes, tratamientos):
    cronograma = [['' for _ in range(len(turnos))] for _ in range(dias_mes)]
    turnos_reservados = TurnoDAO.obtener_todos(clientes, tratamientos)

    for i in range(dias_mes):
        dia_actual = date(anio, mes, i + 1)
        es_finde = dia_actual.weekday() in [5, 6]

        for j, hora in enumerate(turnos):
            if es_finde:
                cronograma[i][j] = "Cerrado"
            else:
                reservado = any(
                    t.fecha == dia_actual and t.hora.strftime("%H:%M") == hora
                    for t in turnos_reservados
                )
                cronograma[i][j] = "Reservado" if reservado else ""

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
