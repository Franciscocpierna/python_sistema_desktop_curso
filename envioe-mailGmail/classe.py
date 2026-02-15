# import email, smtplib
# from email import encoders
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase 


# # configuração inicial do Email
# port = 587
# subject = 'Email automático com Anexo - teste'
# body = 'segue boleto em anexo - Esta é uma mensagem automática'
# smtp_server = 'smtp.gmail.com'
# sender_email = 'fcpierna@gmail.com'
# receiver_email = 'fcpierna@gmail.com'
# password = '34145292'


# def enviar_email():
#     #criando a mulipart da mensagem e colocando cabeçalho
#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["to"] = receiver_email
#     message["subject"] = subject
#     # adicionando o corpo da mensagem para o email

#     message.attach(MIMEText(body,"plain"))
#     filename = 'teste.PDF'
#     # Abrindo o arquivo PDF em modo binário
#     with open(filename, "rb") as attachment:
#         # adicionar o arquivo na aplicação/octet-stren
#         part = MIMEBase("application", "octet-stream") 
#         part.set_payload(attachment.read())
#         # Arquivo com encode no formato de email
#         encoders.encode_base64(part)
#         # adicionando o cabeçalho como chave/valor da partição do email
#         part.add_header("content-Disposition", f"attachment; filename = {filename}")
#         # adicionando o anexo na mensagem e convertendo a mensagem como string
#         message.attach(part) 
#         # Enviando e-mail
#         with smtplib.SMTP(smtp_server, port) as server:
#             server.starttls()
#             server.login(sender_email, password) 
#             server.sendmail(sender_email, receiver_email, message.as_string()) 
#         print('Email enviado')    

# enviar_email()        


import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase 

# configuração inicial do Email
port = 587
subject = 'Email automático com Anexo - teste'
body = 'segue boleto em anexo - Esta é uma mensagem automática'
smtp_server = 'smtp.gmail.com'
sender_email = 'fcpierna@gmail.com'
receiver_email = 'fcpierna@gmail.com'

# ATENÇÃO: Use aqui a senha de 16 dígitos gerada no Google (Senhas de App)
password = 'uvuo oekt erwb nnhq' 

def enviar_email():
    try:
        # criando a multipart da mensagem e colocando cabeçalho
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email # Corrigido para "To" com T maiúsculo
        message["Subject"] = subject
        
        # adicionando o corpo da mensagem
        message.attach(MIMEText(body, "plain"))
        
        filename = 'teste.PDF'
        
        # Abrindo o arquivo PDF em modo binário
        with open(filename, "rb") as attachment:
            # octet-stream é o padrão para arquivos binários
            part = MIMEBase("application", "octet-stream") 
            part.set_payload(attachment.read())
            
            # Arquivo com encode no formato de email
            encoders.encode_base64(part)
            
            # adicionando o cabeçalho do anexo
            part.add_header("Content-Disposition", f"attachment; filename={filename}")
            
            # adicionando o anexo na mensagem
            message.attach(part) 
            
            # Enviando e-mail
            with smtplib.SMTP(smtp_server, port) as server:
                server.starttls() # Inicia segurança
                server.login(sender_email, password) 
                server.sendmail(sender_email, receiver_email, message.as_string()) 
            
        print('Email enviado com sucesso!')
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{filename}' não foi encontrado.")
    except smtplib.SMTPAuthenticationError:
        print("Erro de Autenticação: Verifique se a Senha de App está correta.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    enviar_email()


'''
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase 

# --- CONFIGURAÇÕES PARA HOTMAIL / OUTLOOK ---
# O servidor SMTP do Hotmail mudou para o endereço do Outlook
smtp_server = 'smtp-mail.outlook.com'
port = 587

# Dados da conta
sender_email = 'seu-email@hotmail.com'
receiver_email = 'destino@gmail.com'
subject = 'Email automático via Hotmail - Teste'
body = 'Este e-mail foi enviado utilizando o servidor do Hotmail/Outlook.'

# IMPORTANTE: Se tiver verificação de dois passos, gere uma "Senha de App" 
# nas configurações de segurança da sua conta Microsoft.
password = 'sua-senha-ou-senha-de-app'

def enviar_email_hotmail():
    try:
        # Criando a estrutura da mensagem
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        
        # Adicionando o corpo do e-mail
        message.attach(MIMEText(body, "plain"))
        
        filename = 'teste.PDF'
        
        # Anexando o arquivo
        try:
            with open(filename, "rb") as attachment:
                part = MIMEBase("application", "octet-stream") 
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename={filename}")
                message.attach(part)
        except FileNotFoundError:
            print(f"Aviso: O arquivo '{filename}' não foi encontrado. Enviando sem anexo.")

        # Processo de conexão e envio específico do Hotmail
        print("Conectando ao servidor do Hotmail...")
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo() # Identificação para o servidor
        server.starttls() # Inicia a criptografia
        server.ehlo() # Re-identificação após iniciar TLS
        
        server.login(sender_email, password)
        
        print("Enviando e-mail...")
        server.sendmail(sender_email, receiver_email, message.as_string())
        
        server.quit() # Encerra a conexão
        print('E-mail enviado com sucesso pelo Hotmail!')
    
    except smtplib.SMTPAuthenticationError:
        print("Erro: Falha na autenticação. Verifique seu e-mail e senha.")
        print("Dica: Verifique se precisa de uma 'Senha de App' na sua conta Microsoft.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    enviar_email_hotmail()


#     O que mudou para o Hotmail?
# smtp-mail.outlook.com: Este é o endereço oficial para contas @hotmail.com, @outlook.com ou @live.com.

# server.ehlo(): No Hotmail, é uma boa prática chamar o comando ehlo() antes e depois do starttls() para garantir que o servidor reconheça as capacidades da conexão.

# Senha de App Microsoft:

# Vá para account.microsoft.com.

# Clique em Segurança > Opções de segurança avançadas.

# Procure por Senhas de aplicativo e clique em "Criar uma nova senha de aplicativo".

# Use essa senha de 16 caracteres no seu código.

# Se você não usar a "Senha de App", o Hotmail pode bloquear a conexão por considerá-la "menos segura", resultando em um erro similar ao que você recebeu no Gmail.
'''  