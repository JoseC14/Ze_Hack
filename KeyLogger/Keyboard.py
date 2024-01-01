from pynput import keyboard
from Key import Key

class Keyboard(Key):

    #Monitorar Teclado
    def mon_key(self):
        listener = keyboard.Listener(on_release=self.on_release)
        listener.start()
    
