#PIETRA
import socket
import sys
import random
import os
import time
import threading
import multiprocessing
import json

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 18233
NUM_WORKERS=2

def genera_richieste(num,address,port):
    start_time_thread= time.time()
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except:
        print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()
    #1. rimpiazzare questa parte con la generazione di operazioni e numeri random, non vogliamo inviare sempre 3+5 
    primoNumero=random.randint(0,100)
    operazioni=["+","-","/","*","%"]
    op=random.randint(0,4)
    op=operazioni[op]
    secondoNumero=random.randint(0,100)

    #2. comporre il messaggio, inviarlo come json e ricevere il risultato
    data={
        "primoNumero":primoNumero,
        "operazione":op,
        "secondoNumero":secondoNumero,
    }
    data=json.dumps(data)#conversione in json
    #manda il messaggio al server
    s.sendall(data.encode("UTF-8"))
    #
    data=s.recv(1024)
    if not data:
        print(f"{threading.current_thread().name}: Server non risponde. Exit")
    else:
        print(f"{threading.current_thread().name}: Risultato: {data.decode()}") # trasforma il vettore di byte in stringa
    s.close()
    end_time_thread=time.time()
    print(f"{threading.current_thread().name} tempo di esecuzione time=", end_time_thread-start_time_thread)

if __name__ == '__main__':
    start_time=time.time()
    i=0
    for i in range(NUM_WORKERS):
        genera_richieste(i,SERVER_ADDRESS, SERVER_PORT)
    # 3 ciclo per chiamare NUM_WORKERS volte la funzione genera richieste alla quale passo i parametri (num,SERVER_ADDRESS, SERVER_PORT)
    end_time=time.time()
    print("Total SERIAL time=", end_time - start_time)
     
    start_time=time.time()
    threads=[]
    for i in range(NUM_WORKERS):
        # 4 ciclo per chiamare NUM_WORKERS volte la funzione genera richieste tramite l'avvio di un thread al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
        threads.append(threading.Thread(target=genera_richieste, args=(i,SERVER_ADDRESS,SERVER_PORT)))
        #threads.append(t)
    for x in threads:
        x.start()
        x.join()
    # ad ogni iterazione appendo il thread creato alla lista threads
    # 5 avvio tutti i thread
    # 6 aspetto la fine di tutti i thread 
    end_time=time.time()
    print("Total THREADS time= ", end_time - start_time)

    start_time=time.time()
    process=[]
    # 7 ciclo per chiamare NUM_WORKERS volte la funzione genera richieste tramite l'avvio di un processo al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # ad ogni iterazione appendo il thread creato alla lista threads
    # 8 avvio tutti i processi
    # 9 aspetto la fine di tutti i processi 
    end_time=time.time()
    print("Total PROCESS time= ", end_time - start_time)