import sqlite3
from datetime import datetime, timedelta
def sqlconductor_create():
    # Conectar a la base de datos
    com = sqlite3.connect('com.conductor_sistema.db')

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

def agregar_conductor():
    # Conectar a la base de datos
    con = sqlite3.connect('com.conductor_sistema.db')

    # Crear el cursor
    cursor = con.cursor()

    # Solicitar los datos al usuario
    username = input("Ingrese el nombre de usuario: ")
    auto = input("Ingrese el nombre del auto: ")
    dias = int(input("Ingrese la cantidad de días a agregar: "))

    # Calcular la nueva fecha sumando los días ingresados
    fecha_actual = datetime.now()
    nueva_fecha = fecha_actual + timedelta(days=dias)
    tiempo = nueva_fecha.strftime("%Y-%m-%d %H:%M:%S")

    # Insertar los datos en la base de datos
    cursor.execute("INSERT INTO conductor_sistema (username, auto, time) VALUES (?, ?, ?)", (username, auto, tiempo))
    con.commit()

    # Imprimir la fecha y hora ingresada
    print("Fecha y hora ingresada:", tiempo)

    print("Datos agregados exitosamente a la base de datos.")

    # Cerrar la conexión y el cursor
    cursor.close()
    con.close()

# while True:

    # user = input("User desea cuntinuar pulse enter o exit para salir")
    # if user == "exit":
    #     break
    # else:
        # agregar_conductor()
sqlconductor_create()
agregar_conductor()           