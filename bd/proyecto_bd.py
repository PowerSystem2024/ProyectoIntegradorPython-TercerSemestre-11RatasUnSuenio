import psycopg2
#agregar perfil 
conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='proyectPython11_Ratas_1Suenio'
)