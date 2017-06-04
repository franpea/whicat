from app import db

class Website(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(2083), index=True, unique=True)
    title = db.Column(db.String(64), index=True)
    assessments = db.relationship('Assessment', backref='url', lazy='dynamic')

    def __repr__(self):
        return '<Website %r>' % (self.title)

class Assessment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    answer1 = db.Column(db.Integer)
    answer2 = db.Column(db.Integer)
    answer3 = db.Column(db.Integer)
    answer4 = db.Column(db.Integer)
    answer5 = db.Column(db.Integer)
    answer6 = db.Column(db.Integer)
    answer7 = db.Column(db.Integer)
    answer8 = db.Column(db.Integer)
    answer9 = db.Column(db.Integer)
    answer10 = db.Column(db.Integer)
    answer11 = db.Column(db.Integer)
    answer12 = db.Column(db.Integer)
    website_id = db.Column(db.Integer, db.ForeignKey('website.id'))
    checklist_id = db.Column(db.Integer, db.ForeignKey('checklist.id'))

    def __repr__(self):
        return '<Assessment %r>' % (self.website_id.title)

class Checklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    questions = db.relationship('Question', backref='set', lazy='dynamic')

    def __repr__(self):
        return '<Checklist %r>' % (self.id)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    number = db.Column(db.Integer)
    text = db.Column(db.String(1028))
    button1 = db.Column(db.String(64))
    button2 = db.Column(db.String(64))
    button3 = db.Column(db.String(64))
    button4 = db.Column(db.String(64))
    button5 = db.Column(db.String(64))
    hint = db.Column(db.String(4096))
    example = db.Column(db.String(4096))
    checklist_id = db.Column(db.Integer, db.ForeignKey('checklist.id'))

    def __repr__(self):
        return '<Question %r>' % (self.text)