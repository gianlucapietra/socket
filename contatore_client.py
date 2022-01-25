from ast import While
import socket 
import json

HOST= "127.0.0.1"
PORT=00000
#AF_INET indica il tipo di protocollo usato
#SOCK_STREAM indica che connessione è
#with apre il socket e lo associa alla variabile s, una volta finite le azioni lo chiude
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        messaggio=input("Scrivi qualcosa :)  altrimenti digita KO per uscire")
        if messaggio=="KO"
            break
        nota={'messaggio': messaggio} 
        nota=json.dumps(nota)#trasforma un oggetto in una stringa
        s.sendall(nota.encode("UTF-8"))#invia il vettore di byte al server
        data=s.recv(1024)

