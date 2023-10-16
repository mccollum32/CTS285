from flask import Flask;
##Used to import Variable rules for flask EX.<variable name>
from markupsafe import escape;
##Used to import Methods
from flask import request;
##used to import CSS + HTML 
from flask import render_template;
##Used to import Url Building
from flask import url_for;


app = Flask(__name__)

### This routes the user to where the page/active page is 
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def hello(name):
    return f"<p>Hello, {escape(name)}!</p>"

@app.route("/")
def index():
    return "<p>Indexing Page</p>"


@app.route("/user/<username>")
def ShowUserProfile(username):
    # shows the users username information 
    return f"User {escape(username)}"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


#### This shows the unique urls for the pages 
@app.route('/projects/')
def projects():
    return 'Project Page'

@app.route('/about')
def about():
    return 'About Page'

## URL redirections, this will redirect the user if no '/' is given in the url 
@app.route('/projects/')
def projects():
    return 'The Project page'

@app.route('/about')
def about():
    return 'The about page'

## These are the Url Templates

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login' , next='/'))
    print(url_for('profile', username = 'John Doe'))
    
##Http/ Url methods using Get
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.meethod == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()

#Static Files/Folder CSS for styling the page
url_for('static', filename='style.css')

##To render the templates
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)