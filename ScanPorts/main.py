from Scan import Scan


print("--------------------")
print("ESCANEADOR DE PORTAS")
print("--------------------")
while True:
    ip = input("Digite o ip a ser escaneado: ")
    mode = int(input("Você quer escanear apenas uma porta ou um range de portas?(1,2)"))

    if mode == 1:
        porta = int(input("Digite a porta: "))
        Scan(ip=ip,port=porta).escanear_porta()
    elif mode == 2:
        porta_begin = int(input("Digite o inicio do range: "))
        porta_end   = int(input("Digtie o fim do range: "))
        Scan(ip=ip,port_begin = porta_begin, port_end = porta_end).escanear_portas()




