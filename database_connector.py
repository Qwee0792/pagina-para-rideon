import sqlite3
import datetime

def sqlconductor_create():
    # Conectar a la base de datos
    con = sqlite3.connect('/db/com.conductor_sistema.db')

    # Crear el cursor
    cursor = con.cursor()

    # Crear la tabla "conductor_sistema" si no existe
    cursor.execute("""CREATE TABLE IF NOT EXISTS conductor_sistema (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username VARCHAR(255) NOT NULL,
                    auto VARCHAR(255) NOT NULL,
                    time DATETIME NOT NULL)""")

    # Cerrar el cursor y la conexión
    cursor.close()
    con.close()

def sqlconductor_pregunta(username):
    # Conectar a la base de datos
    con = sqlite3.connect('/db/com.conductor_sistema.db')

    # Crear el cursor
    cursor = con.cursor()

    # Ejecutar la consulta SELECT
    cursor.execute("SELECT * FROM conductor_sistema WHERE username=?", (username,))

    # Obtener los resultados
    resultados = cursor.fetchall()

    # Cerrar el cursor y la conexión
    cursor.close()
    con.close()

    # Verificar si hay resultados
    if resultados:
        # Obtener la fecha actual
        fecha_actual = datetime.datetime.now().date()

        # Obtener la fecha almacenada en la base de datos
        fecha_almacenada = datetime.datetime.strptime(resultados[0][3], "%Y-%m-%d").date()

        # Comparar las fechas
        if fecha_almacenada == fecha_actual:
            autorizado = False
        else:
            autorizado = True

        # Crear el diccionario de resultados
        resultado = {
            'id': resultados[0][0],
            'usernameConductor': resultados[0][1],
            'auto': resultados[0][2],
            'tiempo': resultados[0][3],
            'autorizado': autorizado
        }

        return resultado

    return None
