from bd.proyecto_bd import conexion
from modelo.tratamiento import Tratamiento
from dao.tratamiento_dao import TratamientoDAO

def crear_tablas():
    cursor = conexion.cursor()

    # Crear tabla cliente
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cliente (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        apellido VARCHAR(100) NOT NULL,
        correo VARCHAR(100),
        telefono VARCHAR(20)
    );
    """)

    # Crear tabla tratamiento
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tratamiento (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        descripcion TEXT,
        precio NUMERIC(10, 2),
        duracion INTEGER
    );
    """)

    # Crear tabla turno
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS turno (
        id SERIAL PRIMARY KEY,
        cliente_id INTEGER REFERENCES cliente(id),
        tratamiento_id INTEGER REFERENCES tratamiento(id),
        fecha DATE,
        hora TIME
    );
    """)

    # ✅ Confirmamos la creación antes de insertar nada
    conexion.commit()
    cursor.close()
    print("✔ Tablas creadas.")

    # 👇 Esto se ejecuta DESPUÉS de crear las tablas
    tratamientos = [
        Tratamiento("Reflexología", "Terapia para tratar puntos dolorosos a través de masajes podales", 7000, 60),
        Tratamiento("Masaje descontracturante", "Ideal para relajar la musculatura y disolver contracturas", 10000, 60),
        Tratamiento("Pulido corporal e hidratación", "Tratamiento corporal hiper estimulante que elimina las células muertas", 23000, 60),
    ]
    for tratamiento in tratamientos:
        if not TratamientoDAO.existe(tratamiento.nombre):
            TratamientoDAO.guardar(tratamiento)
            print(f"Tratamiento '{tratamiento.nombre}' insertado.")
        else:
            print(f"Tratamiento '{tratamiento.nombre}' ya existe, se omite.")
