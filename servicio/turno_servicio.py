from servicio.cliente_servicio import ClienteServicio
from utilidades.utils import Utilidades
from modelo.turno import Turno
from dao.tratamiento_dao import TratamientoDAO
from dao.turno_dao import TurnoDAO
from dao.cliente_dao import ClienteDAO
from datetime import date
import calendar
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
    import calendar
    from datetime import date

    dias_semana = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]
    nombre_mes = calendar.month_name[mes]

    ROJO = '\033[91m'
    VERDE = '\033[92m'
    RESET = '\033[0m'

    ancho_col = 14 
    ancho_dia = 10 
    columnas = len(turnos)
    ancho_total = ancho_dia + (ancho_col + 1) * columnas + 1

    print("+" + "-" * (ancho_total - 2) + "+")  #cambio de titulo 
    titulo = f"{nombre_mes} / {anio}"
    print("|" + titulo.center(ancho_total - 2) + "|")
    print("+" + "-" * ancho_dia + "+" + ("-" * ancho_col + "+") * columnas)

    encabezado = f"| {'Día-Hora':<{ancho_dia}}|" + "".join([f" {hora:^{ancho_col - 1}}|" for hora in turnos])
    print(encabezado)
    print("+" + "-" * ancho_dia + "+" + ("-" * ancho_col + "+") * columnas)

    for i, fila in enumerate(cronograma):
        dia_actual = date(anio, mes, i + 1)
        dia_nombre = dias_semana[dia_actual.weekday()]
        dia_texto = f"{dia_nombre} {i+1}"
        linea = f"| {dia_texto:<{ancho_dia - 1}}|"

        for estado in fila:
            estado = estado.strip()
            if estado == "":
                texto_plano = "Disponible"
                texto = f"{VERDE}{texto_plano:^{ancho_col - 1}}{RESET}"
            elif estado == "Reservado":
                texto_plano = "Reservado"
                texto = f"{ROJO}{texto_plano:^{ancho_col - 1}}{RESET}"
            elif estado == "Cerrado":
                texto_plano = "Cerrado"
                texto = f"{texto_plano:^{ancho_col - 1}}"
            else:
                texto_plano = estado
                texto = f"{texto_plano:^{ancho_col - 1}}"

            linea += f"{texto}|"

        print(linea)
        # Línea separadora después de cada fila
        print("+" + "-" * ancho_dia + "+" + ("-" * ancho_col + "+") * columnas)


def cargar_turnos():
    return [
        "09:00", "10:30", "12:00", "13:30", "15:00", "16:30", "18:00"
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
    return all(celda.strip() == "Cerrado" for celda in cronograma[dia])


def comprobar_fecha_turno(dia, turno, cronograma):
    if cronograma[dia][turno].strip() == "Reservado":
        print("\n--- El día y turno seleccionado están reservados. Por favor ingrese otro día o turno ---")
        time.sleep(1.5)
        return True
    else:
        cronograma[dia][turno] = "Reservado"
        return False
