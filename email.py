import smtplib
import email.message

def enviar_email():
    corpo_email = """
    <p>Olá, Ganhador</p>
    <p>Você acabou de ganhar o sorteio!</p>
    """

    destinatario = input("Digite o email do destinatário: ")

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'paliomachine268@gmail.com'  # Insira seu email aqui
    msg['To'] = destinatario
    password = 'badq oysi tuah cbar'  # Insira sua senha aqui
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    try:
        s = smtplib.SMTP('smtp.gmail.com:587')
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print('Email enviado com sucesso para', destinatario)
    except Exception as e:
        print('Erro ao enviar o email:', str(e))
    finally:
        s.quit()  # Certifique-se de fechar a conexão SMTP

enviar_email()
