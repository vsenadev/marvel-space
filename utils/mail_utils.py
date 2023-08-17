import yagmail
import os
from dotenv import load_dotenv
import keyring

dotenv_path = '.env'

load_dotenv(dotenv_path)

smtp_username = os.getenv('SENDER_MAIL')
smtp_password = os.getenv('MAIL_PASSWORD')


class MailUtils:
    def send_token_email(self):
        try:
            yagmail.register(smtp_username, smtp_password)
            print(smtp_username, smtp_password)
            yag = yagmail.SMTP(smtp_username)
            yag.set_logging(yagmail.logging.DEBUG)
            yag.send(
                to='senavinicius01@gmail.com',
                subject='teste',
                contents='Ola, testando'
            )
            print('Enviou')
            return True
        except Exception as error:
            print("Erro ao enviar e-mail:", error)
            return False
