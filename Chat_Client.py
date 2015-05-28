__author__ = 'siddiqui'
import socket
import threading
import time

lock = threading.Lock()

end = False

def receiving(name, sock):
    while not end:
        try :
            lock.acquire()
            while True:
                data, address = sock.recvfrom(1024)
                print str(data)

        except:
            pass
        finally:
            lock.release()

host = '127.0.0.1'
port = 0

server = ('127.0.0.1', 2000)

newsoc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
newsoc.bind((host,port))
newsoc.setblocking(0)

receivingthread= threading.Thread(target=receiving, args=("RecvThread", newsoc))
receivingthread.start()

username = raw_input("Name :")
message = raw_input(username + " : ")
while message != 'quit':
    if message != '':
        newsoc.sendto(username + ":" + message, server)
    lock.acquire()
    message = raw_input(username + " : ")
    lock.release()
    time.sleep(.2)

end = True
receivingthread.join()
newsoc.close()
