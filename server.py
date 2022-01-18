import socket
import json 
HOST= "127.0.0.1"
PORT=65432

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
            primonumero=data['primonumero']
            operazione=data['operazione']
            secondonumero=data['secondonumero']
            ris=""
            if operazione=="+":
                ris=primonumero+secondonumero
            elif operazione=="-":
                ris=primonumero-secondonumero
            elif operazione=="*":
                ris=primonumero*secondonumero
            elif operazione=="/":
                if secondonumero==0:
                    ris="non puoi dividere per 0"
                else:
                    ris=primonumero/secondonumero
            elif operazione=="%":
                ris=primonumero%secondonumero
            else:
                ris="operazione non riconosciuta"
            ris=str(ris)
            cs.sendall(ris.encode("UTF-8"))

