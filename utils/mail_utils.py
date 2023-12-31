import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class MailUtils:
    def send_token_email(self, mail, code):
        template = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Seu Código de Acesso</title>
        </head>
        <body>
            <p>Olá,</p>
            <p>Aqui está o seu código de acesso: <strong>{code}</strong></p>
            <p>Use este código para acessar o seguinte link: <strong>+++++++</strong></p>
            <p>Atenciosamente,</p>
            <p>Equipe de Suporte</p>
        </body>
        </html>
        """

        message = Mail(
            from_email='marvelspace2099@gmail.com',
            to_emails=mail,
            subject='Sending with Twilio SendGrid is Fun',
            html_content=template)
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            sg.send(message)

            return True
        except Exception as error:
            return False
