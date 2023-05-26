import socket
import json

def tcp_server():
    server_ip = '0.0.0.0'  # Escucha en todas las interfaces de red
    server_port = 1234

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((server_ip, server_port))
    sock.listen(1)

    print(f"Servidor TCP escuchando en {server_ip}:{server_port}")

    while True:
        conn, addr = sock.accept()
        print('Cliente conectado:', addr)

        data = b''
        while True:
            chunk = conn.recv(1024)
            if not chunk:
                break
            data += chunk

        conn.close()

        # Decodificar los datos JSON
        json_data = data.decode()
        datos = json.loads(json_data)
        return datos

def enviar_datos(ip_client, json_data):
    import socket
    import json

    datos = json_data

    # Configurar los detalles de la conexión TCP
    server_ip = ip_client
    server_port = 1234

    # Convertir los datos a JSON
    json_data = json.dumps(datos)

    # Crear un socket TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conectar al servidor
        sock.connect((server_ip, server_port))

        # Enviar los datos JSON
        sock.sendall(json_data.encode())

        # Esperar la respuesta del servidor
        response = sock.recv(1024)
        print('Respuesta del servidor:', response.decode())
    finally:
        # Cerrar el socket
        sock.close()

    return True
