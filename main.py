from flask import Flask, Response, jsonify,render_template, request, session
import os

# install dependencies for pip 
os.system('pip install sqlite3')
os.system('python -m pip install sqlite3')
os.system('py -m pip install sqlite3')
os.system('python -m pip install --upgrade pip')
os.system('py -m pip install --upgrade pip')

# creamos el segundo proseso de sql para conductores
import database_connector

app= Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('Home.html')

@app.route('/Descargar')
def descargar():
    return render_template('Descargar.html')

@app.route('/Trabajo')
def trabajo():
    return render_template('trabajo.html')

@app.route('/contactanos')
def contactanos():
    return render_template('contacto.html')

@app.route('/Politica')
def political_pribacidad():
    return render_template('politicas.html')


# error handling
@app.errorhandler(404)
def error_404():
    return render_template('error_404.html')
@app.errorhandler(500)
def error_500():
    return render_template('error_500.html')

# SQL conductores NO HTML solo HTTPS support

import xml.etree.ElementTree as ET

@app.route('/sql_conductores', methods=['POST'])
def procesar_datos():
    # Crear base de datos
    database_connector.sqlconductor_create()
    # preguntar a base de datos
    dataConductorRequest= request.get_json()
    username = dataConductorRequest['username']
    # prosesar solisitud en base de datos 
    anwer= database_connector.sqlconductor_pregunta(username)
    respuesta = anwer
    idConductor= respuesta.get('id')
    numAuto= respuesta.get('auto')
    timeConductor= respuesta.get('tiempo')
    autorisadoConductor = respuesta.get('autorisado')
    print(timeConductor)
    print(numAuto)
    print(autorisadoConductor)
    print(idConductor)
    # crear el json para respomder
    import json
    data = {}
    data['Datos'] = []
    data['Datos'].append({
        'id':idConductor,
        'auto': numAuto,
        'time': timeConductor,
        'autorisado': autorisadoConductor})
    
    return data

# local development
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)