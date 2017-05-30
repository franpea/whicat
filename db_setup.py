from app import db
from models import QuestionSet

db.session.add(QuestionSet(QuestionSet_ID=1, QuestionNumber=1, QuestionText=u"Hello", RadioButtonLabel1=u"Not clear",
                           RadioButtonLabel2=u"Somewhatclear", RadioButtonLabel3=u"3", RadioButtonLabel4=u"4",
                           RadioButtonLabel5=u"5", QuestionHints=u"Hints",QuestionExamples=u"Examples"))
db.session.commit()

__tablename__ = "questionset"
QuestionSet_ID = db.Column(db.Integer, primary_key=True)
QuestionNumber = db.Column(db.Integer, primary_key=True)
QuestionText = db.Column(db.String(), unique=True)
RadioButtonLabel1 = db.Column(db.String(2))
RadioButtonLabel2 = db.Column(db.String(8))
RadioButtonLabel3 = db.Column(db.String(12))
RadioButtonLabel4 = db.Column(db.String(6))
RadioButtonLabel5 = db.Column(db.String(3))
QuestionHints = db.Column(db.String(), unique=True)
QuestionExamples = db.Column(db.String(), unique=True)
