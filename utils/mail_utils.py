import yagmail
import os
from dotenv import load_dotenv
import keyring
from flask import jsonify

dotenv_path = '.env'

load_dotenv(dotenv_path)

smtp_username = os.getenv('SENDER_MAIL')
smtp_password = os.getenv('MAIL_PASSWORD')


class MailUtils:
    def send_token_email(self, mail, code):
        try:
            yagmail.register(smtp_username, smtp_password)
            print(smtp_username, smtp_password)
            yag = yagmail.SMTP(smtp_username)
            yag.set_logging(yagmail.logging.DEBUG)
            yag.send(
                to=mail,
                subject='Código de redefinição',
                contents=f'Seu código de autenticação é: {code}'
            )

            return True
        except Exception as error:
            print(error)
            return False
