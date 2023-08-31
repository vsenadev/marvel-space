class ResetPassword:
    def __init__(self, email, code, time_limit):
        self.email = email
        self.code = code
        self.time_limit = time_limit
