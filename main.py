from flask import Flask, render_template, request
import os
import tcpProtocol
import requests
import json
import database_connector

app = Flask(__name__)

# Creamos el segundo proceso de SQL para conductores
database_connector.sqlconductor_create()

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
def political_privacidad():
    return render_template('politicas.html')

# Error handling
@app.errorhandler(404)
def error_404(e):
    return render_template('error_404.html'), 404

@app.errorhandler(500)
def error_500(e):
    return render_template('error_500.html'), 500

# SQL conductores NO HTML solo HTTPS support
@app.route('/sql_conductores', methods=['POST'])
def procesar_datos():
    ip_client = request.remote_addr
    data = tcpProtocol.tcp_server()
    
    if data is None:
        tcpProtocol.enviar_datos(ip_client, json.dumps({'error': 'La consulta fue NULL', 'code': 404}))
        return 'Error: La consulta fue NULL', 404
    else:
        username = data['user']
        answer = database_connector.sqlconductor_pregunta(username)

        if answer is None:
            tcpProtocol.enviar_datos(ip_client, json.dumps({'error': 'No se encontró información para el conductor', 'code': 404}))
            return 'Error: No se encontró información para el conductor', 404

        auto = answer['auto']
        id_conductor = answer['id']
        autorizado = answer['autorizado']
        usernameConductor = answer['usernameConductor']

        dataJson = {
            'auto': auto,
            'id': id_conductor,
            'autorizado': autorizado,
            'usernameConductor': usernameConductor
        }
        json_data = json.dumps(dataJson)
        tcpProtocol.enviar_datos(ip_client, json_data)
        return 'Datos enviados con éxito'

# Local development
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
