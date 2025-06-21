from modelo.cliente import Cliente
from modelo.tratamiento import Tratamiento

class Turno:
  _turnos: list["Turno"] = []
  
  def __init__(self, cliente: "Cliente", dia: str, hora: str, tratamiento: "Tratamiento", id=None):
    self._id = id
    self._cliente = cliente
    self._tratamiento = tratamiento
    self._dia = dia
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
  def fecha(self) -> str:
    return self._dia
  
  @property
  def hora(self) -> str:
    return self._hora

  def __str__(self) -> str:
    sb = []
    sb.append("Turno:")
    sb.append(f"\t Fecha: {self._dia}/10/24  Hora: {self._hora.strip()}")
    sb.append(str(self._cliente))  # Esto depende de que Cliente también tenga __str__
    sb.append(str(self._tratamiento))  # Esto depende de que Tratamiento también tenga __str__
    return "\n".join(sb)