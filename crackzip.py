import pyzipper
import animation
import time


def quebrar_zip(wordlist,objzip):
    idx = 0
    with open(wordlist,'rb') as wlist:
        lines = wlist.readlines()
        
        for line in lines:
            try:

                nline = line.decode().replace("\n","")

                idx += 1
                objzip.extractall(pwd=line)

                print(f"Senha é {nline}")
                wait_animation.stop()
                return True
                
            except:
                continue

print("PASSWORD ZIP CRACKER")

senhas      = input("Insira o nome do arquivo de wordlist: ")

arquivo     = input("Digite agora o nome do arquivo zip: ")
arquivo_zip = pyzipper.AESZipFile(arquivo,'r',compression=pyzipper.ZIP_LZMA,encryption=pyzipper.WZ_AES)

wait_animation = animation.Wait()
wait_animation.start()
quebrou = quebrar_zip(senhas,arquivo_zip)
wait_animation.stop()
if not quebrou:
    print("Senha não encontrada nessa wordlist")



