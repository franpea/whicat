from app import db
import os.path
from models import QuestionSet

def updateQuestion(number, newQuestion):
    question = db.session.query(QuestionSet).filter_by(QuestionNumber=number)
    question.QuestionText = newQuestion
    db.session.commit()

updateQuestion(2, "What is a duck")
