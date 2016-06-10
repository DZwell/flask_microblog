from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    """Return index."""
    user = {'name': 'DZ'}
    posts = [
        {
            'author': {'name': 'Bert'},
            'body': 'My what a beautiful day today.'
        },
        {
            'author': {'name': 'Bartran'},
            'body': 'Indded it is a beautiful day today.'
        }

    ]
    return render_template('index.html', title=None, user=user, posts=posts)
