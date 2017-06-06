import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from app import app
from .forms import LoginForm, UrlForm
from .models import Question



def reduceURL(url):
    if(url[4] == 's'):
        return url[8:]
    else:
        return url[7:]


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

@app.route('/checklist', methods=['GET', 'POST'])
def checklist():
    form = UrlForm()
    if request.method == 'POST':
        name = request.form['URL']
        print name
        session['name'] = name
        return redirect(url_for('question', number=1))
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
						   navigation=navigation,
                          form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = UrlForm()
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
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           navigation=navigation)

@app.route('/checklist/question/<number>', methods=['GET', 'POST'])
def question(number):
    name = session['name']
    question = Question.query.filter_by(number=number).first()
    if number == 12:
        print("ok")
        redirect(url_for('end'))
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
						   navigation=navigation,
                           url=name,
                           urlTitle=reduceURL(name))


@app.route('/checklist/end')
def end():
    return render_template('checklist-end.html',
                           title='Checklist Complete')
