import socket
import threading
import os
from subprocess32 import Popen, PIPE


def RetrFile(name, sock):
    '''
    PERMISSION DENIED
    cmd = sock.recv(1024)
    p = Popen(cmd, stdout=PIPE)
    result = p.communicate()
    s.send(result[0])
    '''
    filename = sock.recv(2048)
    if os.path.isfile(filename):
        sock.send("EXISTS " + str(os.path.getsize(filename)))
        userResponse = sock.recv(2048)
        if userResponse[:2] == 'OK':
            with open(filename, 'rb') as f:
                bytesToSend = f.read(2048)
                sock.send(bytesToSend)
                while bytesToSend != "":
                    bytesToSend = f.read(2048)
                    sock.send(bytesToSend)
    else:
        sock.send("ERR ")

    sock.close()


def Main():
    host = '127.0.0.1'
    port = 5383

    s = socket.socket()
    s.bind((host, port))

    s.listen(5)

    print "Server Started."
    while True:
        c, addr = s.accept()
        print "client connedted ip:<" + str(addr) + ">"
        t = threading.Thread(target=RetrFile, args=("RetrThread", c))
        t.start()

    s.close()


if __name__ == '__main__':
    Main()
