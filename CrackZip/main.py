from Arquivo import Arquivo
from Wordlist import Wordlist
from ZipCrack import ZipCrack
import animation



print("PASSWORD ZIP CRACKER")

senhas      = input("Insira o nome do arquivo de wordlist: ")
arquivo     = input("Digite agora o nome do arquivo zip: ")

arquivo_zip    = Arquivo(arquivo).arq_zip()
wordlist       = Wordlist(senhas).wordlist()
wait_animation = animation.Wait()
wait_animation.start()
quebrou = ZipCrack(wordlist,arquivo_zip).quebrar_zip()
wait_animation.stop()
if quebrou != True:
    print("Senha não encontrada nessa wordlist")



