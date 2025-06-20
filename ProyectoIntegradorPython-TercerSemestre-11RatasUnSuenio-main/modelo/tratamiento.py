class Tratamiento:
  _contador = 1
  _tratamientos: list["Tratamiento"] = []
  
  def __init__(self, nombre: str, descripcion: str, precio: float, duracion: int):
    self._nombre = nombre
    self._descripcion = descripcion
    self._precio = precio
    self._duracion = duracion
    self._id = Tratamiento._contador
    Tratamiento._contador += 1
    Tratamiento._tratamientos.append(self)

  @classmethod
  def listar_tratamientos(cls):
    return cls._tratamientos
  
  @property
  def nombre(self) -> str:
    return self._nombre
  
  @nombre.setter
  def nombre(self, nombre: str):
    self._nombre = nombre
  
  @property
  def descripcion(self) -> str:
    return self._descripcion
  
  @descripcion.setter
  def descripcion(self, descripcion: str):
    self._descripcion = descripcion
  
  @property
  def precio(self) -> float:
    return self._precio
  
  @precio.setter
  def precio(self, precio: float):
    self._precio = precio
  
  @property
  def duracion(self) -> int:
    return self._duracion
  
  @duracion.setter
  def duracion(self, duracion: int):
    self._duracion = duracion
  
  def __str__(self) -> str:
    return (
      f"Tratamiento {self._id}:\n"
      f"\tNombre: {self._nombre} \n\tDescripcion: {self._descripcion} "
      f"\n\tDuración: {self._duracion} minutos \n\tPrecio: ${self._precio} \n"
    )

Tratamiento("Reflexología","Terapia para tratar puntos dolorosos a través de masajes podales",7000, 60);
Tratamiento("Masaje descontracturante", "Ideal para relajar la musculatura y disolver contracturas",10000, 60);
Tratamiento("Pulido corporal e hidratación", "Tratamiento corporal hiper estimulante que elimina las células muertas",23000,60)