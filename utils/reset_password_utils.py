from utils.mail_utils import MailUtils
import random


class ResetPasswordUtils:
    mail_utils = MailUtils()

    def validate_attempt(self, email):
        code = self.generate_code()
        return self.mail_utils.send_token_email(email, code)

    def generate_code(self):
        random_numbers = []
        for _ in range(5):
            number = random.randint(1,9)
            random_numbers.append(number)

        number_str = ' '.join(map(str, random_numbers))

        return number_str

