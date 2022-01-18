from ast import While
import socket 
import json

HOST= "127.0.0.1"
PORT=65432
#AF_INET indica il tipo di protocollo usato
#SOCK_STREAM indica che connessione è
#with apre il socket e lo associa alla variabile s, una volta finite le azioni lo chiude
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        primonumero=input("inserire il primo numero. exit() per uscire")
        if primonumero=="exit()":
            break
        primonumero=float(primonumero)
        operazione=input("inserire l'operazione (+,-,*,/,%)")
        secondonumero=float(input("inserire il secondo numero."))
        messagio={'primonumero': primonumero, 
        'operazione':operazione,
        'secondonumero':secondonumero}
        messagio=json.dumps(messagio)#trasforma un oggetto in una stringa
        s.sendall(messagio.encode("UTF-8"))#invia il vettore di byte al server
        data=s.recv(1024)
        print("Risultato:", data.decode())#decode trasforma il vettore di byte in stringa


