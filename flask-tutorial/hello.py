from flask import Flask, url_for
from markupsafe import escape

## https://flask.palletsprojects.com/en/3.0.x/tutorial/ ##

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/login')
def login():
    return 'Hello, World'

@app.route('/user/<username>')

def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)} \'s profile'
# return "<p>Hello, {escape(name)} ,! hahahaha</p>"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('show_user_profile', username='John Doe'))
    