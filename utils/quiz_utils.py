class QuizUtils:
    def validate_responses(self, quiz, response_list):
        questions_and_responses = [(item['quest'], item['response']) for item in quiz['question_list']]
        correct_answer = 0

        for question, response in questions_and_responses:
            for item in response_list:
                if item['quest'] == question:
                    if item['answer'] == response:
                        correct_answer += 1

        return correct_answer * 10
