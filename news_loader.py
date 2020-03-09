import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

with open('static/content-welcome.png', 'wb') as picture:
    while True:
        data = conn.recv(8192)
        if not data:
            break
        picture.write(data)

conn.close()
