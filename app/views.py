from app import app

@app.route('/')
@app.route('/index')
def index():
    """Return hello world."""
    return 'Hello world.'
