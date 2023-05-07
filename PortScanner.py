import socket
import threading
from queue import Queue

# It is forbidden to use this code against users without their permission,
# keep in mind that this is a criminal offense and you can go to jail!!!

target = "127.0.0.1"
quene = Queue()
open_ports = []

def portscan(port):
    try:
       sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       sock.connect((target, port))
       return True
    except:
       return False

def fill_queue(port_list):
    for port in port_list:
        quene.put(port)

def worker():
    while not quene.empty():
        port = quene.get()
        if portscan(port):
            print("port {} is open!" .format(port))    
            open_ports.append(port)    

port_list = range(1, 1024)
fill_queue(port_list)

thread_list = []

for t in range(1000):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open ports are: ", open_ports)

    