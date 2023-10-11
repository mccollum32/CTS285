from flask import Flask;
from markupsafe import escape;

app = Flask(__name__)

### 
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

