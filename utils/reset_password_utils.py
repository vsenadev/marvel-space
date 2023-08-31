from utils.mail_utils import MailUtils
from datetime import datetime, timedelta
import random


class ResetPasswordUtils:
    mail_utils = MailUtils()

    def validate_attempt(self, email):
        code = self.generate_code()
        send_code = self.mail_utils.send_token_email(email, code)
        return send_code, code

    def generate_code(self):
        random_numbers = []
        for _ in range(5):
            number = random.randint(1, 9)
            random_numbers.append(number)

        number_str = ' '.join(map(str, random_numbers))

        return number_str

    def get_time_limit(self):
        current_time = datetime.now()
        new_time = current_time + timedelta(minutes=5)

        formatted_hour = "%H:%M:%S"
        return new_time.strftime(formatted_hour)
