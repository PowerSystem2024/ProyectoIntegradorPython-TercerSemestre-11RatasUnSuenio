from bd.proyecto_bd import conexion
from modelo.tratamiento import Tratamiento

class TratamientoDAO:

    @staticmethod
    def guardar(tratamiento: Tratamiento):
        cursor = conexion.cursor()
        query = """
            INSERT INTO tratamiento (nombre, descripcion, precio, duracion)
            VALUES (%s, %s, %s, %s)
            RETURNING id;
        """
        valores = (tratamiento.nombre, tratamiento.descripcion, tratamiento.precio, tratamiento.duracion)
        cursor.execute(query, valores)
        tratamiento._id = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()

    @staticmethod
    def obtener_todos():
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, descripcion, precio, duracion FROM tratamiento;")
        resultados = cursor.fetchall()
        cursor.close()
        return [Tratamiento(nombre, descripcion, float(precio), duracion, id) for id, nombre, descripcion, precio, duracion in resultados]

    @staticmethod
    def existe(nombre: str):
        cursor = conexion.cursor()
        cursor.execute("SELECT 1 FROM tratamiento WHERE nombre = %s LIMIT 1;", (nombre,))
        existe = cursor.fetchone() is not None
        cursor.close()
        return existe
