class ResetPasswordUtils:
    def validate_attempt(self, email):
        return self.collection.find({email: email})
