import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 1234))

s.listen(5)

while True:
    c, addr = s.accept()
    print("Conexion de ", addr)
    recibido = c.recv(1024).decode()
    print(recibido)
    if recibido == "hola":
        c.send('Adios'.encode())
    elif recibido == "adios":
        c.send("servidor cerrado".encode())
        break
    else:
        c.send(b'Un hola no costaba')
    c.close()
