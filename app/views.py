import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from app import app
from .forms import LoginForm, UrlForm




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
        return redirect(url_for('question1'))
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
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    form = LoginForm()
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
						   user=user)

@app.route('/checklist/question/1', methods=['GET', 'POST'])
def question1():
    name = session['name']
    return render_template('checklist-Q1.html', name=name, title=reduceURL(name))

@app.route('/checklist/question/2', methods=['GET', 'POST'])
def question2():
    name = session['name']
    return render_template('checklist-Q2.html', name=name, title=reduceURL(name))


@app.route('/checklist/question/3', methods=['GET', 'POST'])
def question3():
    name = session['name']
    return render_template('checklist-Q3.html', name=name, title=reduceURL(name))


@app.route('/checklist/question/4', methods=['GET', 'POST'])
def question4():
    name = session['name']
    return render_template('checklist-Q4.html', name=name, title=reduceURL(name))


@app.route('/checklist/question/5', methods=['GET', 'POST'])
def question5():
    name = session['name']
    return render_template('checklist-Q5.html', name=name, title=reduceURL(name))


@app.route('/checklist/question/6', methods=['GET', 'POST'])
def question6():
    name = session['name']
    return render_template('checklist-Q6.html', name=name, title=reduceURL(name))


@app.route('/checklist/question/7', methods=['GET', 'POST'])
def question7():
    name = session['name']
    return render_template('checklist-Q7.html', name=name, title=reduceURL(name))


@app.route('/checklist/question/8', methods=['GET', 'POST'])
def question8():
    name = session['name']
    return render_template('checklist-Q8.html', name=name, title=reduceURL(name))


@app.route('/checklist/question/9', methods=['GET', 'POST'])
def question9():
    name = session['name']
    return render_template('checklist-Q9.html', name=name, title=reduceURL(name))


@app.route('/checklist/question/10', methods=['GET', 'POST'])
def question10():
    name = session['name']
    return render_template('checklist-Q10.html', name=name, title=reduceURL(name))


@app.route('/checklist/question/11', methods=['GET', 'POST'])
def question11():
    name = session['name']
    return render_template('checklist-Q11.html', name=name, title=reduceURL(name))


@app.route('/checklist/question/12', methods=['GET', 'POST'])
def question12():
    name = session['name']
    return render_template('checklist-Q12.html', name=name, title=reduceURL(name))

@app.route('/checklist/end')
def end():
    return render_template('checklist-end.html')
