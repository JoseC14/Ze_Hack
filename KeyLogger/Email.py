import smtplib, ssl

class Email:

    def __init__(self,sender,pwd,dest,msg):
        self._sender = sender
        self._pwd    = pwd
        self._dest   = dest
        self._msg    = msg
        
    #Envia o email com o log
    def enviar_email(self):
        enviou         = False
        smtp_server    = "smtp.gmail.com"
        port           = 587 
        time           = 12
        context        = ssl.create_default_context()
        if  enviou == False:         
            try:
                print(f"Enviando email...{self._msg}")
                server = smtplib.SMTP(smtp_server,port)
                server.ehlo() 
                server.starttls(context=context)
                server.ehlo()
                server.login(self._sender, self._pwd)
                server.sendmail(self._sender,self._dest,self._msg)
                enviou = True
            except Exception as e:
                print(e)
            finally:
                server.quit() 

