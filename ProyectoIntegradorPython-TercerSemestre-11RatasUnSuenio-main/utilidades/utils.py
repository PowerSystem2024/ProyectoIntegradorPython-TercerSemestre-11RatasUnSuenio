import re

class Utilidades:
    @staticmethod
    def encabezado(encabedazado: str):
        print("\n-------------------------------------------------")
        print("Menú   >>" + encabedazado)
        print("-------------------------------------------------")
        print()

    @staticmethod
    def encabezado_contacto(encabedazado: str, encabedazado2: str):
        print("\n-------------------------------------------------")
        print("Menú   >>" + encabedazado + " >> " + encabedazado2)
        print("-------------------------------------------------")
        print()

    @staticmethod
    def validar_correo(correo: str) -> bool:
        EMAIL_REGEX = r'^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$'
        return bool(re.match(EMAIL_REGEX, correo))

    @staticmethod
    def validar_telefono(telefono: str) -> bool:
        TELEFONO_REGEX = r'^\+?[0-9]{7,15}$'
        return bool(re.match(TELEFONO_REGEX, telefono))