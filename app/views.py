from __future__ import division
from flask import render_template, flash, redirect, session, url_for, request, g, make_response
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid, models
from .forms import LoginForm
from .models import User, Question

@app.route('/')
@app.route('/index')
def index():
    navigation = [  # navigation menu items
        {
            'href': '/index', 
            'caption': 'Home' 
        },
        { 
            'href': '/checklist', 
            'caption': 'Checklist' 
        },
        { 
            'href': '/tutorial', 
            'caption': 'Tutorial' 
        },
        { 
            'href': '/login', 
            'caption': 'Login' 
        }
    ]
    return render_template('index.html',
                           title='Home',
						   navigation=navigation)

@app.route('/checklist')
def checklist():
    navigation = [  # navigation menu items
        {
            'href': '/index', 
            'caption': 'Home' 
        },
        { 
            'href': '/checklist', 
            'caption': 'Checklist' 
        },
        { 
            'href': '/tutorial', 
            'caption': 'Tutorial' 
        },
        { 
            'href': '/login', 
            'caption': 'Login' 
        }
    ]
    return render_template('checklist.html',
                           title='Checklist',
						   navigation=navigation)

@app.route('/checklist/question/<number>')
def question(number):
    question = Question.query.filter_by(number=number).first()
    if int(number) == 12:
        return redirect(url_for('lastquestion'))
    else:
        nextNum = int(number)+1
    navigation = [  # navigation menu items
        {
            'href': '/index', 
            'caption': 'Home' 
        },
        {
            'href': '/checklist', 
            'caption': 'Checklist' 
        },
        { 
            'href': '/tutorial', 
            'caption': 'Tutorial' 
        },
        { 
            'href': '/login', 
            'caption': 'Login' 
        }
    ]
    return render_template('question.html',
                           title='Checklist',
                           question=question,
                           nextNum=nextNum,
						   navigation=navigation)

@app.route('/lastquestion')
def lastquestion():
    question = Question.query.get(int(12))
    navigation = [  # navigation menu items
        {
            'href': '/index', 
            'caption': 'Home' 
        },
        {
            'href': '/checklist', 
            'caption': 'Checklist' 
        },
        { 
            'href': '/tutorial', 
            'caption': 'Tutorial' 
        },
        { 
            'href': '/login', 
            'caption': 'Login' 
        }
    ]
    return render_template('last-question.html',
                           title='Checklist',
                           question=question,
						   navigation=navigation)

@app.route('/checklist/complete')
def complete():
    navigation = [  # navigation menu items
        {
            'href': '/index', 
            'caption': 'Home' 
        },
        {
            'href': '/checklist', 
            'caption': 'Checklist' 
        },
        { 
            'href': '/tutorial',
            'caption': 'Tutorial' 
        },
        { 
            'href': '/login', 
            'caption': 'Login' 
        }
    ]
    return render_template('checklist-complete.html',
                           title='Checklist',
						   navigation=navigation)

@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.before_request
def before_request():
    g.user = current_user

@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('reports'))


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    navigation = [  # navigation menu items
        {
            'href': '/index', 
            'caption': 'Home' 
        },
        {
            'href': '/checklist', 
            'caption': 'Checklist' 
        },
        { 
            'href': '/tutorial', 
            'caption': 'Tutorial' 
        },
        { 
            'href': '/login', 
            'caption': 'Login' 
        }
    ]
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('reports'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html', 
                           title='Login',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'],
                           navigation=navigation)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


def calcAvg(answers):
	"""Returns average score for a website received based on completed assessments,
	BEWARE: assumes answer12 is not null."""
	score = 0
	for a in answers:
		score += a.answer12
	return score/len(answers)

def rankingDict(websites):
	"""Create a dict of website and average score."""
	tally = {}
	for w in websites:
		x = models.Website.query.get(w.id)
		answers = x.assessments.all()
		if len(answers) is not None:
			tally[w.title] = calcAvg(answers)
	return tally


@app.route('/reports')
@login_required
def reports():
    """Display website assessment ranking report."""
    navigation = [  # navigation menu items
        { 
            'href': '/logout', 
            'caption': 'Logout' 
        }
    ]
    user = g.user
    websites = models.Website.query.all()
    sitescores = rankingDict(websites)
    return render_template(
            'reports.html',
            navigation=navigation,
            sitescores=sitescores,
            user=user)