class QuizModel:
    def __init__(self, name: str, theme: str, login: str, questions_list: list):
        self.name = name
        self.theme = theme
        self.login = login
        self.question_list = questions_list
