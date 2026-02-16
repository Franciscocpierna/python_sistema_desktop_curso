import smtplib
import email.message

class enviarEmail:
    ''' Classe que permite enviar email pelo Gmail'''
    def __init__(self, Subject, From, To, password, corpo_email):
        self.Subject = Subject
        self.From = From
        self.To = To
        self.password = password
        self.corpo_email = corpo_email
        print('Objeto Criado')
    def enviandoEmail(self):
        corpo_email = self.corpo_email
        msg = email.message.Message()
        msg['Subject'] = self.Subject #assunto
        msg['From'] = self.From #Remetente
        msg['To'] = self.To #Destinatário
        password = self.password
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        # Login credenciais para enviar o email
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        return 'Email enviado'
