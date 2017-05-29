from flask import render_template
from app import app
from .forms import LoginForm

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