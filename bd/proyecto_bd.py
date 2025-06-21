import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='root',
    host='127.0.0.1',
    port='5432',
    database='proyectPython11_Ratas_1Suenio'
)