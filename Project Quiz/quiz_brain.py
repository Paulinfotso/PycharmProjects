class QuizBrain:

    def __int__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        choice = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False) ? : ").capitalize()