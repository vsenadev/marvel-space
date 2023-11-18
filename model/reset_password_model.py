class ResetPassword:
    def __init__(self, email: str, code: int, time_limit):
        self.email = email
        self.code = code
        self.time_limit = time_limit
