from classes import enviarEmail

corpo_email = """
        <p> Boa noite,</p>
        <p> Segue meu email automático. </p>
        """
Subject = 'Email_automático' #Assunto
From = 'fcpierna@gmail.com' #remetente
To = 'fcpierna@gmail.com' #destinatário - mais de um email separar por vírgula
password = 'uvuo oekt erwb nnhq' #senha do aplicativo

objEnviarEmail = enviarEmail(Subject, From, To, password, corpo_email) #Instanciando a classe - criando um obj que chama objEnviarEmail

retornoGmail = objEnviarEmail.enviandoEmail()

print(retornoGmail)