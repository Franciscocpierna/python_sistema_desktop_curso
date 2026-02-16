# pip install secure-smtplib
# pip install email - normalmente vem já por padrão no python

# Imports para enviar emails
import email, smtplib, ssl
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase



### Configurações Iniciais do Email ###
port = 587  # For SSL
subject = "Email automático com anexo - teste"
body = "Segue boleto em anexo.  Esta é uma mensagem automatica."
smtp_server = 'smtp.gmail.com'
sender_email = "pyqtenviaremail@gmail.com"  # Enter your address
receiver_email = "pyqtenviaremail@gmail.com" # Enter your address
password = 'qpczkevwgmsvfdgl'



def enviar_email():
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    # Add body to email
    message.attach(MIMEText(body, "plain"))
    filename = 'ArquivoPDF.pdf'
    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)
        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        # Add attachment to message and convert message to string
        message.attach(part)
        with smtplib.SMTP(smtp_server, port) as server:
            #server.ehlo()  # Can be omitted
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("email enviado")

enviar_email()