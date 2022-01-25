import socket
import json 
HOST= "127.0.0.1"
PORT=00000
i=0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    print("[*] in ascolto su %s: %d"%(HOST,PORT))
    clientsocket, address=s.accept()#accetta la connessione al socket
    with clientsocket as cs:
        print("connessione da", address)
        while True:
            data=cs.recv(1024)
            if not data:#se data è un vettore vuoto usciamo dal ciclo
                break
            data=data.decode()
            data=json.loads(data)
            messaggio=data['messaggio']
            i+=1
            if messaggio="KO"
            break
            cs.sendall(i.encode("UTF-8"))