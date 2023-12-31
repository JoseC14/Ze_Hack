import socket


def escanear(ip,mode,port_begin=None,port_end=None,port=None):
    if mode == 1:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if s.connect_ex((ip, port)) == 0:
            print(f"Porta {port} Aberta!")
            s.close()
        else:
            print(f"Porta {port} Fechada")
    elif mode == 2:
        for ports in range(port_begin,port_end+1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            if s.connect_ex((ip, ports)) == 0:
                print(f"Porta {ports} Aberta!")
                s.close()

print("--------------------")
print("ESCANEADOR DE PORTAS")
print("--------------------")
while True:
    ip = input("Digite o ip a ser escaneado: ")
    mode = int(input("Você quer escanear apenas uma porta ou um range de portas?(1,2)"))

    if mode == 1:
        porta = int(input("Digite a porta"))
        escanear(ip=ip,mode=mode,port = porta)




