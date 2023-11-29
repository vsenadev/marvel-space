class QuizUtils:
    def validate_responses(self, quiz, response_list):
        questions_and_responses = [(item['quest'], item['response']) for item in quiz['question_list']]
        print(questions_and_responses)