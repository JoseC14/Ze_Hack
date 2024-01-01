import socket

class Scan:

    def __init__(self,ip,port_begin=None,port_end=None,port=None):
        self._ip         = ip
        self._port_begin = port_begin
        self._port_end   = port_end
        self._port       = port

    #Escaneia apenas uma porta
    def escanear_porta(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
        if s.connect_ex((self._ip, self._port)) == 0:
            print(f"Porta {self._port} Aberta!")
            s.close()
        else:
            print(f"Porta {self._port} Fechada")
    
    #Escaneia mais de uma porta
    def escanear_portas(self):
        for ports in range(self._port_begin,self._port_end+1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10)
            if s.connect_ex((self._ip, ports)) == 0:
                print(f"Porta {ports} Aberta!")              
            else:
                print(f"Porta {ports} Fechada!")

            s.close()