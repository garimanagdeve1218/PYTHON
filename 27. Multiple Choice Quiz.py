#Building a multiple choice quiz in python:

#in file Questions.py
class Question:
    def __init__(self, prompt, answer):      #every question willl have a question prompt and a answer for that question.
        self.prompt = prompt
        self.answer = answer

#in file app.py

from Question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

#let's start creating question objects:

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

#now let's write a function that will run the test:

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "correct.")

run_test(questions)

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
What color are apples?
(a) Red/Green
(b) Purple
(c) Orange

a
What color are Bananas?
(a) Teal
(b) Magenta
(c) Yellow

c
What color are strawberries?
(a) Yellow
(b) Red
(c) Blue

a
You got 2/3correct.

Process finished with exit code 0
