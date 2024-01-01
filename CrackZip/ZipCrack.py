

class ZipCrack:

    def __init__(self, wordlist,arquivo):
        self._wordlist = wordlist
        self._arquivo  = arquivo

    def quebrar_zip(self):
        for line in self._wordlist:
                try:
                    self._arquivo.pwd = bytes(line,'utf-8')
                    self._arquivo.extractall()
                    print(f"Senha é {line}")
                    return True
                    
                except:
                    continue
