__author__ = 'siddiqui'
import socket
import time

host = '127.0.0.1'
port = 2000

clients = []

newsoc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
newsoc.bind((host,port))
newsoc.setblocking(0)

end= False
print('Server Started.')

while not end :
    try:
        data, address = newsoc.recvfrom(1024)
        if str(data)=='quit':
            end = True
        if address not in clients:
            clients.append(address)

        print time.ctime(time.time()) + str(address) + " : " + str(data)
        for client in clients:
            newsoc.sendto(data, client)

    except :
        pass
newsoc.close()
