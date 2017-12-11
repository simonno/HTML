import socket
from os.path import splitext

from HTMLParser import HttpMassageParser


def get_content_type(file_path):
    file_name, file_extension = splitext(file_path)
    return {
        '.jpg': 'image/jpg',
        '.png': 'image/png',
        '.gif': 'image/gif',
        '.woff': 'application/x-font-woff',
        '.ttf': 'application/x-font-ttf',
        '.svg': 'image/svg+xml',
        '.eot': 'application/vnd.ms-fontobject',
        '.otf': 'application/x-font-otf',
        '.css': 'text/css',
        '.html': 'text/html',
        '.js': 'application/javascript',

    }.get(file_extension, 'text/html')


def parser(massageHTML):
    lines = massageHTML.splitlines()
    data_path = lines[0].split("GET /")[1].split(" HTTP/1.1")[0]
    try:
        data = open(data_path, 'rb').read()
    except IOError:
        massage_parser = HttpMassageParser(1.1, 404, 'text/html', 'close', '')
        return massage_parser.get_massage()

    massage_parser = HttpMassageParser(1.1, 200, get_content_type(data_path), 'close', data)
    return massage_parser.get_massage()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '127.0.0.1'
server_port = 80
server.bind((server_ip, server_port))
server.listen(5)

while True:
    client_socket, client_address = server.accept()
    print 'Connection from: ', client_address
    massage = client_socket.recv(1024)
    while not massage == '':
        print 'Received: ', massage
        to_send = parser(massage)
        client_socket.send(to_send)
        massage = client_socket.recv(1024)

    print 'Client disconnected'
    client_socket.close()
