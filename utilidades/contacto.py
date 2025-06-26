import time
from utilidades.utils import Utilidades

class Contacto:
    @staticmethod
    def contacto():
        while True:
            Utilidades.encabezado("Contacto")
            print("¡Estaremos encantados de atenderte!\n")
            Contacto.horario()
            print()
            print(" - Teléfono: +54 3492 30-2771")
            print(" - Email: Beautyesteticarafaela@gmail.com")
            print(" - Dirección: Urquiza 275, Rafaela. Santa Fé, Argentina.\n")
            print(" ¡Contáctanos!")
            print("  1. Llamar")
            print("  2. Enviar un correo")
            print("  3. Volver al menú principal\n")

            opcion = input("¿Cómo deseas continuar? > ").strip()
            if opcion == "1":
                Contacto.llamar()
            elif opcion == "2":
                Contacto.enviar_correo()
            elif opcion == "3":
                break
            else:
                print("Opción inválida. Intenta de nuevo.\n")

    @staticmethod
    def llamar():
        Utilidades.encabezado_contacto("Contacto", "Llamando")
        print("Llamando", end="")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(1)
        print("\nLlamada finalizada.\n")

    @staticmethod
    def enviar_correo():
        Utilidades.encabezado_contacto("Contacto", "Enviar correo")
        Contacto.pedir_datos()
        print("\nMensaje enviado con éxito!\n")
        time.sleep(2)

    @staticmethod
    def pedir_datos():
        while True:
            nombre = input("Nombre completo: ").strip()
            if len(nombre) > 5:
                break
            print("\n-- Ingrese un nombre válido (más de 5 caracteres) --\n")

        while True:
            telefono = input("Teléfono: ").strip()
            if Utilidades.validar_telefono(telefono):
                break
            print("\n-- El número de teléfono es inválido --\n")

        while True:
            correo = input("Correo: ").strip()
            if Utilidades.validar_correo(correo):
                break
            print("\n-- El correo ingresado no es válido --\n")

        while True:
            mensaje = input("Mensaje: ").strip()
            if len(mensaje) > 5:
                break
            print("\n-- Ingrese un mensaje válido (más de 5 caracteres) --\n")

    @staticmethod
    def horario():
        horarios = [
            ("Lun", "09:00 - 18:00"),
            ("Mar", "09:00 - 18:00"),
            ("Mié", "09:00 - 18:00"),
            ("Jue", "09:00 - 18:00"),
            ("Vie", "09:00 - 18:00"),
            ("Sáb", "  CERRADO  "),
            ("Dom", "  CERRADO  "),
        ]
        print(" Horarios - Septiembre 2024")
        for dia, hora in horarios:
            print(f"   | {dia}: {hora} |")
