# Quize game
class Quize:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

questions = [
    "1.what is the full form of ABC in python?\n a.Abstract Base class\n b.Apple Base class\n c.Nothing\n d.do not know",
    "2.what is the full form of OOPS in python?\n a.object oriented python\n b.object oriented programming language\nc.object oral programming",
    "3.what is the full form of ATM\n a.automatic teller machine\n b.automated telling machine\n c.automated teller macine",
]

quizList = [
    Quize(questions[0], 'a'),
    Quize(questions[1], 'b'),
    Quize(questions[2], 'c'),
]

def show(quizList):
    marks = 0
    for i in quizList:
        ask = input(f"{i.question}\n enter your answer: ")
        if ask == i.answer:
            marks += 1
        else:
            print(f"you chose the wrong answer, the correct answer is {i.answer} ")
    print(f"your marks is {marks/len(questions)*100}%")

show(quizList)
