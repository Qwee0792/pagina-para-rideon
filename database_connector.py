# creamos la base de datos si no existe
import sqlite3

def sqlconductor_create():
    # Conectar a la base de datos
    com = sqlite3.connect('/db/com.conductor_sistema.db')

    # Crear el cursor
    cursor = com.cursor()

    # Crear la tabla "conductor_sistema" si no existe
    cursor.execute("""CREATE TABLE IF NOT EXISTS conductor_sistema (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username VARCHAR(255) NOT NULL,
                    auto VARCHAR(255) NOT NULL,
                    time DATETIME NOT NULL)""")

    # Cerrar el cursor
    cursor.close()

import sqlite3
import datetime

def sqlconductor_pregunta(username):
    # Conectar a la base de datos
    com = sqlite3.connect('/db/com.conductor_sistema.db')

    # Crear el cursor
    cursor = com.cursor()

    # Ejecutar la consulta SELECT
    cursor.execute("SELECT * FROM conductor_sistema WHERE username=?", (username,))

    # Obtener los resultados
    resultados = cursor.fetchall()

    # Cerrar el cursor
    cursor.close()

    # Obtener la fecha actual
    fecha_actual = datetime.datetime.now().date()

    # Obtener la fecha almacenada en la base de datos
    fecha_almacenada = datetime.datetime.strptime(resultados[0][3], "%Y-%m-%d").date()
    id = resultados[0]
    usernameConductor = resultados[1]
    auto= resultados[2]
    tiempo= resultados[3]
    # Comparar las fechas
    if fecha_almacenada == fecha_actual:
        autorizado = False
    else:

        autorizado = True
    resultodos = {'auto':auto,
                    'tiempo' : tiempo,
                    'id' : id,
                    'autorizado' : autorizado,
                    'usernameConductor' : usernameConductor}

    return resultados


    


