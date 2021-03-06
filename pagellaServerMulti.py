#nome del file : pagellaServerMulti.py

from pprint import pprint
import socket
from threading import Thread
import json


SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22225

#Versione 1 
def ricevi_comandi1(sock_service,addr_client):
    while True:
        data=sock_service.recv(1024)
        if not data: 
                break
        data=data.decode()
        data=json.loads(data)        
        #1. recuperare dal json studente, materia, voto e assenze
        alunno=data['alunno']
        materia=data['materia']
        voto=data['voto']
        assenze=data['assenze']
        #2. restituire un messaggio in json contenente studente, materia e una valutazione testuale :
        # voto < 4 Gravemente insufficiente
        if voto<4:
            valutazione="valutazione: gravemente insufficiente"
        # voto [4..5] Insufficiente
        elif voto==4 or voto==5: 
            valutazione="valutazione: insufficiente"
        # voto = 6 Sufficiente
        elif voto==6:
            valutazione="valutazione: sufficiente"
        # voto = 7 Discreto 
        elif voto==7:
            valutazione="valutazione: discreta"
        # voto [8..9] Buono
        elif voto==8 or voto==9:
            valutazione="valutazione: buono"
        # voto = 10 Ottimo
        elif voto==10:
            valutazione="valutazione: ottimo"
        messaggio={'alunno':alunno,
        'materia':materia,
        'valutazione':valutazione}
        print(messaggio)
        messaggio:json.dumps(messaggio)
        sock_service.sendall(messaggio.encode("UTF-8"))
    sock_service.close()

#Versione 2 
def ricevi_comandi2(sock_service,addr_client):
    while True:
        data=sock_service.recv(1024)
        if not data: 
                break
        data=data.decode()
        data=json.loads(data)
        #1.recuperare dal json studente e pagella
        alunno=data['alunno']
        pagella=data['pagella']
        assenze=0
        media=0
        for i,p in range:
            media+=int(p[1])
            assenze+=int(p[2])
        media=media/i
        messaggio={'alunno':alunno,
        'media':media,
        'assenze':assenze}
        print(messaggio)
        messaggio=json.dumps(data)
        sock_service.sendall(messaggio.encode("UTF-8"))

    sock_service.close()

  #2.restituire studente, media dei voti e somma delle assenze :

#Versione 3
def ricevi_comandi3(sock_service,addr_client):
    while True: 
        data=sock_service.recv(1024)
        if not data:
                break
        data=data.decode()
        data=json.loads(data)
        pp=pprint.PrettyPrinter(indent=4)
        tabellone=[]
        for a in data:
            pagella=data[a]
            assenze=0
            media=0
            for i,p in enumerate(pagella):
                media+=int(p[1])
                assenze+=int(p[2])
                media=media/i
                messaggio={'alunno':a,
                'media':media,
                'assenze':assenze}
                tabellone.append(messaggio)
        pp.pprint(tabellone)
        messaggio=tabellone
        messaggio=json.dumps(messaggio)
        sock_service.sendall(messaggio.encode("UTF-8"))
    sock_service.close()
  #....
  #1.recuperare dal json il tabellone
  #2. restituire per ogni studente la media dei voti e somma delle assenze :


def ricevi_connessioni(sock_listen):
    while True:
        sock_service, addr_client = sock_listen.accept()
        print("\nConnessione ricevuta da " + str(addr_client))
        print("\nCreo un thread per servire le richieste ")
        try:
            Thread(target=ricevi_comandi1,args=(sock_service,addr_client)).start()
        except:
            print("il thread non si avvia")
            sock_listen.close()
        
def avvia_server(SERVER_ADDRESS,SERVER_PORT):
    sock_listen=socket.socket()
    sock_listen.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sock_listen.bind((SERVER_ADDRESS,SERVER_PORT))
    sock_listen.listen(5)
    print("Server in ascolto su %s." %str((SERVER_ADDRESS,SERVER_PORT)))
    ricevi_connessioni(sock_listen)

if __name__=='__main__':
    avvia_server(SERVER_ADDRESS,SERVER_PORT)