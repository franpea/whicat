from app import db


class QuestionSet(db.Model):
    QuestionSet_ID = db.Column(db.Integer, primary_key=True)
    QuestionNumber = db.Column(db.Integer, primary_key=True)
    QuestionText = db.Column(db.String(), index=True, unique=True)
    RadioButtonLabel1 = db.Column(db.String(2))
    RadioButtonLabel2 = db.Column(db.String(8))
    RadioButtonLabel3 = db.Column(db.String(12))
    RadioButtonLabel4 = db.Column(db.String(6))
    RadioButtonLabel5 = db.Column(db.String(3))
    QuestionHints = db.Column(db.String(),index=True, unique=True)
    QuestionExamples = db.Column(db.String(),index=True, unique=True)


class Tutorial(db.Model):
    Tutorial_ID = db.Column(db.Integer, primary_key=True)
    TutorialVersion = db.Column(db.Integer, primary_key=True)
    QuestionSet_ID = db.Column(db.Integer, foreign_key=True)
    QuestionNumber = db.Column(db.Integer, foreign_key=True)
    TutorialCategory = db.Column(db.String(6), index=True, unique=False)
    CorrectAnswer = db.Column(db.Integer, index=True, unique=False)
    ExpertFeedback = db.Column(db.String(), index=True, unique=True)


class UserAnswers(db.Model):
    Answers_ID = db.Column(db.Integer, primary_key=True)
    Session_ID = db.Column(db.String(), foreign_key=True)
    URL_ID = db.Column(db.Integer, foreign_key=True)
    QuestionSet_ID = db.Column(db.Integer, foreign_key=True)
    QuestionNumber1 = db.Column(db.Integer, index=False, unique=False)
    QuestionNumber2 = db.Column(db.Integer, index=False, unique=False)
    QuestionNumber3 = db.Column(db.Integer, index=False, unique=False)
    QuestionNumber4 = db.Column(db.Integer, index=False, unique=False)
    QuestionNumber5 = db.Column(db.Integer, index=False, unique=False)
    QuestionNumber6 = db.Column(db.Integer, index=False, unique=False)
    QuestionNumber7 = db.Column(db.Integer, index=False, unique=False)
    QuestionNumber8 = db.Column(db.Integer, index=False, unique=False)
    QuestionNumber9 = db.Column(db.Integer, index=False, unique=False)
    QuestionNumber10 = db.Column(db.Integer, index=False, unique=False)
    QuestionNumber11 = db.Column(db.Integer, index=False, unique=False)
    QuestionNumber12 = db.Column(db.Integer, index=False, unique=False)


class URLs(db.Model):
    URL_ID = db.Column(db.Integer, primary_key=True)
    URL = db.Column(db.String(), index=True, unique=False)
