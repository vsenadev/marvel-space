from utils.mail_utils import MailUtils

class ResetPasswordUtils:
    mail_utils = MailUtils()
    def validate_attempt(self):
        self.mail_utils.send_token_email()
        # return self.collection.find({email: email})
