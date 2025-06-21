class Cliente:
    def __init__(self, nombre, apellido, correo, telefono, id=None):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
        self._telefono = telefono

    # Getters y setters
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, valor):
        self._apellido = valor

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        self._correo = valor

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        self._telefono = valor

    @property
    def id(self):
        return self._id

    def __str__(self):
        return (
            f"Cliente {self.id}: \n"
            f"\t Nombre: {self.nombre}, "
            f"Apellido: {self.apellido}, "
            f"Correo: {self.correo}, "
            f"Telefono: {self.telefono} "
        )