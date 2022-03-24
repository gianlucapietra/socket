import socket
from threading import Thread
SERVER_ADDRESS='127.0.0.1'
SERVER_PORT=22225
class Server():
    """
    Questa classe rappresenta un server
    """
    def __init__(self,address,port):
        self.address=address
        self.port=port
    
    def avvia_server(self):
        """
        Metodo per aprirsi e mettersi in ascolto aspettando richieste da service
        """
        sock_listen=socket.socket()
        sock_listen.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        sock_listen.listen(5)
        print("server in ascolto su %s. " % str((self.address, self.port)))
        return sock_listen

    def accetta_connessione(self,sock_listen):
        """
        Metodo per accettare richieste di un servizio ed assegnare un Thread ad ognuna di esse
        """
        while True:
            sock_service,addr_client= sock_listen.accept()
            print("\nConnessione ricevuta da " + str(addr_client))
            print("\nCreo un thread per servire le richieste ")
            try:
                Thread(target=self.ricevi_comandi, args=(sock_service,addr_client)).start()
            except:
                print("il thread non si avvia")
                sock_listen.close()

    def ricevi_comandi(self,sock_service,addr_client):
        """
        metodo per ricevere i comandi e servire le richieste ricevute
        """
        print("avviato")
        while True:
            dati=sock_service.recv(2048)
            if not dati:
                print("Fine dati dal client. reset")
                break
            dati=dati.decode()
            print("Ricevuto: '%s'" % dati )
            if dati=='0':
                print("Chiudo la connessione con" + str(addr_client))
                break
            risultato=0
            op,n1,n2=dati.split(";")
            if op=="più":
                risultato=int(n1)+int(n2)

            if op=="meno":
                risultato=int(n1)-int(n2)

            if op=="per":
                risultato=int(n1)*int(n2)

            if op=="diviso":
                risultato=int(n1)/int(n2)
            
            dati=f"risposta a : {str(addr_client)}, Il risultato dell'operazione({n1} {op} {n2}) è : {risultato}"
            dati=dati.encode()
            sock_service.send(dati)
        sock_service.close()
s1=Server(SERVER_ADDRESS,SERVER_PORT)
sock_lis=s1.avvia_server()
s1.accetta_connessione(sock_lis)

