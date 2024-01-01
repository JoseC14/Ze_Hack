import pyzipper
class Arquivo:
    def __init__(self,nome):
        self._nome = nome

    #Gera o objeto zip
    def arq_zip(self):
       return pyzipper.AESZipFile(self._nome,'r')