#nome del file : pagellaClientMulti.py
import socket
import sys
import random
import os
import time
import threading
import multiprocessing
import json
import pprint

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22225
NUM_WORKERS=4

#Versione 1 
def genera_richieste1(num,address,port):
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except:
        print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()

    #1. Generazione casuale:
    #   di uno studente (valori ammessi: 5 cognomi a caso tra cui il tuo cognome)
    alunni=["Pietra","Moraru","Falcone","Colombo","Peralta"]
    alunno=alunni[random.randint(0,4)]
    #   di una materia (valori ammessi: Matematica, Italiano, inglese, Storia e Geografia)
    materie=["Matematica", "Italiano", "inglese", "Storia", "Geografia"]
    materia=materie[random.randint(0,4)]
    #   di un voto (valori ammessi 1 ..10)
    voto=random.randint(1,10)
    #   delle assenze (valori ammessi 1..5) 
    assenze=random.randint(1,5)
    #2. comporre il messaggio, inviarlo come json
    data={
        "alunno":alunni,
        "materia":materie,
        "voto":voto,
        "assenze":assenze,
    }
    data=json.dumps(data)#conversione in json
    #manda il messaggio al server
    s.sendall(data.encode("UTF-8"))
    #   esempio: {'studente': 'Studente4', 'materia': 'Italiano', 'voto': 2, 'assenze': 3}
    #3. ricevere il risultato come json: {'studente':'Studente4','materia':'italiano','valutazione':'Gravemente insufficiente'}
    data=s.recv(1024)
    
    
    if not data:
        print(f"{threading.current_thread().name}: Server non risponde. Exit")
    else:
        #4 stampare la valutazione ricevuta esempio: La valutazione di Studente4 in italiano è Gravemente insufficiente
        print(f"{threading.current_thread().name}: Risultato: {data.decode()}") # trasforma il vettore di byte in stringa
        s.close()

#Versione 2 
def genera_richieste2(num,address,port):
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except:
        print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()
    
  
#   1. Generazione casuale di uno studente(valori ammessi: 5 cognomi a caso scelti da una lista)
    alunni=["Pietra","Moraru","Falcone","Colombo","Peralta"]
    alunno=alunni[random.randint(0,4)]
#   Per ognuna delle materie ammesse: Matematica, Italiano, inglese, Storia e Geografia)
    materie=["Matematica", "Italiano", "inglese", "Storia", "Geografia"]
    materia=materie[random.randint(0,4)]
#   generazione di un voto (valori ammessi 1 ..10)
    voto=random.randint(1,10)
#   e delle assenze (valori ammessi 1..5) 
    assenze=random.randint(1,5)
    for i in range(len(alunni)):
        pagella={alunni[i]:[("Matematica",8,1), ("Italiano",6,1), ("Inglese",9.5,3), ("Storia",8,2), ("Geografia",8,1)]}
#   esempio: pagella={"Cognome1":[("Matematica",8,1), ("Italiano",6,1), ("Inglese",9.5,3), ("Storia",8,2), ("Geografia",8,1)]}
#2. comporre il messaggio, inviarlo come json
    data={
    "alunno":alunni,
    "materia":materie,
    "voto":voto,
    "assenze":assenze,
    "pagella":pagella,
}
    data=json.dumps(data)#conversione in json
#manda il messaggio al server
    s.sendall(data.encode("UTF-8"))
#   esempio: {'studente': 'Studente4', 'materia': 'Italiano', 'voto': 2, 'assenze': 3}
#3. ricevere il risultato come json: {'studente':'Studente4','materia':'italiano','valutazione':'Gravemente insufficiente'}
    data=s.recv(1024)
#3  ricevere il risultato come json {'studente': 'Cognome1', 'media': 8.0, 'assenze': 8}
    if not data:
        print(f"{threading.current_thread().name}: Server non risponde. Exit")
    else:
    #4 stampare la valutazione ricevuta esempio: La valutazione di Studente4 in italiano è Gravemente insufficiente
        print(f"{threading.current_thread().name}: Risultato: {data.decode()}") # trasforma il vettore di byte in stringa
    s.close()
#Versione 3
def genera_richieste3(num,address,port):
    pass
  #....
  #   1. Per ognuno degli studenti ammessi: 5 cognomi a caso scelti da una lista
  #   Per ognuna delle materie ammesse: Matematica, Italiano, inglese, Storia e Geografia)
  #   generazione di un voto (valori ammessi 1 ..10)
  #   e delle assenze (valori ammessi 1..5) 
  #   esempio: tabellone={"Cognome1":[("Matematica",8,1), ("Italiano",6,1), ("Inglese",9,3), ("Storia",8,2), ("Geografia",8,1)],
  #                       "Cognome2":[("Matematica",7,2), ("Italiano",5,3), ("Inglese",4,12), ("Storia",5,2), ("Geografia",4,1)],
  #                        .....}
  #2. comporre il messaggio, inviarlo come json
  #3  ricevere il risultato come json e stampare l'output come indicato in CONSOLE CLIENT V.3

if __name__ == '__main__':
    start_time=time.time()
    for i in range(NUM_WORKERS):
        genera_richieste1(i,SERVER_ADDRESS, SERVER_PORT)
    # 3 ciclo per chiamare NUM_WORKERS volte la funzione genera richieste alla quale passo i parametri (num,SERVER_ADDRESS, SERVER_PORT)
    end_time=time.time()
    print("Total SERIAL time=", end_time - start_time)
     
    start_time=time.time()
    threads=[]
    # PUNTO A) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3)
    # alla quale passo i parametri (num,SERVER_ADDRESS, SERVER_PORT)
    for i in range(NUM_WORKERS):
         for i in range(NUM_WORKERS):
            threads.append(threading.Thread(target=genera_richieste2, args=(i,SERVER_ADDRESS,SERVER_PORT)))
    for x in threads:
        x.start()
        x.join()
    end_time=time.time()
    print("Total SERIAL time=", end_time - start_time)
     
    start_time=time.time()
    threads=[]
    # PUNTO B) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3)  
    # tramite l'avvio di un thread al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # avviare tutti i thread e attenderne la fine
    end_time=time.time()
    print("Total THREADS time= ", end_time - start_time)

    start_time=time.time()
    process=[]
    # PUNTO C) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3) 
    # tramite l'avvio di un processo al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # avviare tutti i processi e attenderne la fine
    end_time=time.time()
    print("Total PROCESS time= ", end_time - start_time)