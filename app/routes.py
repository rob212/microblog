from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Rob'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Edinburgh!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'I like coding in Python!'
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
