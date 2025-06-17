from modelo.cliente import Cliente
from modelo.tratamiento import Tratamiento

class Turno:
  _turnos: list["Turno"] = []
  
  def __init__(self, cliente: "Cliente", tratamiento: "Tratamiento", dia: str, hora: str):
    self._cliente = cliente
    self._tratamiento = tratamiento
    self._dia = dia
    self._hora = hora
    Turno._turnos.append(self)
    
  @classmethod
  def listar_turnos(cls):
    return cls._turnos
  
  @property
  def cliente(self) -> Cliente:
    return self._cliente
  
  @property
  def tratamiento(self) -> Tratamiento:
    return self._tratamiento
  
  @property
  def fecha(self) -> str:
    return self._dia
  
  @property
  def hora(self) -> str:
    return self._hora
  
  def __str__(self) -> str:
    return (
      f"Turno para: {self._cliente.nombre}\n"
      f"\t{self._tratamiento}\n"
      f"\tDía: {self._dia}, Hora: {self._hora}"
    )