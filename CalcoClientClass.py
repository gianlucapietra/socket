from distutils.log import error
import socket
from threading import Thread
SERVER_ADDRESS='127.0.0.1'
SERVER_PORT=22225
class Client():
    """
    questa classe rappresenta una persona che opera come client
    """
    def connessione_server(self,address,port):
        """
        metodo per stabilire una connessione con il server 
        """
        sock_service=socket.socket()
        sock_service.connect((address,port))
        print("Connesso a "+str((address,port)))
        return sock_service
    
    def invia_comandi(self,sock_service):
        """
        metodo per inviare le richieste di servizio e ricevere le risposte
        """
        while True:
            try:
                n1=input("inserisci il primo numero: ")
                n2=input("inserisci il secondo numero: ")
                op=input("inserire l'operazione da effettuare(più/meno/per/diviso): ")
                dati=f"{op};{n1};{n2}"
            except EOFError:
                print("\nOkay. Exit")
                break
            if not dati:
                print("Non puoi inviare una stringa vuota")
                continue
            if dati=="0":
                print("Chiudo la connessione con il server")
                sock_service.close()
                break

            dati=dati.encode()
            sock_service.sendall(dati)
            dati=sock_service.recv(2048)
            if not dati:
                print("server non risponde. Exit")
                break
            dati=dati.decode()
            print("ricevuto dal server")
            print(dati +'\n')
            
c1=Client()
sock_serv=c1.connessione_server(SERVER_ADDRESS,SERVER_PORT)
c1.invia_comandi(sock_serv)

