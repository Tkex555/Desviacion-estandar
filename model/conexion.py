import mysql.connector
from mysql.connector import Error

def conectar_db():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',  # Cambia por tu usuario de MySQL
            password='',  # Cambia por tu contraseña de MySQL
            database='machine_learning_db'
        )
        return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def guardar_medicion(valores, desviacion, metodo):
    conexion = conectar_db()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = """
                INSERT INTO mediciones (valores, desviacion_estandar, metodo)
                VALUES (%s, %s, %s)
            """
            cursor.execute(consulta, (" ".join(map(str, valores)), desviacion, metodo))
            conexion.commit()
            print("Medición guardada en la base de datos.")
            return True
        except Exception as e:
            print(f"Error al guardar la medición: {e}")
            return False
        finally:
            cursor.close()
            conexion.close()
    return False
