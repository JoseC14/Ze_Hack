import random
import string

class Senha:

    def __init__(self,tamanho):
        self._tamanho = tamanho
    
    #Gera uma senha com o tamanho informado
    def gerar_senha(self):
        alfanumeric = string.ascii_letters + string.digits + string.punctuation
        senha = ""
        for i in range(self._tamanho):
            senha += random.choice(alfanumeric)
        
        return senha