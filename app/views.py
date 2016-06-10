from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

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


@app.route('/login', methods=['POST', 'GET'])
def login():
    """Return login form."""
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID={}, remember_me={}'.format(form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])
