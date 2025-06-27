from datetime import date
from modelo.cliente import Cliente
from modelo.tratamiento import Tratamiento


class Turno:
    _turnos: list["Turno"] = []

    def __init__(self, cliente: "Cliente", fecha: date, hora: str, tratamiento: "Tratamiento", id=None):
        self._id = id
        self._cliente = cliente
        self._tratamiento = tratamiento
        self._fecha = fecha
        self._hora = hora
        Turno._turnos.append(self)

    @classmethod
    def listar_turnos(cls):
        return cls._turnos

    @property
    def id(self):
        return self._id

    @property
    def cliente(self) -> Cliente:
        return self._cliente

    @property
    def tratamiento(self) -> Tratamiento:
        return self._tratamiento

    @property
    def fecha(self) -> date:
        return self._fecha

    @property
    def hora(self) -> str:
        return self._hora

    def __str__(self) -> str:
        sb = ["Turno:", f"\t Fecha: {self._fecha}  Hora: {self._hora.strip()}", str(self._cliente),
              str(self._tratamiento)]
        return "\n".join(sb)
