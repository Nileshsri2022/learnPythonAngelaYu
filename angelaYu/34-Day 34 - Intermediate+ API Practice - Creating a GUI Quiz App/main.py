"""Day 34 project: Quizzler — the GUI quiz app with live Trivia API data.

Requires ui.py, quiz_brain.py, question_model.py, data.py and images/.
"""

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

import html

question_bank = []
for question in question_data:
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    question_bank.append(Question(question_text, question_answer))

quiz = QuizBrain(question_bank)
QuizInterface(quiz)
