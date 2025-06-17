class Cliente:
    
  def __init__(self, nombre: str, apellido: str, correo: str, telefono: str):
    self._id = Cliente._generar_id()
    self._nombre = nombre
    self._apellido = apellido
    self._correo = correo
    self._telefono = telefono
    
  _contador = 1
  
  @classmethod
  def _generar_id(cls):
    id_ = cls._contador
    cls._contador += 1
    return id_
    
  @property
  def nombre(self) -> str:
    return self._nombre
  
  @nombre.setter
  def nombre(self, nombre: str):
    self._nombre = nombre
  
  @property
  def apellido(self) -> str:
    return self._apellido
  
  @apellido.setter
  def apellido(self, apellido: str):
    self._apellido = apellido
  
  @property
  def correo(self) -> str:
    return self._correo
  
  @correo.setter
  def correo(self, correo: str):
    self._correo = correo
  
  @property
  def telefono(self) -> str:
    return self._telefono
  
  @telefono.setter
  def telefono(self, telefono: str):
    self._telefono = telefono
  
  @property
  def id(self) -> int:
    return self._id
  
  def __str__(self) -> str:
    return (
      f"Cliente {self.id}:\n"
      f"\tNombre: {self.nombre}, Apellido: {self.apellido}, "
      f"Correo: {self.correo}, Telefono: {self.telefono}"
    )
