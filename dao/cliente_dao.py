import psycopg2
from bd.proyecto_bd import conexion
from modelo.cliente import Cliente

class ClienteDAO:

    @staticmethod
    def guardar(cliente: Cliente):
        cursor = conexion.cursor()
        query = """
            INSERT INTO cliente (nombre, apellido, correo, telefono)
            VALUES (%s, %s, %s, %s)
            RETURNING id;
        """
        valores = (cliente.nombre, cliente.apellido, cliente.correo, cliente.telefono)
        cursor.execute(query, valores)
        cliente._id = cursor.fetchone()[0]  # Asignamos el id generado
        conexion.commit()
        cursor.close()

    @staticmethod
    def obtener_todos():
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, apellido, correo, telefono FROM cliente;")
        registros = cursor.fetchall()
        cursor.close()
        return [Cliente(nombre, apellido, correo, telefono, id) for id, nombre, apellido, correo, telefono in registros]

    @staticmethod
    def eliminar_por_id(id_cliente):
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM cliente WHERE id = %s;", (id_cliente,))
        conexion.commit()
        cursor.close()
