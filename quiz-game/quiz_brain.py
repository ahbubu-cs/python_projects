class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions_list

    def next_question(self):
        item = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {item.text} (True/False)?: ")
        self.check_answer(user_answer, item.answer)

    def still_has_question(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, real_answer):
        if real_answer.lower() == user_answer.lower():
            print("You got it right!")
            self.score += 1

        else:
            print("You got it wrong!")
        print(f"The correct answer is {real_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")
