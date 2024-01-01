#Classe wordlist
class Wordlist:
    def __init__(self,nome):
        self._nome = nome
    
    #Abre a wordlist
    def wordlist(self):
        with open(self._nome,'r') as wlist:
            return wlist.read().split('\n')