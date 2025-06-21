from bd.proyecto_bd import conexion
from modelo.turno import Turno
from modelo.cliente import Cliente
from modelo.tratamiento import Tratamiento

class TurnoDAO:

    @staticmethod
    def guardar(turno: Turno):
        cursor = conexion.cursor()
        query = """
            INSERT INTO turno (cliente_id, tratamiento_id, fecha, hora)
            VALUES (%s, %s, %s, %s)
            RETURNING id;
        """
        valores = (
            turno.cliente.id,
            turno.tratamiento.id,
            turno.fecha,
            turno.hora
        )
        cursor.execute(query, valores)
        turno._id = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()

    @staticmethod
    def obtener_todos(clientes: list[Cliente], tratamientos: list[Tratamiento]):
        cursor = conexion.cursor()
        cursor.execute("SELECT id, cliente_id, tratamiento_id, fecha, hora FROM turno;")
        resultados = cursor.fetchall()
        cursor.close()

        # Mapeo por id para acceder rápido
        cliente_map = {c.id: c for c in clientes}
        tratamiento_map = {t.id: t for t in tratamientos}

        turnos = []
        for id, cliente_id, tratamiento_id, fecha, hora in resultados:
            cliente = cliente_map.get(cliente_id)
            tratamiento = tratamiento_map.get(tratamiento_id)
            turnos.append(Turno(cliente, str(fecha), str(hora), tratamiento, id))
        return turnos
