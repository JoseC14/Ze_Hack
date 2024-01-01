class Wordlist:
    def __init__(self,nome):
        self._nome = nome
    
    def wordlist(self):
        with open(self._nome,'r') as wlist:
            return wlist.read().split('\n')